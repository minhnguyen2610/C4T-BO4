
while True:
    import random
    x = random.randint(0, 20)
    m = random.randint(-20,20)
    y = random.randint(0,100)
    z = 1
    if y < 50:
        print(x)
        print("+")
        print(m)
        n = int(input("What is your answer? "))
        if n == x + m:
            print("nice correct")
        else:
            break
            
  
    elif 50 < y < 100:
        print(x)
        print("-")
        print(m)
        n = int(input("What is your answer? "))
        if n == x - m:
            print("nice correct")
        else:
            break
           
  