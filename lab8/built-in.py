
#TASK1
a = [int(i) for i in input().split()]
def convert(a):
    return tuple(a)
x = convert(a)
result = sum(x)
print(result)

#TASK2
x = str(input())
count_upper = 0
count_lower = 0
for i in x:
    if i.isupper() == True:
        count_upper+=1
    elif i.islower() == True:
        count_lower+=1
print(count_upper, end=" ")
print(count_lower)

#TASK3
x = str(input())
x1 = ''.join(reversed(x))

if (x==x1):
    print("It is palindrome")
else:
    print("It is not palindrome")


#TASK4
from time import sleep
import math

def delay(y, miliseconds, *args):
  sleep(miliseconds / 1000)
  return y(*args)

root = int(input())
seconds = int(input())
print(delay(lambda x: math.sqrt(x), seconds, root))

#TASK5
a = (1, True, True)
x = all(a)
print(x)