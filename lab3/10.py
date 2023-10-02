a = [int(i) for i in input().split()]
max = 0
min = 0
for i in range(1, len(a)):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        min = i
a[max], a[min] = a[min], a[max]
print(' '.join([str(i) for i in a]))
