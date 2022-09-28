import os
webaddresses = []
line = input("Please enter www adress: ")
while not line == "":
    line = input("Please enter www adress: ")
    webaddresses.append(line)
print(webaddresses)
dirname = os.getcwd()
filename = input("Enter the file name: ")
filepath = os.path.join(dirname, filename)
file = open(filepath, 'w')
for adress in webaddresses:
    filepath.write(adress, '\n')

filepath.close()
print("--------------------")
import os
filename1 = input("Podaj ścieżkę dostępu do pliku: ")
while not filename1 == os.path.isfile:
    filename1 = input("Podaj ścieżkę dostępu do pliku: ")
    if not filename1 == os.path.isfile:
        print("plik nie istnieje! Spróbuj ponownie!")
    webaddresses1 = []
    filename.open()
    with open(filename,'r') as file:
        for line in file:
            webaddresses.append(line.replace("\n",''))
            for line in webaddresses:
                if line.endswith('.pl'):
                    print(line,'is a polish web page')
                else:
                    print(line, 'is not a polish web page')
print("------------------------------------------------------------------")
import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line+"\n")
    else:
        fileOther.write(line+"\n")
filePL.close()
fileOther.close()
