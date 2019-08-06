items = ['blue','red','green']
print("our color list: ")
print(*items, sep = ',')
x = input("pls enter a new color: ")
items.append(x)
print("Our new color list: ")
print(*items, sep = ',')

