numbers =  [1]

line = ''
for n in numbers:
    line += "%3d"

print(numbers)
for i in range(5):

    newNumbers = [1]

    position = 0
    while position < len(numbers) -1:
        newNumbers.append(numbers[position] + numbers[position] +1)
        position +=1
    newNumbers.append(1)

    numbers = newNumbers.copy()
    print(numbers)