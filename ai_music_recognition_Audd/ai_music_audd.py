from pytube import YouTube
import os
import requests

def download_audio_direct(video_url, output_path):
    try:
        # Use the current working directory as the output path
        if not output_path:
            output_path = os.getcwd()

        # Use pytube to download the audio from the video
        yt = YouTube(video_url)
        audio_stream = yt.streams.get_audio_only()
        audio_file_path = audio_stream.download(output_path=output_path)
        
        # Rename the downloaded audio file to .mp3
        base, ext = os.path.splitext(audio_file_path)
        new_audio_file_path = base + '.mp3'
        os.rename(audio_file_path, new_audio_file_path)

        print(f"Audio file has been saved to: {new_audio_file_path}")
        return new_audio_file_path
        
    except Exception as e:
        print(f"An error occurred during the download process: {e}")
        return None

def upload_audio_and_get_data(file_path):
    try:
        # Prepare the data for the request
        data = {
            'return': 'apple_music,spotify',
            'api_token': 'test'  # Use your actual API token here
        }

        # Prepare the file to be uploaded
        files = {
            'file': open(file_path, 'rb')
        }

        # Send the POST request
        response = requests.post('https://api.audd.io/', data=data, files=files)
        print(response.text)
        
    except Exception as e:
        print(f"An error occurred during the upload process: {e}")
        
    finally:
        # Close the file
        files['file'].close()

# Example use
video_url = 'your YouTube video link here'  # Replace with the actual video link
output_path = ''  # Use the directory where the script is running as the output path
file_path = download_audio_direct(video_url, output_path)

if file_path:
    upload_audio_and_get_data(file_path)
