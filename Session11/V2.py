Kho = {
    "HP":"20",
    "Dell":"50",
    "MacBook":"12",
    "ASUS":"30",
}
Kho["Toshiba"] = "10"
Kho["Dell"] = "60"
Kho["MacBook"] = "2"
Kho["Fujitsu"] = "15"
Kho["Alienware"] = "5"
print(Kho)
n = input("pls enter the branch u want to buy: ")
m = int(input("pls enter the amount u want to buy: "))
y = int(Kho[n])
x = y - m 
print("The remaining amount is: ", x)
