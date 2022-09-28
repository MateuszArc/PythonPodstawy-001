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
print(line.index('p'))