N, K = map(int, input().split())
x = set()
y = set()
for i in range(6, N+1, 7):
    y.add(i)
for i in range(7, N+1, 7):
    y.add(i)
for _ in range(K):
    a, b = map(int, input().split())
    for i in range(a, N+1, b):
        if(i not in y):
            x.add(i)
print(len(x))