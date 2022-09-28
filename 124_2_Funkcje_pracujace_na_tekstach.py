line ='This IS a very STRANGE text'
print(line.capitalize())
print(line.title())
print(line.upper())
print(line.lower())
print(line.swapcase())
print(line.casefold())
line = 'der Fluss'
print(line.lower())
print(line.casefold())
line = 'ŻÓŁĆ'
print(line.lower())
print(line.casefold())
print(line.replace('Ż', 'Z'.replace('Ó', 'O').replace('Ł', 'L').replace('Ć', 'C').lower()))

line ='This IS a very STRANGE text'
print(line.count('e'))
print(line.find('e'))
print(line.rfind('e'))
print(line.index('e'))
print(line.rindex('e'))

print(line.find('p'))

print('e' in line)
print('p' in line)

line ='this IS a very STRANGE text'
print(line.startswith('this'))
print(line.startswith('THIS'))
print(line.endswith('text'))

line = """This is a long text
that spans multiple lines
but should be somehow presented in python"""
print(line)
print(line.count('\n'))

import string
print(string.ascii_letters)
print(string.digits)

line = 'this is the end of this lesson'
print(line.split(' '))
list = line.split(' ')
print(list)
print(list.join(' '))