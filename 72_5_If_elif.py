age = 17
isDrunk = False
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

if age < 18:
     print("You are too young to buy alcohol")
elif isDrunk:
    print("You are drunk? We cannot sell you alcohol")
elif isEstrictedArea:
    print("Restricted area. Alcohol is forbidden")
else:
    print("OK, you can buy alcohol")