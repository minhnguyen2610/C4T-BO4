Kho = {
    "HP":"600",
    "DELL":"650",
    "MACBOOK":"12000",
    "ASUS":"400",
    "ACER":"350",
    "TOSHIBA":"600",
    "FUJITSU":"900",
    "ALIENWARE":"1000"
}
m = int(input("pls enter the amount u want to buy: "))
n = input("pls enter the brand u want to buy from: ")
y = int(Kho[n])
x = y*m
print("The total price is: ", x)