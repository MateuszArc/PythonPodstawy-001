import random 

min = 1
max = 6

dice = random.randint(min, max)

if dice == 1:
    print("o")
    print(" ")
    print(" ")
elif dice == 2:
    print("   o")
    print(" ")
    print("o ")
elif dice == 3:
    print("   o")
    print(" o")
    print("o ")
elif dice == 4:
    print("o o")
    print("   ")
    print("o o")
elif dice == 5:
    print("   o o ")
    print("    o  ")
    print("   o o ")             
else:
    print("   o o ")
    print("   o o ")     
    print("   o o ") 

dices = []
for s in range(5):
    dices2 = random.randint(min, max)
    dices.append(dices2)

dices.sort()
print(dices)