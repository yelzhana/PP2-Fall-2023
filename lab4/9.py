n = int(input())
all_known = set()
any_known = set()

for _ in range(n):
    number=int(input())
    languages=set()
    for _ in range(number):
        language = input()
        languages.add(language)
    if(any_known==set()):
        all_known.update(languages)
        any_known.update(languages)
    else:
        all_known &= languages
        any_known |= languages
        
print(len(all_known))
for language in sorted(all_known):
    print(language)

print(len(any_known))
for language in sorted(any_known):
    print(language)