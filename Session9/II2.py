from turtle import *

forward(10)

items = ['yellow','blue', 'green', 'red', 'orange']
for i in range (0 , len(items)):
    color(items[i])

    forward(10)


mainloop()