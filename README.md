# 🐱 TikTok Video Uploader

This project automates the process of uploading a video named 'Weewee Cat.mp4' to TikTok every day at 17:00 UTC using GitHub Actions and TikTok's API.

## 📂 Project Structure
- `.github/workflows/tiktok_video_upload.yml`: Defines the GitHub Action for running the script.
- `upload_script.py`: Python script for uploading the video.
- `Weewee Cat.mp4`: The video file to be uploaded.

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [repository-url]
   ```

2. **Add Secrets:**
   In your GitHub repository, navigate to **Settings > Secrets and variables > Actions** and add:
   - `CLIENT_KEY`: Your TikTok API client key.
   - `CLIENT_SECRET`: Your TikTok API client secret.

3. **Modify the video file:**
   Replace `Weewee Cat.mp4` with your desired video file, or modify the filename in the script.

4. **Run locally (optional):**
   ```bash
   python upload_script.py
   ```

## 🕒 Automation Schedule
The video upload is automated via GitHub Actions to run daily at 17:00 UTC. You can modify the schedule in the `cron` section of the workflow file.

## 🚀 Features
- Automatic video uploads to TikTok.
- Customizable video file and API configuration.
- GitHub Actions integration for scheduled execution.

## 🛠️ Dependencies
- Python 3.x
- Requests library (install with `pip install requests`)

## 📢 Note
Ensure that TikTok API access and permissions are correctly configured for successful video uploads.