#!/usr/bin/env python3
"""
Script to download transcripts from all videos on a YouTube channel using yt-dlp
"""

import os
import subprocess
import json
import re
from pathlib import Path

def get_video_urls(channel_url):
    """Fetch all video URLs from a YouTube channel"""
    print(f"Fetching video list from: {channel_url}")

    # Use yt-dlp to get video URLs from the channel
    cmd = [
        'yt-dlp',
        '--flat-playlist',
        '--print', 'url',
        '--print', 'title',
        channel_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')

        # Parse alternating lines (URL, title, URL, title, ...)
        videos = []
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                videos.append({
                    'url': lines[i],
                    'title': lines[i + 1]
                })

        print(f"Found {len(videos)} videos")
        return videos
    except subprocess.CalledProcessError as e:
        print(f"Error fetching video list: {e}")
        print(f"stderr: {e.stderr}")
        return []

def convert_vtt_to_txt(vtt_file_path):
    """Convert VTT subtitle file to plain text"""
    try:
        with open(vtt_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove VTT header
        content = re.sub(r'WEBVTT\n.*?\n\n', '', content, flags=re.DOTALL)

        # Remove timestamps and cue identifiers
        content = re.sub(r'\d+\n', '', content)
        content = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}.*?\n', '', content)

        # Remove VTT formatting tags
        content = re.sub(r'<[^>]+>', '', content)

        # Remove duplicate lines and extra whitespace
        lines = [line.strip() for line in content.split('\n') if line.strip()]

        # Join lines into paragraphs (every sentence on new line, but group similar content)
        text = '\n'.join(lines)

        # Save as txt file
        txt_file_path = vtt_file_path.replace('.vtt', '.txt')
        with open(txt_file_path, 'w', encoding='utf-8') as f:
            f.write(text)

        # Remove the original VTT file
        os.remove(vtt_file_path)

        return txt_file_path
    except Exception as e:
        print(f"  Warning: Could not convert VTT to TXT: {e}")
        return None

def download_transcript(video_url, video_title, output_dir):
    """Download transcript for a single video"""
    print(f"\nDownloading transcript for: {video_title}")

    # Sanitize filename
    safe_title = "".join(c for c in video_title if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title[:200]  # Limit length

    cmd = [
        'yt-dlp',
        '--skip-download',  # Don't download video
        '--write-subs',     # Write subtitles
        '--write-auto-subs', # Write auto-generated subs if manual not available
        '--sub-format', 'vtt',  # Format
        '--sub-langs', 'en',    # English only
        '-o', f'{output_dir}/{safe_title}.%(ext)s',  # Output template
        video_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        # Find the VTT file and convert it to TXT
        vtt_file = f'{output_dir}/{safe_title}.en.vtt'
        if os.path.exists(vtt_file):
            txt_file = convert_vtt_to_txt(vtt_file)
            if txt_file:
                print(f"✓ Downloaded and converted transcript for: {video_title}")
                return True

        print(f"✓ Downloaded transcript for: {video_title}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to download transcript for: {video_title}")
        print(f"  Error: {e.stderr}")
        return False

def main():
    # Configuration
    channel_url = 'https://www.youtube.com/@DanielPriestley/videos'
    output_dir = Path(__file__).parent  # Current directory

    print("=" * 60)
    print("YouTube Channel Transcript Downloader")
    print("=" * 60)

    # Check if yt-dlp is installed
    try:
        subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: yt-dlp is not installed or not in PATH")
        print("Install it with: pip install yt-dlp")
        return

    # Get all video URLs
    videos = get_video_urls(channel_url)

    if not videos:
        print("No videos found or error occurred")
        return

    # Download transcripts for each video
    print(f"\nStarting transcript downloads to: {output_dir}")
    print("=" * 60)

    successful = 0
    failed = 0

    for i, video in enumerate(videos, 1):
        print(f"\n[{i}/{len(videos)}]", end=" ")
        if download_transcript(video['url'], video['title'], output_dir):
            successful += 1
        else:
            failed += 1

    # Summary
    print("\n" + "=" * 60)
    print(f"Download Summary:")
    print(f"  Total videos: {len(videos)}")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print("=" * 60)

if __name__ == '__main__':
    main()
