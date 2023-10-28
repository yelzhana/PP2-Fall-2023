#TASK1
n = int(input())
squares = (i * i for i in range(n))
for i in squares:
    print(i)

#TASK2
def even_numbers_generator(n):
    for num in range(2, n + 1, 2):
        yield num

def main():
    try:
        n = int(input())
        if n < 0:
            print()
            return

        even_numbers = even_numbers_generator(n)
        result = ",".join(map(str, even_numbers))
        print(f"Even numbers between 0 and {n}: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

#TASK3
def divisible_generator(n):
    for num in range(0, n):
        if(num%3==0 and num%4==0):
            yield num

def main():
    try:
        n = int(input())
        if n < 0:
            print()
            return
        
        divisible = divisible_generator(n)
        result = ",".join(map(str, divisible))
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

#TASK4
def squares_generator(a,b):
    for num in range(a, b):
        num = num**2
        yield num

def main():
    a = int(input())
    b = int(input())
        
    squares = squares_generator(a,b)
    result = ",".join(map(str, squares))
    print(result)

if __name__ == "__main__":
    main()

#TASK5
def numbers_generator(n):
    while n >= 0:
        yield n
        n -= 1

def main():
    n = int(input())
    numbers = numbers_generator(n)
    result = ",".join(map(str, numbers))
    print(result)

if __name__ == "__main__":
    main()