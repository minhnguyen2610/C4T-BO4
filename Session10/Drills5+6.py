p1 = {
    "name":"Huy",
    "Role":"Waiter",
    "Hour":"12",
    "Salary per hour($)":"0.8"
}
p2 = {
    "name":"Tung",
    "Role":"Cook",
    "Hour":"24",
    "Salary per hour($)":"1.5",
}
p3 = {
    "name":"Mr.Duc",
    "Role":"Manager",
    "Hour":"2",
    "Salary per hour($)":"2",
}


People = [p1,p2,p3]

p4 = {
    "name":"Don",
    "Role":"helper",
    "Hour":"12",
    "Salary per hour($)":"0.9",
}
p5 = {
    "name":"H.Duc",
    "Role":"Waiter",
    "Hour":"14",
    "Salary per hour($)":"0.7",
}
p6 = {
    "name":"Huyen",
    "Role":"Waitress",
    "Hour":"14",
    "Salary per hour($)":"1.1",
}
People.append(p4)
People.append(p5)
#People.pop(len(People))
#People[0] = p6
#for i, item in enumerate(People):
#    print(i+1 ,".", item)

#print(People)
#print(People[2])

x=0
for i in range(len(People)):
    m = int(People[i]["Hour"])
    n = float(People[i]["Salary per hour($)"])
    y = m*n
    x += y  
print(x)

