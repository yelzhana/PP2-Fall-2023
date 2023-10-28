from datetime import datetime, timedelta, date
#TASK1
x = datetime.now()
z = x - timedelta(days=5)
y = z.strftime("%Y-%m-%d")

print(y)

#TASK2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
y = yesterday.strftime("%Y-%m-%d")
z = tomorrow.strftime("%Y-%m-%d")
print(y, z, end='')

#TASK3
date1 = datetime.now()
date2 = date1.replace(microsecond=0)
print(date2)

#TASK4
year1 = int(input())
day1 = int(input())
month1 = int(input())
year2 = int(input())
day2 = int(input())
month2 = int(input())
date1 = date(year1, month1, day1)
date2 = date(year2, month2, day2)
if(date1>date2):
    difference = date1-date2
else:
    difference = date2-date1
print(difference.total_seconds())
