data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']
for error in data:
    print(error.upper())

for error in data:
    print(error.split(':'))
elements = error.split(':')

print(elements[0].upper(), elements[1])

for error in data:
    print(error.split(':'))
elements = error.split(':')
if elements[0] == "Error":
    print(elements[1].upper())
else:
    print(elements[1])