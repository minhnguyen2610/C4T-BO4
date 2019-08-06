skill1 = {
    "Name":"Tackle",
    "Minimum level":"1",
    "Damage":"5",
    "Hit rate":"0.3",
}
skill2 = {
    "Name":"Quick attack",
    "Minimum level":"2",
    "Damage":"3",
    "Hit rate":"0.5",
}
skill3 = {
    "Name":"Strong kick",
    "Minimum level":"4",
    "Damage":"9",
    "Hit rate":"0.2",
}
lis = [skill1,skill2,skill3]
for i, item in enumerate(lis):
    print(i+1 ,".", item["Name"])

