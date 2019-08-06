import random
a = float(random.randint(0,1))

skill1 = {
    "Name":"Tackle",
    "Minimum level":"1",
    "Damage":"5",
    "Hit rate":"0.3",
}
skill2 = {
    "Name":"Quick attack",
    "Minimum level":"2",
    "Damage":"3",
    "Hit rate":"0.5",
}
skill3 = {
    "Name":"Strong kick",
    "Minimum level":"4",
    "Damage":"9",
    "Hit rate":"0.2",
}

lis = [skill1,skill2,skill3]
print("Level 3")
print("List of skill can be used: ")
for i, item in enumerate(lis):
    print(i+1 ,".", item["Name"])
n = input("pls enter the name of skill: ")
for k in range(len(lis)):
    if n in lis[k].values():
        m = int(lis[k]["Minimum level"])
        x = int(lis[k]["Damage"])
        b = float(lis[k]["Hit rate"])
        if a < b:
            if m < 3:
                print("Damage inflicted: ", x)
            else:
                print("Your level is too low")
        else:
            print("fail to attack")