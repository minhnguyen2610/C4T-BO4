from __future__ import unicode_literals
from youtube_dl import YoutubeDL
import youtube_dl
import json
import pyglet

lol = []

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
            dataGet = json.load(outData)

        m = input('please enter the name of the music video that you want to download: ')
        options1 = {
            

        'outtmpl': '%(id)s', # lấy tên file đown về là id của video

            'postprocessors': [{

            'key': 'FFmpegExtractAudio', # Tách lấy audio

            'preferredcodec': 'mp3', # Format ưu tiên là mp3

            'preferredquality': '192', # Chất lượng bitrate


        }]}

        options = {
            'default_search': 'ytsearch5'
        }

        ydl = YoutubeDL(options)
        ydl_download = YoutubeDL(options1)
        search_result = ydl.extract_info(m, False)
        for i in range(len(search_result["entries"])):
            print(i + 1, "-", search_result["entries"][i]['id'])
        
        chooseMusics = int(input("Choose the song you want to download : ")) - 1
        musicGet = ydl_download.extract_info(search_result['entries'][chooseMusics]['webpage_url'], True)
        dataGet.append(musicGet)

        with open("data.json", "w") as dumpData:
            json.dump(dataGet, dumpData)
        while True:
            q = int(input("pls enter the number of the option that you choose: "))
            if q == 1:
                for i in range(len(search_result2["entries"])):
                    print(i + 1, "-", search_result["entries"][i]['id'])
            if q == 2:
                for i in range(len(search_result["entries"])):
                    print(i + 1, "-", search_result["entries"][i]['id'])
                    print("-", search_result["entries"][i]['uploader'])
                    print("-", search_result["entries"][i]['duration'],"in second")
            
            if q == 3:
                with open("data.json") as outData:
                    dataGet = json.load(outData)

                while True:
                    player = pyglet.media.Player()
                    for i in range(len(search_result["entries"])):
                        print(i + 1, "-", search_result["entries"][i]['id'])
                    j = int(input("pls input the song you want to play: "))
                    jj = search_result["entries"][j-1]['id'] + ".mp3"

                    music = pyglet.resource.media('music.mp3')
                    music.play()
                    print(player.time())
                    pyglet.app.run()
                    s = input("enter 1 to stop, 2 to continue, 3 to escape: ")
                    if s == 1:
                        player.pause()
                    elif s == 2:
                        music.play()
                    else:
                        break


            if q == 1:
                print(dataGet)
            if q == 2:
                for i in range(len(search_result["entries"])):
                    print(i + 1, "-", search_result["entries"][i]['id'])
                    print("-", search_result["entries"][i]['uploader'])
                    print("-", search_result["entries"][i]['duration'],"in second")
    if n == 5:
        break