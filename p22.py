import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox

def download_video():
    url = url_entry.get()  # Get URL from the entry widget

    if not url:
        messagebox.showerror("Input Error", "Please enter a valid YouTube URL.")
        return

    # Set the path to save videos in C:/Users/Student
    download_folder = r'C:\Users\Asus\OneDrive\Desktop\Code\CapStone\prac3\youtube_downloads'  # Make sure this folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)  # Create the folder if it doesn't exist

    ydl_opts = {
        'format': 'best',  # Choose the best available format
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save in the 'Student' folder with the title as filename
        'progress_hooks': [on_progress]  # Function to handle progress updates
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", f"Download completed successfully!\nFile downloaded to: {os.path.abspath(download_folder)}")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {str(e)}")

def on_progress(d):
    if d['status'] == 'downloading':
        progress_label.config(text=f"Downloading: {d['filename']} - {d['_percent_str']}")

# Set up the Tkinter window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL Entry
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Progress Label
progress_label = tk.Label(root, text="Progress: None", font=("Arial", 12))
progress_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
