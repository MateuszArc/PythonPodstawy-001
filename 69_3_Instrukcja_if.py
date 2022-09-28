age = 27

if age >= 18:
    print("You are adult you can buy alcohol")
else:
    print("You are too young to buy alcohol")

isDrunk = True

if age >= 18 and not isDrunk:
    print("You are adult you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

isEstrictedArea = False

if age >= 18 and not isDrunk and not isEstrictedArea:
    print("You are adult you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")