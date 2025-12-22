#!/usr/bin/env python3
"""
Script to download transcripts with timestamps from any YouTube channel
Usage: python3 download_channel_transcripts.py <channel_url> [output_dir]
"""

import os
import subprocess
import json
import re
import sys
from pathlib import Path

def get_channel_info(channel_url):
    """Get channel name from URL"""
    cmd = [
        'yt-dlp',
        '--flat-playlist',
        '--print', 'channel',
        '--playlist-items', '1',
        channel_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        channel_name = result.stdout.strip()
        return channel_name
    except subprocess.CalledProcessError as e:
        print(f"Error getting channel info: {e}")
        return None

def get_video_urls(channel_url):
    """Fetch all video URLs from a YouTube channel"""
    print(f"Fetching video list from: {channel_url}")

    cmd = [
        'yt-dlp',
        '--flat-playlist',
        '--print', '%(id)s',
        '--print', 'title',
        channel_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')

        videos = []
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                videos.append({
                    'id': lines[i],
                    'url': f'https://www.youtube.com/watch?v={lines[i]}',
                    'title': lines[i + 1]
                })

        print(f"Found {len(videos)} videos")
        return videos
    except subprocess.CalledProcessError as e:
        print(f"Error fetching video list: {e}")
        print(f"stderr: {e.stderr}")
        return []

def parse_vtt_with_timestamps(vtt_file_path):
    """Parse VTT file and extract text with timestamps"""
    try:
        with open(vtt_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split into cue blocks
        blocks = re.split(r'\n\n+', content)

        transcript_data = []
        for block in blocks:
            # Look for timestamp line
            timestamp_match = re.search(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})', block)
            if timestamp_match:
                start_time = timestamp_match.group(1)
                # Convert to seconds for YouTube URL
                time_parts = start_time.split(':')
                seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + float(time_parts[2])

                # Extract text (everything after the timestamp line)
                lines = block.split('\n')
                text_lines = []
                found_timestamp = False
                for line in lines:
                    if '-->' in line:
                        found_timestamp = True
                        continue
                    if found_timestamp and line.strip():
                        # Remove HTML tags
                        clean_line = re.sub(r'<[^>]+>', '', line.strip())
                        if clean_line:
                            text_lines.append(clean_line)

                if text_lines:
                    text = ' '.join(text_lines)
                    transcript_data.append({
                        'timestamp': start_time,
                        'seconds': int(seconds),
                        'text': text
                    })

        return transcript_data
    except Exception as e:
        print(f"  Error parsing VTT: {e}")
        return []

def download_transcript(video_info, output_dir):
    """Download transcript for a single video"""
    print(f"\nDownloading transcript for: {video_info['title']}")

    safe_title = "".join(c for c in video_info['title'] if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title[:200]

    cmd = [
        'yt-dlp',
        '--skip-download',
        '--write-subs',
        '--write-auto-subs',
        '--sub-format', 'vtt',
        '--sub-langs', 'en',
        '-o', f'{output_dir}/{safe_title}.%(ext)s',
        video_info['url']
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        vtt_file = f'{output_dir}/{safe_title}.en.vtt'
        if os.path.exists(vtt_file):
            # Parse VTT with timestamps
            transcript_data = parse_vtt_with_timestamps(vtt_file)

            if transcript_data:
                # Save as JSON with timestamps
                json_file = f'{output_dir}/{safe_title}.json'
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        'video_id': video_info['id'],
                        'title': video_info['title'],
                        'url': video_info['url'],
                        'transcript': transcript_data
                    }, f, indent=2, ensure_ascii=False)

                # Also create a readable text version with timestamps
                txt_file = f'{output_dir}/{safe_title}.timestamped.txt'
                with open(txt_file, 'w', encoding='utf-8') as f:
                    prev_text = None
                    for entry in transcript_data:
                        # Remove duplicate consecutive entries
                        if entry['text'] != prev_text:
                            f.write(f"[{entry['timestamp']}] {entry['text']}\n")
                            prev_text = entry['text']

                # Remove VTT file
                os.remove(vtt_file)

                print(f"✓ Downloaded transcript with timestamps: {video_info['title']}")
                return True

        return False
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to download transcript for: {video_info['title']}")
        print(f"  Error: {e.stderr}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 download_channel_transcripts.py <channel_url> [output_dir]")
        print("Example: python3 download_channel_transcripts.py https://www.youtube.com/@DanielPriestley/videos")
        sys.exit(1)

    channel_url = sys.argv[1]

    # Get channel name for directory
    channel_name = get_channel_info(channel_url)
    if not channel_name:
        channel_name = "Unknown_Channel"

    # Sanitize channel name for directory
    safe_channel_name = "".join(c for c in channel_name if c.isalnum() or c in (' ', '-', '_')).strip()

    # Determine output directory
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = Path(__file__).parent / safe_channel_name

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("YouTube Channel Transcript Downloader (with Timestamps)")
    print("=" * 60)
    print(f"Channel: {channel_name}")
    print(f"Output directory: {output_dir}")
    print("=" * 60)

    try:
        subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: yt-dlp is not installed")
        return

    videos = get_video_urls(channel_url)
    if not videos:
        return

    print(f"\nStarting downloads to: {output_dir}")
    print("=" * 60)

    successful = 0
    failed = 0

    for i, video in enumerate(videos, 1):
        print(f"\n[{i}/{len(videos)}]", end=" ")
        if download_transcript(video, output_dir):
            successful += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    print(f"Summary: {successful} successful, {failed} failed")
    print(f"Transcripts saved to: {output_dir}")
    print("=" * 60)

if __name__ == '__main__':
    main()
