from pytube import YouTube
from sys import argv

#link = argv[1]
yt = YouTube('https://www.youtube.com/watch?v=vEQ8CXFWLZU')

print("Title: ", yt.title)

#print("View: ", yt.views)

#yd = yt.streams

# ADD FOLDER HERE
#yd.download('/Users/Qaasim/Downloads/Videos/Youtube_downloads')
