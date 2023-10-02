a = [int(i) for i in input().split()]
max=0
for i in range(1, len(a)):
    if a[i]>a[max]:
        max = i
print(a[max], max, end=' ')