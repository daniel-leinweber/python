#!/usr/bin/env python3

import sys, argparse
from pytube import YouTube
from pytube import Playlist

def download(url, output_directory):
    youtube = YouTube(url)

    # Show video details
    print("Downloading video: ", youtube.title)

    # Get highest resolution possible
    youtube_stream = youtube.streams.get_highest_resolution()

    # Start download
    youtube_stream.download(output_directory)
    print("Download completed! Video saved to: ", output_directory + "/" + youtube.title)

def main(argv):
    url = ""
    output_directory = ""
    if len(argv) >= 1:
        parser = argparse.ArgumentParser(description="YouTube-Downloader v1.0.0")
        parser.add_argument("-u", "--url", help="YouTube video or playlist URL", required=True, type=str)
        parser.add_argument("-o", "--outputDirectory", help="Output directory of the video download", required=False, type=str, default="/Users/daniel/Downloads")
        args = parser.parse_args()
        url = args.url
        output_directory = args.outputDirectory
    else:
        # Ask for the video link from user
        url = input("Please enter the YouTube video or playlist URL: ")

        # Ask for the output directory from user
        output_directory = input("Please provide the output directory: (default ~/Downloads)")

    if url == "":
        print("No video or playlist URL was provided!")
        sys.exit(2)

    if "playlist" in url:
        playlist = Playlist(url)
        print("Playlist URL provided. Videos in playlist: ", len(playlist.video_urls))
        for video_url in playlist.video_urls:
            download(video_url, output_directory)
    else:
        download(url, output_directory)

if __name__ == "__main__":
    main(sys.argv[1:])
