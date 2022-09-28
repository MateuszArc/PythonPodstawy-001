file = open("c:\\temp\\joke.txt", "r")

content = file.read
print(content)

file.close()

with open('c:\\temp\\joke.txt', 'r') as file:
    content = file.read()
    print(content)

with open('c:\\temp\\joke.txt', 'r') as file:
    for line in file:
        print(line)

file = open("c:\\temp\\joke.txt", "r")
for line in file:
    print(line)
file.close()

file = open("c:\\temp\\joke.txt", "r")
for line in file.readlines():
    print(line)
file.close()

file = open("c:\\temp\\joke.txt", "r")
for line in file.readlines():
    print(line)
file.close()