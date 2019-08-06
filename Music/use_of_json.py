from __future__ import unicode_literals
import youtube_dl
import json

options = {


'outtmpl': '%(title)s.%(ext)s', # lấy tên file đown về là ten của video

 	'postprocessors': [{

     'key': 'FFmpegExtractAudio', # Tách lấy audio

     'preferredcodec': 'mp3', # Format ưu tiên là mp3

     'preferredquality': '192', # Chất lượng bitrate

}],

}
ydl = youtube_dl.YoutubeDL(options)
searchResult1 = ydl.extract_info('https://youtu.be/1rfSHisyHdc',download = False)
searchResult2 = ydl.extract_info('https://www.youtube.com/watch?v=Wv2rLZmbPMA', download=False)
listInfos = [searchResult1, searchResult2]
#(ben tren) tao list(array) cho cai dong thong tin bay vao
with open("data.json", "w") as dataList:
    json.dump(listInfos, dataList)
#(ben tren) nem cai dong thong tin vao cai "data.json" va "w" la viet cai thong tin vao data.json
with open("data.json") as dataGet:
    listDataGet = json.load(dataGet) #phai tao ra mot cai bien moi de cho cai thong tin vao de doc
#(ben tren) day la doc ra cai thong tin luu vao roi
#neu muon doc duoc cai dong shit o trong data.json, co mot cai trang web giup
while True:
    n = int(input('input "10" if u want to continue: '))
    if n == 10:
        m = input("input the object you want to find: ")
        print(listDataGet[1][m])
    else:
        break
#print title:
for a in range(len(listDataGet)):
    print(listDataGet[a]['title'])


# listData = [searchResult1, searchResult2]

