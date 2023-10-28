from math import math, tan, pi 
#TASK1
degree = (int(input()))
radian = math.radians(degree)

print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}")

#TASK2
height = int(input())
base1 = int(input())
base2 = int(input())
area = ((base1+base2)*height)/2
print(f"Height: {height}")
print(f"Base1: {base1}")
print(f"Base2: {base2}")
print(f"Expected output: {area}")

#TASK3
sides = int(input())
length = int(input())
area = sides * (length ** 2) / (4 * tan(pi / sides))
print("The area of the polygon is:", int(area))

#TASK4
length = int(input())
height = int(input())
area = length*height
print("Expected Output:", float(area))