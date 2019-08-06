lit1 = ['ST','BD','BTL','CG','DD','HBT']
lit2 = [150300,247100,333300,266800,420900,318000]
lit3 = [11743,9224,4335,1204,996,1009]
lit4 = []
#for x in range(len(lit1)):
#    n = lit2[x]/lit3[x]
#    lit4.append(n)
#print(lit4)

total = 0
for x in range(len(lit1)):
    n = lit2[x]/lit3[x]
    total += n 
aver = total / (len(lit1)+1)
print(aver)



