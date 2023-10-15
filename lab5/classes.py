import math
#TASK1
class string:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Enter a string: ")
    
    def printString(self):
        print(self.my_string.upper())

result = string()
result.getString()
result.printString()

#TASK2
class Shape:
    def Area(self):
        return 0
      
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def Area(self):
        self.area = self.length*self.length
        return self.area

shape = Shape()
print(shape.Area())

length = float(input())
square = Square(length)
print(square.Area())

#TASK3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Area(self):
        self.area = self.length*self.width
        return self.area
    
length = float(input())
width = float(input())
rectangle = Rectangle(length, width)
print(rectangle.Area())

#TASK4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self,new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, point2):
        dx = self.x-point2.x
        dy = self.y-point2.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
    
x1=int(input())
y1=int(input())

x2=int(input())
y2=int(input())

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()

x3=int(input())
y3=int(input())

point1.move(x3, y3)
point1.show()

distance = point1.dist(point2)
print(distance)

#TASK5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, plus):
        self.depos = self.balance + plus
        print(self.depos)

    def withdraw(self, minus):
        if(self.balance>=minus):
            self.withdrawal = self.balance - minus
            print(self.withdrawal)
        else:
            print('Insufficient balance')

owner_name = input()
balance_card = float(input())
account = Account(owner_name, balance_card)

print(f"Hello, {owner_name}, you have {balance_card} on your balance, press 1 if you want to deposit or Press 0 if you want to withdraw")
choice = int(input())
if(choice==1):
    add = float(input())
    account.deposit(add)
elif(choice==0):
    substract = float(input())
    account.withdraw(substract)

#TASK6
def filter_prime(a):
    b = []
    for i in range(len(a)):
        if a[i] == 1:
            b.append(a[i])
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                b.append(i)
    return b

class prime:
    def __init__(self, a):
        self.numbers = a
   
    def filter_primes(self):
        return list(filter(lambda x: x in filter_prime(self.numbers), self.numbers))
            
a = [int(s) for s in input().split()]

prime_filter = prime(a)
prime_numbers = prime_filter.filter_primes()

print(prime_numbers)
