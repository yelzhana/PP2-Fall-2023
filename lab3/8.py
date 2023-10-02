a = [int(i) for i in input().split()]
count = 1
for i in range(0,len(a)-1):
    if(a[i] != a[i+1]):
        count = count+1
print(count)
