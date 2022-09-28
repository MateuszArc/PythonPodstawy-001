IsWeekend = True
print("Is weekend =", IsWeekend)

Temperature = 5
print("Temperature =", Temperature)

ToDoList = ''
print("ToDoList =", ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy =", IsHappy)

IsHappy = not IsWeekend and Temperature <= 20 and ToDoList != ''
print("IsHappy =", IsHappy)