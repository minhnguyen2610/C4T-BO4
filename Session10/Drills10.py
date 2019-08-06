print("How many turtle u can create in a painting? ")
TTTc = {
    "1":"Two songs",
    "2":"28 songs",
    "3":"104",
    "4":"Who knows",
}
n = 0
m = 0
a = 100
for k,v in TTTc.items():
    print(k,"=",v)

while True:
    x = int(input("what is your answer? "))
    if x == 4:
        print("u r correct")
        n += 1
        break
    else:
        print("u r wrong")
        m += 1

print("How many songs of Unvle Ho have been created? ")
TTTc = {
    "1":"Two songs",
    "2":"28 songs",
    "3":"104",
    "4":"Who knows",
}

for k,v in TTTc.items():
    print(k,"=",v)

while True:
    x = int(input("what is your answer? "))
    if x == 4:
        print("u r correct")
        n += 1
        break
    else:
        print("u r wrong")
        m += 1
if m == 0:
    f = a
else:
    f = n/m
print("Numbers of correct answers: ",n)
print("Percantage of correct answers: ", f)