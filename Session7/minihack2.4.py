from turtle import *

n = int(input("nhap so canh cua hinh da giac vao day: "))
y = 180*(n-2)/n

for i in range(n):
    forward(30)
    left(180-y)

mainloop()