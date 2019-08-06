import random
x = input("enter a word: ")
characters = list(x)
random.shuffle(characters)
print("".join(characters))


