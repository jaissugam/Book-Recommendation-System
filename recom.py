from preprocess import *

def recommend(book):
    books,proximityVector=finalData()
    recomms=[]
    if book in books['title'].tolist():
        index = books[books['title'] == book].index[0]
        distances = sorted(list(enumerate(proximityVector[index])),reverse=True,key = lambda x: x[1])
        for i in distances[1:6]:
            recomms.append(books.iloc[i[0]].title)
    return recomms

#choice=input("Enter a book you like : ")
#print('\n~ Fetching books you might like ~')
#print(recommend(choice))




