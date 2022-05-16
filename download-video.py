# pip install pytube


# importing YouTube from pytube module
from pytube import YouTube

# assigning video link to a variable
video_link = "https://www.youtube.com/watch?v=MDqxBGL738U"
# passing that link variable to YouTube function
video = YouTube(video_link)

# download video
video.streams.filter(res='720p').first().download('C:\\videos')
