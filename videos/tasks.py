import os
from celery import shared_task
from django.core.files import File
import yt_dlp
from videos.models import Video, UserModel

@shared_task
def download_videos_task(vids_full_info: list, download_path: str):
    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'format': 'best',
        'progress_with_newline': True,
        'limit_rate': None,
        'geo_bypass': True,
        'noplaylist': True,
        'verbose': True,
        'concurrent_fragments': 50,
        'retries': 10,
        'fragment_retries': 10,
        'merge_output_format': 'mp4',
        'external_downloader': 'aria2c',
        'external_downloader_args': [
            '-x', '4',
            '-s', '32',
            '-k', '1M',
            '--min-split-size=1M',
            '--max-connection-per-server=16',
            '--enable-http-pipelining=true',
            '--auto-file-renaming=false',
        ],
    }

    print(f"[*] Starting download of {len(vids_full_info)} videos...")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for vid in vids_full_info:
            url = vid['Link']
            title = vid['Title']
            print(f"[*] Downloading: {url}")
            try:
                ydl.download([url])
                local_file_path = os.path.join(download_path, f"{title}.mp4")

                # Save to Django model
                with open(local_file_path, "rb") as f:
                    video = Video(
                        title=title,
                        uploader=UserModel.objects.filter(username='admin').first(),
                    )
                    video.video_file.save(os.path.basename(local_file_path), File(f), save=True)

                # Remove local file after saving to media
                if os.path.exists(local_file_path):
                    os.remove(local_file_path)
                    print(f"[+] Deleted local file: {local_file_path}")

            except Exception as e:
                print(f"[!] Failed to download {url}: {e}")