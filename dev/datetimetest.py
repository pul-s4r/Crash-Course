import datetime

d1 = "17/06/1998"

d2 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
print(d2)
print("17/06/1998" == d2.strftime("%d/%m/%Y"))
print(d2.strftime("%d/%m/%Y"))
