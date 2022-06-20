import numpy as np
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import gzip

def findCosine(v):
    proximityVector=cosine_similarity(v)
    return proximityVector

def finalData():
    books=pickle.load(open("new-books-list.pkl","rb"))
    vect=pickle.load(gzip.open("count-vector.zip","rb"))
    proximityVector=findCosine(vect)
    return books,proximityVector

def listBooks():
    books=pickle.load(open("new-books-list.pkl","rb"))
    return books['title'].values.tolist()

def getThumbnail(title):
    old=pickle.load(open("old-books-list.pkl","rb"))
    new=pickle.load(open("new-books-list.pkl","rb"))
    id=new.loc[new['title'] == title, 'isbn13'].iloc[0]
    return old.loc[old['isbn13']==id,'thumbnail'].iloc[0]


#def zipVector(books):
#    vect=CountVectorizer(max_features=4000,stop_words='english')
#    vector=vect.fit_transform(books['label']).toarray()
    #return vector
    #pickle.dump(vector,open("count-vector.pkl","wb"))
#    pickle.dump(vector, gzip.open("count-vector.zip","wb"))

#zipVector(pickle.load(open("new-books-list.pkl","rb")))