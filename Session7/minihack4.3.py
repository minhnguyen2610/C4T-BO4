x = input("pls enter your email: ")
while True:
    m = input("enter your password, please have more than 8 words and have number in it.")
    n = len(m)
   
    if n > 7:
        if m.isalpha():
            print("you suck at life")
        elif m.isdigit():
            print("go back to kindergarden")
        else:
            print("ok success")
            break
    else:
        print("no you dont know how to count")
while True:
    z = input("pls enter your password: ")
    zm = input("pls re-enter your password: ")
    if z != zm:
        print("do it again:")
    else:
        break
