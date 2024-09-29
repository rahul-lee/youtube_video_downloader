YouTube Video Downloader
This is a simple web application built using Django that allows users to download videos from YouTube by entering the video URL. The application leverages the powerful yt-dlp library to handle video downloads and supports various formats and quality options.

Features
User-friendly interface for entering YouTube video URLs.
Downloads videos in the best available quality.
Utilizes yt-dlp, a fork of youtube-dl, to handle video downloading.
Responsive design built with Bootstrap for better user experience.

Technologies Used
Python: Programming language for server-side logic.
Django: Web framework for building the application.
yt-dlp: Library for downloading videos from YouTube.
Bootstrap: Frontend framework for styling and responsive design.

Installation
To run this project locally, follow these steps:

Clone the repository:
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader

Create a virtual environment (optional but recommended): (for windows)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
pip install django
pip install yt-dlp
pip install requests 

Run the Django server:
python manage.py runserver

Usage
Enter a valid YouTube video URL in the input field.
Click the "Submit" button to start the download.
Once the download is complete, a success message will be displayed.

Thanks for visiting! 
