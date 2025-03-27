import yt_dlp

def download_audio(url):
    try:
        # Set options for downloading only audio
        ydl_opts = {
            'format': 'bestaudio/best',  # Choose the best audio format
            'extractaudio': True,        # Extract audio only
            'audioquality': 1,           # Highest audio quality
            'outtmpl': '%(title)s.%(ext)s',  # Output filename format
            'postprocessors': [{         # Post-processing options to convert to mp3
                'key': 'FFmpegAudio',
                'preferredcodec': 'mp',
                'preferredquality': '192',
            }],
        }

        # Use yt-dlp to download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download Complete!")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
url = input("Enter YouTube URL: ")
download_audio(url)
