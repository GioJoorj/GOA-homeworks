month=int(input("enter month number"))

if month >= 1 and month <= 2 or month == 12: 
    print("winter")
elif month >= 3 and month <= 5: 
    print("spring")
elif month >= 6 and month <= 8:
    print("summer")
elif month >= 9 and month <= 11: 
    print("autumn")
else:
    print("wrong month number")