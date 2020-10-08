import os
import shutil
import subprocess
import youtube_dl

def audio(video_url, video_info):

	filename = f"{video_info['title']}.mp3" #sets the name as in the youtube page
	options = {
		'format' : 'bestaudio/best',
		'keepvideo' : False,
		'outtmpl' : filename,
		'postprocessors' : [{
			'key' : 'FFmpegExtractAudio',
			'preferredcodec' : 'mp3',
			'preferredquality' : '320',
		}]
	}

	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([video_info['webpage_url']])

	shutil.move(filename,'Specify your required path') #moving to the desire dictionary
	


if __name__ == '__main__':
	video_url = input("Please enter the video link : ") #enter the url that needs to be downloaded
	video_info = youtube_dl.YoutubeDL().extract_info(url=video_url,download=False) #extract the video data
	
	audio(video_url, video_info) #calling the function
