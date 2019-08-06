
#items = ['1','4','34','67','77']
#print(*items, sep=', ')
#x = input("pls enter a correct number: ")
#if x in items:
#    print("found in our list")
#else:
#    print("not found in our list ")

#numbers = [1,3,11,24,66]
#x = sum(numbers)
#print("sum of the sequence is: ")
#print(x)

#numbers = [1,3,11,24,66]
#totals = 0
#for x in range(len(numbers)):
#    totals += numbers[x]
#print(totals)


lit = []
n = int(input("pls input the number of item you will input: "))
for x in range(n):
    ele = int(input("pls input the numbers here: "))
    lit.append(ele)
print(lit)
total = 0
for x in range(n):
    total += lit[x]
print(total)