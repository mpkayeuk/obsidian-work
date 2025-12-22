#!/usr/bin/env python3
"""
Script to analyze video transcripts using Anthropic Batch API
Usage: python3 analyze_channel_batch.py <transcript_directory>
"""

import json
import os
import time
import sys
from pathlib import Path
import anthropic

def get_text_sample(transcript_data, num_samples=20):
    """Get representative text samples from transcript"""
    total_entries = len(transcript_data)
    if total_entries == 0:
        return ""

    # Calculate interval to get evenly spaced samples
    interval = max(1, total_entries // num_samples)

    samples = []
    seen_texts = set()

    for i in range(0, total_entries, interval):
        entry = transcript_data[i]
        # Skip duplicates
        if entry['text'] not in seen_texts and len(entry['text']) > 20:
            samples.append(f"[{entry['seconds']}s] {entry['text']}")
            seen_texts.add(entry['text'])

        if len(samples) >= num_samples:
            break

    return ' '.join(samples)

def create_batch_requests(json_files, channel_name="Channel"):
    """Create batch requests for all transcripts"""
    requests = []

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            video_data = json.load(f)

        # Get representative samples from transcript
        text_sample = get_text_sample(video_data['transcript'], num_samples=30)

        prompt = f"""Analyze this transcript from a video titled "{video_data['title']}" from the {channel_name} YouTube channel.

Below are key samples from the transcript with timestamps in seconds:

{text_sample}

Based on these samples, please provide:

1. **Main Theme** (1-2 sentences): What is the core message of this video?

2. **Key Takeaways** (5-8 bullet points): The most important insights and actionable advice from the video.

3. **Notable Quotes** (3-5 quotes): Memorable or impactful statements from the video. Include approximate timestamps in seconds based on the [Xs] markers.

4. **Key Sections** (4-6 sections): Break down the video into major segments with their approximate start times (in seconds) and brief descriptions.

Format your response as structured JSON:
{{
  "theme": "...",
  "takeaways": ["...", "..."],
  "quotes": [
    {{"quote": "...", "timestamp_seconds": 123}}
  ],
  "sections": [
    {{"title": "...", "timestamp_seconds": 0, "description": "..."}}
  ]
}}"""

        # Create batch request
        request = {
            "custom_id": video_data['video_id'],
            "params": {
                "model": "claude-sonnet-4-5-20250929",
                "max_tokens": 2500,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        }

        requests.append({
            'request': request,
            'video_data': video_data
        })

    return requests

def submit_batch(client, requests):
    """Submit batch requests to Anthropic"""
    print(f"Submitting batch with {len(requests)} requests to Anthropic API...")

    # Prepare batch requests
    batch_requests = [item['request'] for item in requests]

    # Create message batch
    try:
        message_batch = client.messages.batches.create(
            requests=batch_requests
        )

        print(f"✓ Batch submitted successfully!")
        print(f"  Batch ID: {message_batch.id}")
        print(f"  Status: {message_batch.processing_status}")

        return message_batch.id

    except Exception as e:
        print(f"✗ Error submitting batch: {e}")
        import traceback
        traceback.print_exc()
        return None

def poll_batch_status(client, batch_id, poll_interval=10):
    """Poll batch status until completion"""
    print(f"\nPolling batch status (checking every {poll_interval}s)...")

    while True:
        try:
            batch = client.messages.batches.retrieve(batch_id)
            status = batch.processing_status

            # Calculate progress
            total = batch.request_counts.processing + batch.request_counts.succeeded + batch.request_counts.errored + batch.request_counts.canceled + batch.request_counts.expired
            completed = batch.request_counts.succeeded + batch.request_counts.errored

            progress_pct = (completed / total * 100) if total > 0 else 0

            print(f"  Status: {status} | Progress: {completed}/{total} ({progress_pct:.1f}%) | Succeeded: {batch.request_counts.succeeded} | Errors: {batch.request_counts.errored}")

            if status == "ended":
                print(f"\n✓ Batch processing complete!")
                print(f"  Total requests: {total}")
                print(f"  Succeeded: {batch.request_counts.succeeded}")
                print(f"  Errors: {batch.request_counts.errored}")
                return batch

            time.sleep(poll_interval)

        except Exception as e:
            print(f"✗ Error polling batch status: {e}")
            return None

def retrieve_batch_results(client, batch_id):
    """Retrieve results from completed batch"""
    print(f"\nRetrieving batch results...")

    try:
        # Get results as iterator
        results = []
        for result in client.messages.batches.results(batch_id):
            results.append(result)

        print(f"✓ Retrieved {len(results)} results")
        return results

    except Exception as e:
        print(f"✗ Error retrieving results: {e}")
        return []

def parse_batch_results(results, requests_data):
    """Parse batch results and match with video data"""
    analyses = []

    # Create lookup map
    video_lookup = {item['request']['custom_id']: item['video_data'] for item in requests_data}

    for result in results:
        custom_id = result.custom_id
        video_data = video_lookup.get(custom_id)

        if not video_data:
            continue

        # Check if request succeeded
        if result.result.type == "succeeded":
            try:
                response_text = result.result.message.content[0].text

                # Extract JSON from response
                if '```json' in response_text:
                    response_text = response_text.split('```json')[1].split('```')[0].strip()
                elif '```' in response_text:
                    response_text = response_text.split('```')[1].split('```')[0].strip()

                analysis = json.loads(response_text)
                analyses.append((video_data, analysis))
                print(f"  ✓ Parsed: {video_data['title']}")

            except Exception as e:
                print(f"  ✗ Error parsing {video_data['title']}: {e}")
                analyses.append((video_data, None))
        else:
            print(f"  ✗ Request failed for {video_data['title']}: {result.result.type}")
            analyses.append((video_data, None))

    return analyses

def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS or MM:SS format"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

def create_markdown_summary(all_analyses, output_file, channel_name="Channel"):
    """Create a comprehensive markdown summary"""

    md_content = f"""# {channel_name} Video Transcripts - Analysis & Key Takeaways

This document provides a comprehensive analysis of videos from the {channel_name} YouTube channel, with main themes, key takeaways, and direct timestamp links to important sections.

---

"""

    for video_data, analysis in all_analyses:
        if not analysis:
            continue

        video_id = video_data['video_id']
        title = video_data['title']
        url = video_data['url']

        md_content += f"\n## [{title}]({url})\n\n"

        # Theme
        md_content += f"### 🎯 Main Theme\n\n{analysis['theme']}\n\n"

        # Key Takeaways
        md_content += f"### 💡 Key Takeaways\n\n"
        for takeaway in analysis['takeaways']:
            md_content += f"- {takeaway}\n"
        md_content += "\n"

        # Key Sections
        if 'sections' in analysis and analysis['sections']:
            md_content += f"### 📍 Key Sections\n\n"
            for section in analysis['sections']:
                timestamp_sec = section['timestamp_seconds']
                timestamp_str = format_timestamp(timestamp_sec)
                section_url = f"{url}&t={timestamp_sec}s"
                md_content += f"**[{timestamp_str}]({section_url})** - **{section['title']}**\n"
                md_content += f"  {section['description']}\n\n"

        # Notable Quotes
        if 'quotes' in analysis and analysis['quotes']:
            md_content += f"### 💬 Notable Quotes\n\n"
            for quote_data in analysis['quotes']:
                timestamp_sec = quote_data['timestamp_seconds']
                timestamp_str = format_timestamp(timestamp_sec)
                quote_url = f"{url}&t={timestamp_sec}s"
                md_content += f"> *\"{quote_data['quote']}\"*\n"
                md_content += f">  \n> [Watch at {timestamp_str}]({quote_url})\n\n"

        md_content += "---\n\n"

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"\n✓ Markdown summary created: {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_channel_batch.py <transcript_directory>")
        print("Example: python3 analyze_channel_batch.py ./Daniel_Priestley")
        sys.exit(1)

    transcript_dir = Path(sys.argv[1])

    if not transcript_dir.exists():
        print(f"Error: Directory does not exist: {transcript_dir}")
        sys.exit(1)

    # Get channel name from directory
    channel_name = transcript_dir.name

    # Check for API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Please set it with: export ANTHROPIC_API_KEY='your-key-here'")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print("=" * 60)
    print(f"{channel_name} Transcript Analyzer (Batch Mode)")
    print("=" * 60)

    # Find all JSON files (exclude summary files)
    json_files = sorted([f for f in transcript_dir.glob('*.json') if 'summar' not in f.name.lower()])

    if not json_files:
        print(f"No JSON transcript files found in {transcript_dir}")
        sys.exit(1)

    print(f"Found {len(json_files)} transcripts to analyze\n")

    # Create batch requests
    print("Step 1: Creating batch requests...")
    requests_data = create_batch_requests(json_files, channel_name)

    # Submit batch
    print("\nStep 2: Submitting batch...")
    batch_id = submit_batch(client, requests_data)

    if not batch_id:
        print("Failed to submit batch")
        sys.exit(1)

    # Poll for completion
    print("\nStep 3: Waiting for batch to complete...")
    batch = poll_batch_status(client, batch_id)

    if not batch:
        print("Failed to complete batch")
        sys.exit(1)

    # Retrieve results
    print("\nStep 4: Retrieving results...")
    results = retrieve_batch_results(client, batch_id)

    if not results:
        print("No results retrieved")
        sys.exit(1)

    # Parse results
    print("\nStep 5: Parsing results...")
    all_analyses = parse_batch_results(results, requests_data)

    # Create markdown summary
    print("\nStep 6: Creating markdown summary...")
    output_file = transcript_dir / f"{channel_name}_Video_Analysis.md"
    create_markdown_summary(all_analyses, output_file, channel_name)

    print("\n" + "=" * 60)
    print(f"Analysis complete! Check: {output_file}")
    print("=" * 60)

if __name__ == '__main__':
    main()
