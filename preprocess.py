import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from nltk.stem.porter import PorterStemmer

#To tansform the ratings into different categories
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

#To remove unnecessary characters and produce a list of words out of text
def makeLists(text):
    results=re.split(';|&|and|\*|\n', text)
    lists=[]
    for r in results:
        lists.append((r.replace(" ","")).lower())
    return lists

#For stemming
def changeDescription(text):
    res=text.lower()
    res=re.sub(r'[^\w]', ' ', res)
    l=[]
    ps=PorterStemmer()
    for word in res.split():
        l.append(ps.stem(word))
    return l

#For overall preprocessing of the data using above methods 
def readData():
    df=pd.read_csv('books.csv')
    pickle.dump(df,open("old-books-list.pkl","wb")) #Storing original dataframe
    books=df.drop(columns=['isbn10','subtitle','thumbnail','published_year','num_pages'])
    books['popularity']=(books['average_rating']*books['ratings_count'])/100000 #Creating new column
    books.dropna(inplace=True)
    books['popularity']=books['popularity'].apply(changeRating)
    books=books.drop(columns=['average_rating','ratings_count'])
    books['authors']=books['authors'].apply(makeLists)
    books['categories']=books['categories'].apply(makeLists)
    books['popularity']=books['popularity'].apply(lambda a:a.split()) #To make list out of string
    books['description']=books['description'].apply(changeDescription)
    books['label']=books['authors']+books['categories']+books['description']+books['popularity'] #Making a final label
    books=books.drop(columns=['authors','categories','description','popularity'])
    books['label']=books['label'].apply(lambda w:" ".join(w)) #To make string out of list
    books['title']=books['title'].apply(lambda s:s.replace("\"",""))
    #return books
    pickle.dump(books,open("new-books-list.pkl","wb"))

#To construct count-vectorizer
def makeVector(books):
    vect=CountVectorizer(max_features=4000,stop_words='english')
    vector=vect.fit_transform(books['label']).toarray()
    #return vector
    pickle.dump(vector,open("count-vector.pkl","wb"))

#To return final cosine similarity vector
def findCosine(v):
    proximityVector=cosine_similarity(v)
    return proximityVector

def finalData():
    #books=readData()
    #vect=makeVector(books)
    books=pickle.load(open("new-books-list.pkl","rb"))
    vect=pickle.load(open("count-vector.pkl","rb"))
    proximityVector=findCosine(vect)
    return books,proximityVector

def listBooks():
    #books=readData()
    books=pickle.load(open("new-books-list.pkl","rb"))
    return books['title'].values.tolist()

def getThumbnail(title):
    #old=pd.read_csv('books.csv')
    old=pickle.load(open("old-books-list.pkl","rb"))
    #new=readData()
    new=pickle.load(open("new-books-list.pkl","rb"))
    id=new.loc[new['title'] == title, 'isbn13'].iloc[0]
    return old.loc[old['isbn13']==id,'thumbnail'].iloc[0]
