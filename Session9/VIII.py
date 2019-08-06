while True:
    high = [46, 77, 98,34,58]
    n = int(input("player's high score: "))
    high.append(n)
    high.sort( reverse = True)
    for i, item in enumerate(high):
        print(i+1 ,".", item)
