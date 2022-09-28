name = 'Mateusz'
age = 11
daysInYear = 365
daysInYear = 365 * age
message = ' {0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, daysInYear))

name = 'Jan'
age = 26
daysInYear = 365
daysInYear = 365 * age
message = ' {0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, daysInYear))

name = 'Chris'
age = 17
daysInYear = 365
daysInYear = 365 * age
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, daysInYear))

number = 1234567890
number2 = 12345
score = number // number2
score2 = number % number2
message = '{0:d} divided by {1:d} is {2:d} and the rest is {3:d}'
print(message.format(number, number2, score, score2))