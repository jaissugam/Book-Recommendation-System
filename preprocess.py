import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from nltk.stem.porter import PorterStemmer

def changeRating(num):
    new='badr'
    if num>=0.001 and num<0.01:
        new='lowr'
    elif num>=0.01 and num<0.1:
        new='poorr'
    elif num>=0.1 and num<1:
        new='decentr'
    elif num>=1 and num<10:
        new='goodr'
    elif num>=10 and num<50:
        new='outstandingr'
    elif num>=50:
        new='greatr'
    return new

def makeLists(text):
    results=re.split(';|&|and|\*|\n', text)
    lists=[]
    for r in results:
        lists.append((r.replace(" ","")).lower())
    return lists

def changeDescription(text):
    res=text.lower()
    res=re.sub(r'[^\w]', ' ', res)
    l=[]
    ps=PorterStemmer()
    for word in res.split():
        l.append(ps.stem(word))
    return l
   
def readData():
    df=pd.read_csv('books.csv')
    books=df.drop(columns=['isbn10','subtitle','thumbnail','published_year','num_pages'])
    books['popularity']=(books['average_rating']*books['ratings_count'])/100000
    books.dropna(inplace=True)
    books['popularity']=books['popularity'].apply(changeRating)
    books=books.drop(columns=['average_rating','ratings_count'])
    books['authors']=books['authors'].apply(makeLists)
    books['categories']=books['categories'].apply(makeLists)
    books['popularity']=books['popularity'].apply(lambda a:a.split())
    books['description']=books['description'].apply(changeDescription)
    books['label']=books['authors']+books['categories']+books['description']+books['popularity']
    books=books.drop(columns=['authors','categories','description','popularity'])
    books['label']=books['label'].apply(lambda w:" ".join(w))
    books['title']=books['title'].apply(lambda s:s.replace("\"",""))
    return books

def makeVector(books):
    vect=CountVectorizer(max_features=4000,stop_words='english')
    vector=vect.fit_transform(books['label']).toarray()
    return vector

def findCosine(v):
    proximityVector=cosine_similarity(v)
    return proximityVector

def finalData():
    books=readData()
    vect=makeVector(books)
    proximityVector=findCosine(vect)
    return books,proximityVector

def listBooks():
    books=readData()
    return books['title'].values.tolist()