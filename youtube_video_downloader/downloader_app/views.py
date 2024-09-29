from django.shortcuts import render
import yt_dlp as youtube_dl

def youtube_downloader(request):
    error_message = ""
    success_message = ""
    
    if request.method == 'POST':
        # Get the link from the form input and strip any leading/trailing whitespace
        link = request.POST.get('link', '').strip() 
        if not link:
            error_message = "Please enter a valid YouTube URL."
        else:
            try:
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': '%(title)s.%(ext)s',  # Set the output filename to the video title
                }
                
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link]) # Download the video using the provided link

                success_message = "Video downloaded successfully!"
            except Exception as e:
                error_message = f"An unexpected error occurred: {str(e)}"
                
    # Render the template with any error or success messages
    return render(request, 'downloader_app/youtube_downloader.html', {
        'error_message': error_message,
        'success_message': success_message
    })
