movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#TASK1      
def IMDB(movies, index):
    if(movies[index]['imdb']>=5.5):
        print('True')
    elif(movies[index]['imdb']<5.5):
        print('False')
        
x = input()
for i in range(len(movies)):
        if(x==(movies[i]['name'])):
            index = i
IMDB(movies, index)

#TASK2
def IMDB(movies):
    b = []
    for i in range(len(movies)):
        if(movies[i]['imdb']>=5.5):
            b.append(movies[i])
    return b 
  
result = IMDB(movies)
print(result, end = ' ')

#TASK3
def categories(movies, x):
    b = []
    for i in range(len(movies)):
        if(x==(movies[i]['category'])):
            b.append(movies[i])
    return b

x = input()
result = categories(movies, x)
print(result)

#TASK4
def IMDB_average(movies):
    b = []
    sum = 0
    for i in range(len(movies)):
        if(movies[i]['imdb']>=1):
            b.append(movies[i]['imdb'])
    for i in range(len(b)):
        sum += b[i]
        average = sum/len(b) 
    return average
  
result = IMDB_average(movies)
print(result)

#TASK5
def categories(movies, x):
    b = []
    sum = 0
    for i in range(len(movies)):
        if(x==(movies[i]['category'])):
            b.append(movies[i]['imdb'])
    for i in range(len(b)):
        sum += b[i]
        average = sum/len(b) 
    return average

x = input() 
result = categories(movies, x)
print(result)
