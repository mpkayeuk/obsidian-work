#!/usr/bin/env python3
"""
Extract key segments from transcripts for analysis
"""

import json
from pathlib import Path

def extract_segments(json_file, num_segments=10):
    """Extract evenly spaced segments from transcript"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    transcript = data['transcript']
    total_entries = len(transcript)

    if total_entries == 0:
        return None

    # Calculate interval to get evenly spaced segments
    interval = max(1, total_entries // num_segments)

    segments = []
    seen_texts = set()

    for i in range(0, total_entries, interval):
        entry = transcript[i]
        # Skip duplicates
        if entry['text'] not in seen_texts:
            segments.append({
                'timestamp': entry['timestamp'],
                'seconds': entry['seconds'],
                'text': entry['text']
            })
            seen_texts.add(entry['text'])

        if len(segments) >= num_segments:
            break

    return {
        'video_id': data['video_id'],
        'title': data['title'],
        'url': data['url'],
        'segments': segments
    }

def main():
    script_dir = Path(__file__).parent
    json_files = sorted(script_dir.glob('*.json'))

    print(f"Extracting key segments from {len(json_files)} transcripts...\n")

    all_summaries = []

    for json_file in json_files:
        print(f"Processing: {json_file.stem}")
        summary = extract_segments(json_file, num_segments=15)
        if summary:
            all_summaries.append(summary)

    # Save extracted summaries
    output_file = script_dir / "transcript_summaries.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_summaries, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Summaries extracted to: {output_file}")

if __name__ == '__main__':
    main()
