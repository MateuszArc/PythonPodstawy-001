from datetime import date
from datetime import timedelta
def GiveWorkingDay(year=date.today().year,\
                  month=date.today().month,\ 
                  day=date.today().day):
    #prints the nearlest workind day date
    
    #day = date.today()
    day = date(2017,9,30)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for', day,'is',workingday)
    return workingday

GiveWorkingDay(2017,9)
GiveWorkingDay()
GiveWorkingDay(2017,2)