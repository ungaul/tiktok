import requests
import os

# API Configuration
API_ENDPOINT = 'https://open-api.tiktok.com/video/upload/'
CLIENT_KEY = os.getenv('CLIENT_KEY')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
VIDEO_FILENAME = os.getenv('VIDEO_FILENAME', 'Weewee Cat.mp4')

def post_video_to_tiktok():
    # Check if the video file exists
    if not os.path.isfile(VIDEO_FILENAME):
        print(f'The file {VIDEO_FILENAME} does not exist.')
        return

    try:
        with open(VIDEO_FILENAME, 'rb') as video_file:
            files = {'video': video_file}
            data = {
                'client_key': CLIENT_KEY,
                'client_secret': CLIENT_SECRET,
            }

            print('Attempting to upload the video to TikTok...')
            response = requests.post(API_ENDPOINT, files=files, data=data)

            if response.status_code == 200:
                print('Video uploaded successfully!')
            else:
                print(f'Error uploading the video (status code {response.status_code}): {response.text}')

    except Exception as e:
        print('An exception occurred during video upload:', e)

if __name__ == '__main__':
    post_video_to_tiktok()