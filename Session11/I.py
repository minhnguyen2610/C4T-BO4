Kho = {
    "HP":"20",
    "Dell":"12",
    "MacBook":"20",
    "ASUS":"30",
    "Toshiba":"10",
}
for k,v in Kho.items():
    print(k,":",v)
n = input("pls input the company you want to search for: ")
m = Kho[n]
print(m)