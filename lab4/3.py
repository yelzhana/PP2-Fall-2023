a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a1=set(a)
b1=set(b)
c=a1&b1
c1=sorted(c)
for num in c1:
    print(num, end=' ')