import os
import subprocess
from yt_dlp import YoutubeDL


BASE_DIR = r"D:\sangam\Sangam-Documents\Course Info\Ask_from_Course_AI"
OUTPUT_FOLDER = os.path.join(BASE_DIR, "data")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, check=True)
        print("✅ FFmpeg is installed and available.\n")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ FFmpeg is not installed or not found in PATH.\n"
              "Please install FFmpeg or ensure it’s added to your system PATH.")
        return False


def download_playlist_as_mp3(playlist_url):
    if not check_ffmpeg():
        return

    print(f"🎵 Starting download from playlist:\n{playlist_url}\n")
    print(f"All MP3s will be saved to:\n{OUTPUT_FOLDER}\n")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(OUTPUT_FOLDER, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,
        'addmetadata': True,
        'noplaylist': False,
        'progress_hooks': [lambda d: print_progress(d)],
        'quiet': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print("\n✅ All downloads completed successfully!")


def print_progress(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '')
        eta = d.get('_eta_str', '')
        print(f"⬇️  Downloading: {d.get('filename', '')}\n    {percent} at {speed} | ETA {eta}", end='\r')
    elif d['status'] == 'finished':
        print(f"\n🎧 Converted to MP3: {d.get('filename', '')}\n")


if __name__ == "__main__":
    playlist_url = input("🔗 Enter YouTube playlist URL: ").strip()
    if playlist_url:
        download_playlist_as_mp3(playlist_url)
    else:
        print("⚠️ No playlist URL provided. Exiting...")
