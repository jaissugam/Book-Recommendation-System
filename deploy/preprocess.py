import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer

def findCosine(v):
    proximityVector=cosine_similarity(v)
    return proximityVector

def finalData():
    books=pickle.load(open("new-books-list.pkl","rb"))
    vect=pickle.load(open("count-vector.pkl","rb"))
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
