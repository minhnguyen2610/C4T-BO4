while True:
    x = input("enter your password, please have more than 8 words and have number in it.")
    n = len(x)
   
    if n > 7:
        if x.isalpha():
            print("you suck at life")
        elif x.isdigit():
            print("go back to kindergarden")
        else:
            print("ok success")
            break
    else:
        print("no you dont know how to count")
        
