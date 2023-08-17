import os
import tweepy


# Set up the request headers with your Twitter API Keys & Tokens
CONSUMER_KEY = "XXXX"
CONSUMER_SECRET = "XXXX"

BEARER_TOKEN = "XXXX"
ACCESS_TOKEN = "XXXX"
ACCESS_TOKEN_SECRET = "XXXX"

client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)

api = tweepy.API(auth, wait_on_rate_limit=True)


def clean_title(input_string):
    index = input_string.find(".mp4")
    if index != -1:
        return "🎥 🔴  " + input_string[:index]
    else:
        return input_string

async def updateclips():

    # Set the file path for the videos
    path = "videos"
    files = os.listdir(path)
    
    for file in files:
        try:
            # Clean and set the title pretty
            message = clean_title(file)

            # Set the file path for the video
            file_path = f"videos/{file}"
            
            # Upload the video directly using media_upload
            media_info = api.media_upload(filename=file_path, media_category='tweet_video')
            
            # Create the tweet with the uploaded media
            client.create_tweet(text=message, media_ids=[media_info.media_id])
            print(f"Tweeted! {file}")
            
        except Exception as e:
            print(f"An error occurred while processing {file}: {e}")
