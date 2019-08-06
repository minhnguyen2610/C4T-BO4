while True:
    items = ['apple','bannana','chicken','dinner']
    x = input("do you want to continue? Input \'1\' to continue: ")
    if x == "1" :
        print(items)
        print("choose one of these option: C, R, U or D")
        y = input("input here: ")
        if y == "C" :
            x1 = input("input what u like to create: ")
            items.append(x1)
        elif y == "R":
            for e in range(len(items)):
                print(items[e])
        elif y == "U":
            i2 = int(input("where do u want to create? (input 1 or 2 ,..)"))
            x2 = input("input what u like to create: ")
            items[i2-1] = x2
        elif y == "D":
            i3 = int(input("Where do u want to delete: "))
            items.remove(i3)
        else:
            break

    else: 
        break

