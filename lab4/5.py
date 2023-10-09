n, m = [int(s) for s in input().split()]

a = [] 
for i in range(n):  
    new_element = int(input()) 
    a.append(new_element)

b = [] 
for j in range(m):  
    new_element = int(input())  
    b.append(new_element)

a1=set(a)
b1=set(b)

c=a1&b1
d=a1-b1
e=b1-a1

c1=sorted(c)
d1=sorted(d)
e1=sorted(e)

print(len(c1))
for num in c1:
    print(num, end=' ')
print()   
print(len(d1))
for num in d1:
    print(num, end=' ')
print()
print(len(e1))
for num in e1:
    print(num, end=' ')