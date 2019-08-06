Gia = {
    "HP":"600",
    "DELL":"650",
    "MACBOOK":"12000",
    "ASUS":"400",
    "ACER":"350",
    "TOSHIBA":"600",
    "FUJITSU":"900",
    "ALIENWARE":"1000"
}
Kho = {
    "HP":"20",
    "Dell":"50",
    "MacBook":"12",
    "ASUS":"30",
    "Acer":"10",
    "Toshiba":"10",
    "Fujitsu":"15",
    "Alienware":"5",
}

for v in Kho.values():
    for a in Gia.values():
        m = int(a)
    x = int(v)*m
    print(x)
