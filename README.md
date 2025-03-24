# YouTube Video Downloader
# Working in 2025
This is a simple **YouTube Video Downloader** application built using **Python, yt-dlp, and Tkinter**. It allows users to download YouTube videos in the best available format and save them to a specified folder.

---

## Features
- Simple and easy-to-use **Graphical User Interface (GUI)**.
- Downloads YouTube videos in the **best available quality**.
- Saves downloaded videos to a specified folder.
- Displays **download progress**.
- **Error handling** for invalid URLs and other issues.

---

## Requirements
### **1. Install Python**
Ensure you have Python installed (Python 3.x is recommended). You can download it from [python.org](https://www.python.org/downloads/).

### **2. Install Dependencies**
Before running the script, install the required Python packages using:
```sh
pip install yt-dlp tkinter
```

---

## How to Run the Application
1. **Clone or download** this repository.
   ```sh
   git clone https://github.com/UdayBhoyar/Youtube-Video-Downloader.git
   cd Youtube-Video-Downloader
   ```

2. **Run the script**
   ```sh
   python main.py
   ```

3. **Enter the YouTube video URL** in the input box and click the **Download Video** button.

4. The video will be downloaded to the following directory:
   ```sh
   C:\Users\Asus\OneDrive\Desktop\Code\CapStone\prac3\youtube_downloads
   ```
   *(Ensure this folder exists or will be created automatically.)*

5. Once the download is complete, a success message will be displayed.

---

## Code Explanation
The application consists of the following components:
- **Tkinter GUI** for user interaction.
- **yt-dlp library** to handle YouTube video downloading.
- **A progress update function** to display the current download status.

### **Main Functions**
1. `download_video()` – Retrieves the URL, validates it, sets the download path, and downloads the video.
2. `on_progress(d)` – Updates the UI with the download progress.
3. **Tkinter UI elements** – Creates labels, entry fields, buttons, and progress messages.

---

## Possible Errors & Fixes
| Error | Solution |
|--------|------------|
| `ModuleNotFoundError: No module named 'yt_dlp'` | Run `pip install yt-dlp` |
| `PermissionError: [Errno 13] Permission denied` | Ensure you have write permission for the target folder |
| `ERROR: Unsupported URL` | Check if the YouTube link is correct |

---

## Future Enhancements
- Add an option to **choose video quality** (e.g., 1080p, 720p, audio-only).
- Include a **download progress bar** instead of just a label.
- Support **multiple downloads simultaneously**.
- Allow users to **change the download folder** dynamically.

---

## License
This project is open-source and available under the **MIT License**.

---

## Author
**Uday Bhoyar**  
GitHub: [Uday Bhoyar]([https://github.com/aceofwings](https://github.com/UdayBhoyar))  
