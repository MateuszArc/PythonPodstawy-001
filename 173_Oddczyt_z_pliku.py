file = open("c:\\temp\\joke.txt", "r")

content = file.read
print(content)

file.close()

with open('c:\\temp\\joke.txt', 'r') as file:
    content = file.read()
    print(content)

with open('c:\\temp\\joke.txt', 'r') as file:
    content = file.read()
    print(content)