# from datetime import datetime

# now = datetime.now()

# while True:
#     hour1 = now.hour
#     print(now)
#     print(hour1)

from datetime import datetime
import pyglet


mainland = input("please enter time in form of hour:minute for your wake up call ")

while True:
    currentTime = datetime.now().strftime('%H:%M')
    if mainland == currentTime:

        music = pyglet.resource.media('Cricket_Sound_Effect.mp3')
        music.play()

        pyglet.app.run()
    else:
        print("")

