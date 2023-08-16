import json
import os
import requests
from datetime import datetime, timedelta

# Set the minimum views required for the downlaod
min_views = 500

def download_video(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Video downloaded successfully. Saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the video: {e}")

def sanitize_filename(filename):
    return "".join(c for c in filename if c.isalnum() or c in "-_ ")

async def download_top_5_clips(channel_id):
    # Define the API endpoint URL and parameters (setted for the last 24h)
    endpoint = "https://api.twitch.tv/helix/clips"
    params = {"broadcaster_id": channel_id, "first": 5, "started_at": (datetime.utcnow() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')}

    # Set up the request headers with your Twitch API client ID
    headers = {
        "Client-ID": "XXXX",
        "Authorization": "XXXX",
    }

    # Make the API request
    response = requests.get(endpoint, params=params, headers=headers)

    # Parse the response JSON
    data = json.loads(response.text)

    # Create the videos directory if it doesn't exist
    if not os.path.exists("videos"):
        os.makedirs("videos")

    # Loop through the clips and download each one
    for clip in data["data"]:

        clip_views = clip["view_count"]

        if clip_views > min_views:
            clip_broadcaster = clip["broadcaster_name"]
            clip_thumbnail = clip['thumbnail_url']
            clip_title = clip["title"]
            # Remove invalid characters
            sanitized_title = sanitize_filename(clip_title)
            clip_filename = f"{sanitized_title} - {clip_broadcaster}.mp4"
            index = clip_thumbnail.find('-preview')
            clip_url = clip_thumbnail[:index] + '.mp4'
            save_path = "videos/" + clip_filename

            download_video(clip_url, save_path)