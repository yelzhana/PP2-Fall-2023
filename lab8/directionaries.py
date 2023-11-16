import os
import string
#TASK1
path = r'C:\Users\ACER\pp1\pp2'
print("Only directories:")
print([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))])
print("\nOnly files:")
print([x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))])
print("\nDirectories and files")
print([x for x in os.listdir(path)])

#TASK2
def checking(path):
    if os.path.exists(path):
        print(f"{path} exists")

        if os.access(path, os.R_OK):
            print(f"{path} is readable")
        else:
            print(f"{path} is not readable")

        if os.access(path, os.W_OK):
            print(f"{path} is writable")
        else:
            print(f"{path} is not writable")

        if os.access(path, os.X_OK):
            print(f"{path} is executable")
        else:
            print(f"{path} is not executable")
    else:
        print(f"{path} does not exist")

my_path = r'C:\Users\ACER\pp1\pp2'
checking(my_path)

#TASK3
path = r'C:\Users\ACER\pp1\pp2'

if os.path.exists(path):
    print(f"{path} exists")
else:
    print(f'{path} does not exist')

basename = os.path.basename(path)
print(basename)

dirname = os.path.dirname(path)
print(dirname)

#TASK4
with open(r'C:\Users\ACER\pp1\pp2\lect1.py', 'r') as file:
    count = 0
    for line in file:
        if line != "\n":
            count += 1
print(count)

#TASK5
my_list = ["My name ", "is Yelzhana ", "Good to see you "]
 
file1 = open(r'C:\Users\ACER\pp1\pp2\lect1.py', 'w')
file1.writelines(my_list)
file1.close()

#TASK6
if not os.path.exists("letters"):
   os.makedirs("letters")

for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter) 

#TASK7
with open('states.py','r') as firstfile, open('lect1.py','a') as secondfile: 
    for line in firstfile: 
             secondfile.write(line)

f = open("lect1.py", "r")
print(f.read())

#TASK8
path = r'C:\Users\ACER\pp1\pp2\lab8'

if os.path.exists(path):
    print(f"{path} exists")

if os.access(path, os.R_OK):
    print(f"{path} is readable")
else:
    print(f"{path} is not readable")

os.remove("1.py")