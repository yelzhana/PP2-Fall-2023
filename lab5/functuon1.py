#TASK1
def grams_to_ounce(gram):
    ounce = gram*28.3495231
    print(ounce)
gram = int(input())
grams_to_ounce(gram)

#TASK2
def far_to_cei(F):
    C = (5/9)*(F-32)
    print(C)
F=int(input())
far_to_cei(F)

#TASK3
def solve(numheads, numlegs):
    if(numlegs<numheads or numlegs%2!=0):
        print('No solution')
    else:
        r = (numlegs + (-2)*numheads)/2
        c = (numlegs-numheads) - 3*r
        print(c, r, end = ' ')
        
numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)

#TASK4
def filter_prime(a):
    b = []
    for i in range(len(a)):
        if a[i] == 1:
            b.append(a[i])
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                b.append(i)
    return b
            
a = [int(s) for s in input().split()]
result = filter_prime(a)
print(result, end = ' ')

#TASK5
a = str(input())
result = []
def permutations(data, i):
    a1=list(a)
    if i == len(a1): 
        result.append(''.join(data) )
    else: 
        for j in range(i, len(a)): 
            data[i], data[j] = data[j], data[i] 
            permutations(data, i + 1) 
            data[i], data[j] = data[j], data[i]  
permutations(list(a), 0)

print(str(result))

#TASK6
a = str(input())
a1 = list(a)

def rev(a): 
    words = a.split(' ') 
    rever = ' '.join(reversed(words)) 
    return rever
print(rev(a))

#TASK7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = [int(s) for s in input().split()]
print(has_33(nums))

#TASK8
def has_007(nums):
    pattern = [0, 0, 7]
    pattern_index = 0

    for num in nums:
        if num == pattern[pattern_index]:
            pattern_index += 1
            if pattern_index == len(pattern):
                return True
    return False
        
nums = [int(s) for s in input().split()]
print(has_007(nums))

#TASK9
def volume(r):
    volume = 4*(r*r*r*3.14)/3
    print(volume)
    
r = int(input())
volume(r)

#TASK10
def delete_duplicate(lst):
    x = []
    for i in range(len(lst)):
        if(lst[i] not in x):
            x.append(lst[i])
    print(x, end=' ')

lst = [int(s) for s in input().split()]
delete_duplicate(lst)

#TASK11
def palindrome(string):
    s = string[::-1]
    if(string == s):
        print('True')
    else:
        print('False')

string = str(input())
palindrome(string)

#TASK12
def histogram(lst):
    for num in lst:
        print('*' * num)
    
lst = [int(s) for s in input().split()]
histogram(lst)

#TASK13
def guess_the_number():
    num = int(input())
    
    print("Hello! What is your name?")
    name = str(input())
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    
    while True:
        print('Take a guess.')
        guess = int(input())

        guesses += 1
            
        if(num>guess):
                print('Your guess is too low.')
        elif(num<guess):
                print('Your guess is too high.')
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
        
guess_the_number()
