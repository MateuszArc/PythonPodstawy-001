age = 29
isDrunk = True
isEstrictedArea = False

if age < 18 and not isDrunk:
    print("You are too young to buy alcohol")
else:
    if isDrunk:
        print("You are drunk? We cannot sell you alcohol")
    else:
        if isEstrictedArea:
            print("Restricted area. Alcohol is forbidden")
        else:
            print("OK, you can buy alcohol")

print("----")