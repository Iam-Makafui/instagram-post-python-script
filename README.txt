**Instagram Story Auto-Post Script - README**

**1. Requirements**
Before running the script, make sure you have:
- **Python 3.x** installed
- The required Python libraries installed (see step 2)
- A folder with videos ready for posting
- Instagram login credentials

---

**2. Install Dependencies**
Open a terminal or command prompt and run:
```bash


pip install moviepy  
```
This installs the necessary Python packages:
- `instagrapi`: For interacting with Instagram
- `schedule`: For running the script automatically every day

---

**3. Prepare the Video Folder**
- Create a folder named **videos/** in the same directory as the script.
- Place all the videos you want to be randomly posted inside this folder.
- Supported formats: **.mp4, .mov**

---

**4. Script Configuration**
- Open `auto_post.py`
- Replace `your_username` and `your_password` with your actual Instagram credentials:
```python
USERNAME = "your_username"
PASSWORD = "your_password"
```
- Set the time you want the script to post the story (default is **8 AM**)

---

**5. Running the Script**
To start the script, run:
```bash
python auto_post.py
```
This will:
1. Log into Instagram.
2. Select a random video from the **videos/** folder.
3. Post it as an Instagram Story.
4. Repeat this process daily at the scheduled time.

---

6. Running in the Background
To keep the script running after closing the terminal:
- **On Windows**: Use **Task Scheduler** to run the script on startup.
- **On Mac/Linux**: Use:
```bash
nohup python auto_post.py &
```
This will run it in the background.

---

7. Troubleshooting
Login Issues: If login fails, Instagram may require manual verification.
2FA (Two-Factor Authentication) Enabled? Use an **app password** instead of your regular password.
No Videos Found? Make sure the **videos/** folder has videos and that they are in **.mp4** or **.mov** format.
Change Post Time?* Modify this line in the script:

```python
schedule.every().day.at("08:00").do(post_story)
```

Replace `"08:00"` with your preferred time (24-hour format).
---

**8. Notes**
- **Use a test Instagram account first** to avoid bans.
- The script must be running continuously to work daily.
- You can modify the script to post at different times or add captions if needed.

---

**9. Contact & Support**
If you need modifications or have issues, feel free to reach out to me!

