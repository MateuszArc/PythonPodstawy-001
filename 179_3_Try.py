import sys

tasksPerPerson = 0

try:
    tasks = 32
    personStr = input("how many persons are there in the team? ")
    persons = int(personStr)

    tasksPerPerson = tasks / persons

except:
    print("Something went wrong...", sys.exc_info())
print("Every person should have around", tasksPerPerson, "tasks.")