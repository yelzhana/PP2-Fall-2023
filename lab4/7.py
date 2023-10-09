n = int(input())
a = set(range(1, n + 1))
p = a
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        p &= guess
    else:
        p &= a-guess

print(' '.join([str(x) for x in sorted(p)]))