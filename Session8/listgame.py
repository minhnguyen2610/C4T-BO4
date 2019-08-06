import random
items = ['apple', 'bone','cinder','drone']
print(*items, sep = ',')
i = random.randint(0, 4)
characters = list(items[i])
random.shuffle(characters)
x = "".join(characters)
print("".join(characters))
y = input("day a mot tu duoc tron len, phien ban goc cua no la gi: ")
if items[i] == y:
    print("ok u r good")
else:
    print("u suck")