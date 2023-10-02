n, k = [int(s) for s in input().split()]
pop= ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        pop[j] = '.'
print(''.join(pop))