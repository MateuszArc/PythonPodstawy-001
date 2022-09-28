import os

fileIsOk = False

while True:
    filename = input("Enter path to results file: ")

    if os.path.isfile(filename):
        break


print("The results file is %s"% (filename))