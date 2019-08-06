#items = ['blue','red','green']
#print("our color list: ")
#print(*items, sep = ',')
#i = int(input("enter position: "))
#print(items[i-1])

items = ['black','blue', 'green', 'red', 'orange']
for i, m in enumerate(items): 
    print(i+1,".", m)
x = input("items to delete: ")
y = int(x)
if x.isdigit():
    items.pop(y-1)
elif x.isalpha():
    items.remove(x)
else:
    print("no")
print("Our new list")
for n, m in enumerate(items): 
    print(n+1,".", m)

