
#total = 0
#lit = [1,21,33,44,55,66]
#print("all even number(s) is(are): ")
#for x in range(len(lit)):
#    if lit[x]%2==0:
#        print(lit[x])
#    else:
#
#         pass

lit = []
n = int(input("pls input the number of item you will input: "))
for x in range(n):
    ele = int(input("pls input the numbers here: "))
    lit.append(ele)
print(lit)
print("all even number(s) is(are): ")
for i in range(len(lit)):
    if lit[i]%2==0:
        print(lit[i])
    else:
        pass