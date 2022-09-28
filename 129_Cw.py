import time

print("Current time is... unix epoch", time.time())
print("Current time is... tuple", time.localtime(time.time()))

import calendar

print(calendar.month(2022, 8))
calendar.setfirstweekday(6)
print(calendar.month(2022, 8))

print(calendar.isleap(2000))
print(calendar.calendar(2019))