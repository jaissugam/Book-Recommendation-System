from preprocess import *

def recommend(book):
    books,proximityVector=finalData()
    recomms=[]
    if book in books['title'].tolist():
        index = books[books['title'] == book].index[0]
        distances = sorted(list(enumerate(proximityVector[index])),reverse=True,key = lambda x: x[1])
        for i in distances[1:7]:
            temp=[]
            bookTitle=books.iloc[i[0]].title
            bookThumbnail=getThumbnail(bookTitle)
            temp.append(bookTitle)
            temp.append(bookThumbnail)
            recomms.append(temp)
    return recomms




