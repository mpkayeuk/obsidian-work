#!/usr/bin/env python3
"""
Master script to download and analyze transcripts from any YouTube channel
Usage: python3 process_channel.py <channel_url> [output_base_dir]
"""

import sys
import subprocess
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process_channel.py <channel_url> [output_base_dir]")
        print("Example: python3 process_channel.py https://www.youtube.com/@DanielPriestley/videos")
        sys.exit(1)

    channel_url = sys.argv[1]

    # Determine base directory
    if len(sys.argv) >= 3:
        base_dir = Path(sys.argv[2])
    else:
        base_dir = Path(__file__).parent

    script_dir = Path(__file__).parent

    print("=" * 70)
    print("YouTube Channel Processor - Download & Analyze Transcripts")
    print("=" * 70)
    print(f"Channel URL: {channel_url}")
    print(f"Base directory: {base_dir}")
    print("=" * 70)

    # Step 1: Download transcripts
    print("\n" + "=" * 70)
    print("STEP 1: Downloading Transcripts")
    print("=" * 70)

    download_script = script_dir / "download_channel_transcripts.py"
    download_cmd = ["python3", str(download_script), channel_url, str(base_dir)]

    try:
        result = subprocess.run(download_cmd, check=True)
        if result.returncode != 0:
            print("Error downloading transcripts")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running download script: {e}")
        sys.exit(1)

    # Get the created directory (it will be in base_dir with channel name)
    # We need to find it
    transcript_dirs = [d for d in base_dir.iterdir() if d.is_dir() and (d / "*.json")]
    if not transcript_dirs:
        print("Could not find transcript directory")
        sys.exit(1)

    # Use the most recently modified directory
    transcript_dir = max(transcript_dirs, key=lambda d: d.stat().st_mtime)

    # Step 2: Analyze transcripts
    print("\n" + "=" * 70)
    print("STEP 2: Analyzing Transcripts with AI")
    print("=" * 70)

    analyze_script = script_dir / "analyze_channel_batch.py"
    analyze_cmd = ["python3", str(analyze_script), str(transcript_dir)]

    try:
        result = subprocess.run(analyze_cmd, check=True)
        if result.returncode != 0:
            print("Error analyzing transcripts")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running analysis script: {e}")
        sys.exit(1)

    print("\n" + "=" * 70)
    print("✓ COMPLETE! All transcripts downloaded and analyzed.")
    print(f"Results in: {transcript_dir}")
    print("=" * 70)

if __name__ == '__main__':
    main()
