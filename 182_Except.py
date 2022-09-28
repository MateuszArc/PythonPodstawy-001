import sys

tasksPerPerson = 0

try:
    tasks = 32
    personStr = input("how many persons are there in the team? ")
    persons = int(personStr)

    tasksPerPerson = tasks / persons

except ValueError:
    print("Sorry - you need to enter an integer number")

except ZeroDivisionError:
    print("Sorry - you need to enter value > 0")
#except:
    #print("Something went wrong...", sys.exc_info())

print("Every person should have around", tasksPerPerson, "tasks.")