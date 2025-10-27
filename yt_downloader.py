#  uv add yt-dlp
#  uv add ruff
from yt_dlp import YoutubeDL

URLS = [""]

with YoutubeDL() as ydl:
    ydl.download(URLS)

print("yt_downloader Done!")
