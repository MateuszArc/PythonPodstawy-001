string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
a = 9
b = 4
for art in range(a):
    print(string_A)    

print("---------------------------------")
for i in range(9):
    if i %2 == 0:
        print(string_A)
    else:
        print(string_B)
print("--------------------------------")
for a in range(9):
    print(a*'x')
    a += 1
print("--------------------------------")
for c in range(10):
    if c % 2 == 0:
        print('x' * c)
    else:
        print('o'*c)
        