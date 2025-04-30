import os
import random
import schedule
import time
from instagrapi import Client

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
VIDEO_FOLDER = "videos/"
PIC_FOLDER = "pics/"

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

        pics = [f for f in os.listdir(PIC_FOLDER) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if pics:
            pic_path = os.path.join(PIC_FOLDER, random.choice(pics))
            cl.photo_upload_to_story(pic_path)
            print(f"Uploaded image: {pic_path}")
        else:
            print("No images found in the 'pics' folder.")

    except Exception as e:
        print(f"Error: {e}")

schedule.every().day.at("02:17").do(post_story)

print("Script running... Posting stories daily 10:17 PM.")
while True:
    schedule.run_pending()
    time.sleep(60)
