from pytube import YouTube  # Used to get data from YouTube
from sys import argv        # Used to take input commands when running python file

# YouTube connection
link = argv[1] # Note: argv[0] is going to be the file you are running 
yt = YouTube(link)

# Test Connection
print("Title: ", yt.title)
print("Views: ", yt.views)

# Set video resolution
download = yt.streams.get_highest_resolution()

# Download YouTube video
download.download('./Users/Qaasim/Downloads/Videos/Youtube_downloads')
