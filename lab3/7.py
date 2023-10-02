a = [int(i) for i in input().split()]
x = int(input())
place = 0
for i in range(len(a)):
    if(a[i]==x):
        place = i+1
    elif(a[i]>x):
        place = i+1
print(place+1)
