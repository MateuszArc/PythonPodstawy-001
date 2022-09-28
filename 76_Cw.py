musclePain = False
fever = True
weakness = True
isMan = True

if musclePain == True and fever == True and weakness == True:
    print("suspicion of influenza")
else:
    print("The flu is unlikely")

if musclePain == True and fever == True and weakness == True:
    print("suspicion of influenza")
elif weakness == True and fever == False or musclePain == False:
    print("Just take a rest")
else:
    print("You may be cold.")

if musclePain == True and fever == True and weakness == True or isMan == True and musclePain == True or fever == True or weakness == True:
    print("suspicion of flu")
else:
    print("You may be cold.")

isCheckCompleted = True
print("CHECK IS COMPLETED"if isCheckCompleted else "CHECK NOT DONE YET!")