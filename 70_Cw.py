Min_Likes = 500
Min_Shares = 100
num_Likes = 1300
num_Shares = 55

if num_Likes >= Min_Likes and num_Shares >= num_Likes:
    print("Prices drop 10%")
else:
    print("there are not enough likes and shares")

Min_Likes = 500
Min_Shares = 100
num_Likes = Min_Likes = 500
num_Shares = Min_Shares = 100

if Min_Likes <= 500 and Min_Shares <= 100:
    print("Prices drop 10%")
else:
    print("there are not enough likes and shares")


isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if isPizzaOrdered == True and isBigDrinkOrdered == True and isWeekend == False:
    print("You get a coupon for a free burger.")
else:
    print("Try to continue buying.")

discSize = 140
diskSizeUsed = 133 
fileSize = 10
remaining_Disk_Space = discSize - diskSizeUsed

if remaining_Disk_Space >= fileSize:
    print("File can be downloaded")
else:
    print('there is not enough disk space')

discSize = 150
diskSizeUsed = 133 
fileSize = 13
remaining_Disk_Space = discSize - diskSizeUsed

if remaining_Disk_Space >= fileSize:
    print("File can be downloaded")
else:
    print('there is not enough disk space')