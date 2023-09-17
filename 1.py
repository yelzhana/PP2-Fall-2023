#Task1
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#Task2
b = int(input())
h = int(input())
area = (b*h)/2
print(area)

#Task3
n = int(input())
k = int(input())
print(k // n)
print(k % n)

#Task4
n = int(input())
x = n % (24*60)
a = x // 60
b = x % 60
print(a, b)

#Task5
name = str(input())
print('Hello, ' + name + '!')

#Task6
n = int(input())
print('The next number for the number '+ str(n)+ ' is '+ str(n+1) + '.')
print('The previous number for the number '+ str(n)+ ' is '+ str(n-1) + '.')

#Task7
a = int(input())
b = int(input())
c = int(input())
print(a//2+a%2+b//2+b%2+c//2+c%2)

#Task8
a = int(input())
b = int(input())
l = int(input())
N = int(input())

Length = (((N*2)-1)*a) + (((N-1)*b)*2) + (2*l)
print(Length)