import random
while True:
    one = ["-","-","-","-"]
    two = ["-","-","-","-"]
    three  = ["-","-","-","-"]
    four = ["-","-","P","-"]
    print(*one, sep = " ")
    print(*two, sep = " ")
    print(*three, sep = " ")
    print(*four, sep = " ")
    n = int(input("please enter the row that you want to spawn in: "))
    p = int(input("pls enter the location you want to spawn in: "))
    if n == 1:
        n = one
    elif n == 2:
        n = two
    elif n == 3:
        n = three
    elif n == 4:
        n = four
    n[p] = "P"
    q = input("Your move: ")
    print(*one, sep = " ")
    print(*two, sep = " ")
    print(*three, sep = " ")
    print(*four, sep = " ")
x = random.randint(0, len(one)
n = random.randint(1, 5)

