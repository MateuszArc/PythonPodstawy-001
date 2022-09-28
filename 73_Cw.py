likes = 500
shares = 100

if likes < 500 and shares <= 100:
    print("There is not enought likes")
else:
    if likes >= 500 and shares < 100:
            print("There is not enought shares")
    else:
        print("The prices fall about 10%")

if likes < 500:
    print("There is not enought likes")
elif shares < 100:
    print("There is not enought shares")
else:
    print("The prices fall about 10%")

##########################################

isPizzaOrdered = True 
isBigDrincOrdered = True
isWeekend = False

if isPizzaOrdered == True and isBigDrincOrdered == True and isWeekend == True:
    print("the promotion applies only to working days")
else:
    if isPizzaOrdered == True and isBigDrincOrdered == False and isWeekend == True:
        print("the promotion also applies to the drink")
    else:
        if isPizzaOrdered == False and isBigDrincOrdered == True and isWeekend == True:
            print("the promotion also applies to the pizza")
        else:
            print("congratulations you get a voucher for a free burger")

if isWeekend :
    print("the promotion applies only to working days")
elif not isPizzaOrdered:
    print("the promotion also applies to the pizza")
elif not isBigDrincOrdered:
    print("the promotion also applies to the drink")
else:
    print("congratulations you get a voucher for a free burger")