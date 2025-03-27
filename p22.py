import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip

# Set the download folder
DOWNLOAD_FOLDER = r'C:\Users\Asus\OneDrive\Desktop\Code\CapStone\prac3\youtube_downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Function to download video/audio
def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Input Error", "Please enter a valid YouTube URL.")
        return
    
    quality = quality_var.get()
    file_format = format_var.get()

    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'writethumbnail': True,  # Preserve thumbnail
        'writeinfojson': True,  # Preserve metadata
        'quiet': True,  # Suppress console output
    }
    
    # Automatically select best available format
    if quality == "Best Video":
        ydl_opts['format'] = f"bv*+ba/b"  # Best video + best audio, fallback to best single format
    elif quality == "Worst Video":
        ydl_opts['format'] = f"wv*+ba/w"  # Worst video + best audio, fallback to worst single format
    elif quality == "Best Audio":
        ydl_opts['format'] = 'bestaudio'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': file_format,
            'preferredquality': '192'
        }]
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Download completed!\nCheck: {os.path.abspath(DOWNLOAD_FOLDER)}")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {str(e)}")

# Function to paste clipboard content
def paste_from_clipboard():
    url_entry.delete(0, tk.END)
    url_entry.insert(0, pyperclip.paste())

# Tkinter UI Setup
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x350")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Paste from Clipboard", command=paste_from_clipboard).pack(pady=5)

# Quality Selection
tk.Label(root, text="Select Quality:").pack(pady=5)
quality_var = tk.StringVar(value="Best Video")
quality_menu = ttk.Combobox(root, textvariable=quality_var, values=["Best Video", "Worst Video", "Best Audio"])
quality_menu.pack(pady=5)

# Format Selection
tk.Label(root, text="Select Format:").pack(pady=5)
format_var = tk.StringVar(value="mp4")
format_menu = ttk.Combobox(root, textvariable=format_var, values=["mp4", "mp3"])  # Removed "webm"
format_menu.pack(pady=5)

# Buttons
tk.Button(root, text="Download", command=download_video).pack(pady=10)

root.mainloop()
