import os

fileIsOk = False

while not fileIsOk:
    filename = input("Enter path to results file: ")

    if os.path.isfile(filename):
        fileIsOk = True


print("The results file is %s"% (filename))