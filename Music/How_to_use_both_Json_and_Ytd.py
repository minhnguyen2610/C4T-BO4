from youtube_dl import YoutubeDL
import json

options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', False)
listInfos = search_result # a place for the info have been downloaded to stay

with open("data.json1", "w") as dataList:
    json.dump(listInfos, dataList) #put the data that u just download into data.json1

with open("data.json1") as dataGet:
    listDataGet = json.load(dataGet) #open data.json1 to do whatever you want
#extracting info out of the json.data
m = listDataGet[0]['entries']['webpage_url']
print(m)

