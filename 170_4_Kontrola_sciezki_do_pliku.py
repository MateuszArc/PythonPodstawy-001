import os

while True:
    filename = input("Enter path to results file: ")

    if os.path.isfile(filename):
        break
    else:
        print("File name is not correct! Try again!")

print("The results file is %s"% (filename))