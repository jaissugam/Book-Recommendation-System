from preprocess import *

def recommend(book):
    books,proximityVector=finalData()
    index = books[books['title'] == book].index[0]
    distances = sorted(list(enumerate(proximityVector[index])),reverse=True,key = lambda x: x[1])
    recomms=[]
    for i in distances[1:9]:
        recomms.append(books.iloc[i[0]].title)
    return recomms

#choice=input("Enter a book you like : ")
#print('\n~ Fetching books you might like ~')
#print(recommend(choice))




