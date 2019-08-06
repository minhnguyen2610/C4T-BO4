lit1 = ['ST','BD','BTL','CG','DD','HBT']
lit2 = [150300,247100,333300,266800,420900,318000]
n = max(lit2) 
m = min(lit2)

for x in range(len(lit2)):
    if lit2[x] == n:
        print("day la quan voi dan so lon nhat:") 
        print(lit1[x])
        print("voi dan so: ")
        print(lit2[x])
    else:
        pass
for x in range(len(lit2)):
    if lit2[x] == m:
        print("day la quan voi dan so nho nhat:") 
        print(lit1[x])
        print("voi dan so: ")
        print(lit2[x])
    else:
        pass
