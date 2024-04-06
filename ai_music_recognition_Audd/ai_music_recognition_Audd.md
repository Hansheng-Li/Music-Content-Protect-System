# YouTube Audio Downloader and Audd.io API Uploader

This document describes a Python script designed for downloading audio from YouTube videos and uploading it to the Audd.io API for music recognition. This script is useful for identifying songs, artists, and additional metadata from any YouTube video containing music.

## Requirements

To use this script, you will need Python installed on your system along with the `pytube` and `requests` libraries. You can install these libraries using pip:

```bash
pip install pytube requests
```

## How It Works

1. **Download Audio from YouTube**: The script uses `pytube` to download the audio track of a YouTube video.
2. **Upload Audio to Audd.io**: The audio file is then uploaded to the Audd.io API, which analyzes the audio and returns information about the song, including the artist, title, album, release date, and more.

## Usage

1. Replace `your YouTube video link here` in the script with the YouTube video link you want to analyze.
2. Replace `'test'` in the `api_token` field with your actual Audd.io API token.
3. Run the script. The output will be printed to the console.

## Example

As a test, the video at `https://www.youtube.com/watch?v=8_B2epQhz4c` was used, titled "Taylor Swift—Starboy (AI) by The Weeknd". The script successfully identified the song as "Starboy" by The Weeknd, with the following details:

- **Artist**: The Weeknd
- **Title**: Starboy
- **Album**: BRIT Awards 2017
- **Release Date**: 2016-09-22
- **Label**: Universal-Island Records Ltd.
- **Timecode**: 00:14
- **Song Link**: [https://lis.tn/zWWXBb](https://lis.tn/zWWXBb)

## Conclusion

This script demonstrates a practical application of the `pytube` and `requests` libraries for downloading YouTube audio and utilizing music recognition services. It's a powerful tool for music enthusiasts and developers interested in audio analysis and music identification.
