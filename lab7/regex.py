import re
#TASK1
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r'аб*'
matches = re.findall(pattern, text)
print(matches)

#TASK2
pattern1 = r'а.{2-3}б'
matches1 = re.findall(pattern1, text)
print(matches1)

#TASK3
pattern3 = r'[а-я]+_[а-я]+'
matches3 = re.findall(pattern3, text)
print(matches3)

#TASK4
pattern4 = r'[А-Я]+[а-я]+'
matches4 = re.findall(pattern4, text)
print(matches4)

#TASK5
pattern5 = r'а.*б/'
matches5 = re.findall(pattern5, text)
print(matches5)

#TASK6
def replacing(text):
    pattern = r'[ ,.]'
    matches = re.sub(pattern, ':', text)
    return matches

result = replacing(text)
print(result)

#TASK7
def snake_to_camel(text):
    camel = re.split('_+', text)
    camel1 = camel[0] + ''.join(map(lambda x: x.title(), camel[1:]))
    return camel1

test = "Поменяй_этот_текст_на_другой"
result = snake_to_camel(test)
print(result)

#TASK8
def spliting(test):
    split_strings = re.split(r'([А-Я])', test)
    split_strings = [split_strings[i] + split_strings[i+1] if i < len(split_strings) - 1 and split_strings[i+1].isupper() else split_strings[i] for i in range(0, len(split_strings), 2)]
    return split_strings

test = "МеняЗовутЕлжана"
result = spliting(test)
print(result)

#TASK9
def space(test):
    string = re.sub(r'([а-я])([А-Я])', r'\1 \2', test)
    return string

test = "МеняЗовутЕлжана"
result = space(test)
print(result)

#TASK10
def camel_to_snake(test):
    string = re.sub(r'([а-я0-9])([А-Я])', r'\1_\2', test)
    sting = string.capitalize()
    return sting

test = "ПоменяйЭтотТекстНаЗмеиныйТекст"
result = camel_to_snake(test)
print(result)
