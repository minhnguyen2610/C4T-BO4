from __future__ import unicode_literals
import youtube_dl
options = {


'outtmpl': '%(title)s.%(ext)s', # lấy tên file đown về là ten của video

 	'postprocessors': [{

     'key': 'FFmpegExtractAudio', # Tách lấy audio

     'preferredcodec': 'mp3', # Format ưu tiên là mp3

     'preferredquality': '192', # Chất lượng bitrate

}],

}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download('https://youtu.be/1rfSHisyHdc')
