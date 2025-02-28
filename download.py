from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import yt_dlp
import tempfile
import urllib.parse

app = FastAPI()

# Allow CORS so that the frontend can connect to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a Pydantic model to validate the request payload
class VideoDownloadRequest(BaseModel):
    link: str

@app.post("/download/")
async def download_youtube_video(request: VideoDownloadRequest):
    url = request.link
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required")

    # URL decode the provided URL
    decoded_url = urllib.parse.unquote(url)

    # Temporary directory to save the downloaded video
    temp_dir = tempfile.mkdtemp()
    video_filename = None  # Initialize video_filename to prevent UnboundLocalError

    try:
        # yt-dlp options to download the best quality video
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(decoded_url, download=True)

            # Construct the downloaded file path
            video_filename = ydl.prepare_filename(result)

            # Check if the file exists after download
            if not os.path.exists(video_filename):
                raise HTTPException(status_code=500, detail="Video download failed")

        # Return the video file as a response
        return FileResponse(video_filename, media_type='video/mp4', filename=os.path.basename(video_filename))

    except Exception as e:
        # Handle errors (e.g., invalid URL, failed download)
        raise HTTPException(status_code=400, detail=f"Failed to download video: {str(e)}")
    
    finally:
        # Clean up the temporary directory after the response is sent
        if video_filename is None or not os.path.exists(video_filename):
            if os.path.exists(temp_dir):
                for f in os.listdir(temp_dir):
                    os.remove(os.path.join(temp_dir, f))
                os.rmdir(temp_dir)
