# Online-Video-Downloader

## 📌 About the Project
This **Online Video Downloader** is a web-based tool that allows users to download videos from various platforms. Built using **HTML, CSS, and JavaScript** for the frontend and **FastAPI (Python)** for the backend, it provides a simple and efficient way to fetch and download videos via a URL.

## 🚀 Features
✅ User-friendly interface for entering video URLs  
✅ FastAPI backend to process video downloads  
✅ Responsive design for mobile and desktop  
✅ Supports multiple video formats  
✅ Error handling for invalid URLs  

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **Video Processing:** yt-dlp (YouTube Downloader)  

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/online-video-downloader.git
   ```
2. Navigate to the project folder:
   ```bash
   cd online-video-downloader
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn yt-dlp
   ```
4. Run the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```
5. Open `index.html` in a browser to use the downloader.

## 📌 Usage
1. Enter the video URL in the input field.
2. Click the **Download** button.
3. The backend fetches and processes the video.
4. The download link is provided once the video is ready.

## 🤝 Contributing
Feel free to fork this repository, improve the code, and submit a pull request! 

📩 **Let's make video downloading easier!** 🚀
