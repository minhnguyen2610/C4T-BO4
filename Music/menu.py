from __future__ import unicode_literals
from youtube_dl import YoutubeDL
import youtube_dl
import json
import pyglet
import time

lol = 0

while True:
    menu = {
        '1':'Show all song',
        '2':'Show detail of a song',
        '3':'Play a song',
        '4':'Search and download a song',
        '5':'Exit'
    }
    for k,v in menu.items():
        print(k,".",v)
    n = int(input("pls enter the number of the option that you choose: "))

    if n == 4:
        with open("data.json") as outData:
            dataGet = json.load(outData) # tao ra, lay ra data tu data.json

        m = input('please enter the name of the music video that you want to download: ')
        options1 = {
            

        'outtmpl': '%(id)s', # lấy tên file đown về là id của video

            'postprocessors': [{

            'key': 'FFmpegExtractAudio', # Tách lấy audio

            'preferredcodec': 'mp3', # Format ưu tiên là mp3

            'preferredquality': '192', # Chất lượng bitrate


        }]}

        options = {
            'default_search': 'ytsearch5'#search lay 5 ket qua
        }

        ydl = YoutubeDL(options)
        ydl_download = YoutubeDL(options1)
        search_result = ydl.extract_info(m, False)# lay thong tin ra
        for i in range(len(search_result["entries"])):
            print(i + 1, "-", search_result["entries"][i]['id'])
        
        chooseMusics = int(input("Choose the song you want to download : ")) - 1
        musicGet = ydl_download.extract_info(search_result['entries'][chooseMusics]['webpage_url'], True)
        dataGet.append(musicGet)# this cai json neu tai cai moi ve thi de len cai cu, ta phai dung append de them vao chu ko phai xoa di

        with open("data.json", "w") as dumpData:
            json.dump(dataGet, dumpData)# Nem data vao lai dataGet
        
    if n == 1:
        with open("data.json") as out1Data:
            data1Get = json.load(out1Data)#Moi data ra de dung
        for i in range(len(data1Get)):#Day la list
            print(i + 1, "-", data1Get[i]['id'])
    if n == 2:
        with open("data.json") as out1Data:
            data1Get = json.load(out1Data)
        for i in range(len(data1Get)):
            print(i + 1, "-", data1Get[i]['id'])
            print("-", data1Get[i]['uploader'])
            print("-", data1Get[i]['duration'],"in second")
    
    if n == 3:
        with open("data.json") as out1Data:
            data1Get = json.load(out1Data)
        player = pyglet.media.Player()
        for i in range(len(data1Get)):
            print(i + 1, "-", data1Get[i]['id'])
        j = int(input("pls input the song you want to play: "))
        jj = data1Get[j-1]['id'] + ".mp3"
        music = pyglet.resource.media(jj)
        music.play()
        pyglet.app.exit()       
        pyglet.app.run()
        print(player.time())
        pyglet.app.exit()

    if n == 5:
        break



      



        
       
