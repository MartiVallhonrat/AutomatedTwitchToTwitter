import asyncio
from delete_content import delete_contents_in_directory
from download_twitch_clips import download_top_5_clips
from twitter_bot import updateclips

# Set your channel list with the twtich IDs of the channels you want to post tweets
channel_list = []

async def ___main___(channel_list):

    for channel in channel_list:
        await download_top_5_clips(channel)
    
    await updateclips()
    
    delete_contents_in_directory("videos")

    print("Cycle ended!")




asyncio.run(___main___(channel_list))