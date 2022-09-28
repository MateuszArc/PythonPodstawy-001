import random
from tokenize import group

for i in range(10):
    print(random.choice(range(1, 100)))

number1 = random.randint(1, 100)
counter = 1
number2 = random.randint(1, 100)
print(counter, number2)

while number1 != number2:
    counter += 1
    number2 = random.randint(1, 100)
    print(counter, number2)
    
print("The number of attempts is:", counter)

countries = [
        'Uruguay',
        'Russia',
        'Saudi Arabia',
        'Egypt',
        'Spain',
        'Portugal',
        'Iran',
        'Morocco',
        'France',
        'Denmark',
        'Peru',
        'Australia',
        'Croatia',
        'Argentina',
        'Nigeria',
        'Iceland',
        'Brazil',
        'Switzerland',
        'Serbia',
        'Costa Rica',
        'Sweden',
        'Mexico',
        'Korea Republic',
        'Germany',
        'Belgium',
        'England',
        'Tunisia',
        'Panama',
        'Colombia',
        'Japan',
        'Senegal',
        'Poland'
        ]
random.shuffle(countries)
groupNumber = 0

for country in range(len(countries)):
    if country % 4 == 0:
        groupNumber += 1
        print("---Group %d---" % (groupNumber))
        print(countries[country])