#!/usr/bin/env python3
"""
Script to analyze Daniel Priestley video transcripts and create a markdown summary
"""

import json
import os
from pathlib import Path
import anthropic
import sys

def load_transcript(json_file):
    """Load transcript from JSON file"""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_full_text_with_timestamps(transcript_data):
    """Convert transcript data to full text with timestamp markers"""
    lines = []
    prev_text = None

    for i, entry in enumerate(transcript_data):
        # Skip duplicates
        if entry['text'] != prev_text:
            # Add timestamp markers at meaningful intervals (every ~30 seconds)
            if i == 0 or entry['seconds'] % 30 < 5:
                lines.append(f"\n[{entry['seconds']}s] {entry['text']}")
            else:
                lines.append(entry['text'])
            prev_text = entry['text']

    return ' '.join(lines)

def analyze_video(video_data, client):
    """Analyze a single video transcript using Claude"""
    print(f"\nAnalyzing: {video_data['title']}")

    full_text = get_full_text_with_timestamps(video_data['transcript'])

    prompt = f"""Analyze this transcript from Daniel Priestley's video titled "{video_data['title']}".

Transcript with timestamp markers:
{full_text}

Please provide:

1. **Main Theme** (1-2 sentences): What is the core message of this video?

2. **Key Takeaways** (3-7 bullet points): The most important insights and actionable advice from the video.

3. **Notable Quotes** (2-4 quotes): Memorable or impactful statements from the video. Include approximate timestamps based on the [Xs] markers in the transcript.

4. **Key Sections** (3-5 sections): Break down the video into major segments with their approximate start times (in seconds) and brief descriptions.

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

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = message.content[0].text

        # Extract JSON from response (might have markdown code fences)
        if '```json' in response_text:
            response_text = response_text.split('```json')[1].split('```')[0].strip()
        elif '```' in response_text:
            response_text = response_text.split('```')[1].split('```')[0].strip()

        analysis = json.loads(response_text)
        print(f"✓ Analysis complete")
        return analysis

    except Exception as e:
        print(f"✗ Error analyzing video: {e}")
        return None

def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS or MM:SS format"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

def create_markdown_summary(all_analyses, output_file):
    """Create a comprehensive markdown summary"""

    md_content = """# Daniel Priestley Video Transcripts - Analysis & Key Takeaways

This document provides a comprehensive analysis of all videos from Daniel Priestley's YouTube channel, with main themes, key takeaways, and direct timestamp links to important sections.

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
    script_dir = Path(__file__).parent

    # Check for API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Please set it with: export ANTHROPIC_API_KEY='your-key-here'")
        return

    client = anthropic.Anthropic(api_key=api_key)

    print("=" * 60)
    print("Daniel Priestley Transcript Analyzer")
    print("=" * 60)

    # Find all JSON files
    json_files = sorted(script_dir.glob('*.json'))

    if not json_files:
        print("No JSON transcript files found")
        return

    print(f"Found {len(json_files)} transcripts to analyze\n")

    all_analyses = []

    for json_file in json_files:
        video_data = load_transcript(json_file)
        analysis = analyze_video(video_data, client)
        all_analyses.append((video_data, analysis))

    # Create markdown summary
    output_file = script_dir / "Daniel_Priestley_Video_Analysis.md"
    create_markdown_summary(all_analyses, output_file)

    print("\n" + "=" * 60)
    print(f"Analysis complete! Check: {output_file}")
    print("=" * 60)

if __name__ == '__main__':
    main()
