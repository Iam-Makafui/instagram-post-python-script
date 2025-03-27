# import os
# import random
# import schedule
# import time
# from instagrapi import Client

# # Instagram login details
# # USERNAME = "zoejenin"  # Replace with your IG username
# # PASSWORD = "Code42fric@m@k@fui"  # Replace with your IG password
# USERNAME = os.getenv("IG_USERNAME")
# PASSWORD = os.getenv("IG_PASSWORD")

# # Folder where videos are stored
# VIDEO_FOLDER = "videos/"

# # Function to post a random video to IG Story
# def post_story():
#     try:
#         cl = Client()
#         cl.login(USERNAME, PASSWORD)
        
#         # Get a random video from the folder
#         videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.mov'))]
#         if not videos:
#             print("No videos found in the folder.")
#             return
        
#         video_path = os.path.join(VIDEO_FOLDER, random.choice(videos))
        
#         # Post to IG Story
#         cl.video_upload_to_story(video_path)
#         print(f"Uploaded {video_path} to IG Story!")
    
#     except Exception as e:
#         print(f"Error: {e}")

# # Schedule to run daily at 8 AM
# schedule.every().day.at("13:04").do(post_story)

# print("Script running... Posting stories daily at 8 AM.")
# while True:
#     schedule.run_pending()
#     time.sleep(60)
import os
import random
import schedule
import time
from instagrapi import Client

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
VIDEO_FOLDER = "videos/"

def post_story():
    try:
        cl = Client()
        cl.login(USERNAME, PASSWORD)
        
        videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.mov'))]
        if not videos:
            print("No videos found in the folder.")
            return

        video_path = os.path.join(VIDEO_FOLDER, random.choice(videos))
        cl.video_upload_to_story(video_path)
        print(f"Uploaded {video_path} to IG Story!")

    except Exception as e:
        print(f"Error: {e}")

schedule.every().day.at("02:13").do(post_story)

print("Script running... Posting stories daily 10:13 PM.")
while True:
    schedule.run_pending()
    time.sleep(60)