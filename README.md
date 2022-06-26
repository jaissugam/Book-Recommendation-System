## Book-Recommendation-System
#### Currently, the webapp and the underlying recommender model works to recommend content-wise most similar books upon user's input using Cosine Similarity. It's built upon popular [7k Books](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata) dataset.

##### Straight up from the dataset, the dataframe looks like this :point_down:<br>
<img width="800" alt="image" src="https://user-images.githubusercontent.com/67289887/174998044-f75bf47f-89b0-4cda-92ce-e941cee6caa3.png"><br>
##### which, then takes the following form <br>
<img width="800" alt="image" src="https://user-images.githubusercontent.com/67289887/174998507-5570f136-e656-4b3d-b0b4-fdc7e7a2f17f.png"><br>
##### to finally take the shape as follows :point_down:<br>
<img width="800" alt="image" src="https://user-images.githubusercontent.com/67289887/174998639-fa6e2bc4-d33b-43bb-8618-40d5716e183e.png"><br>
##### using
***Step 1:*** **Identification of less valuable columns**
```python
books=df.drop(columns=['isbn10','subtitle','thumbnail','published_year','num_pages'])
```
***Step 2:*** **Transformation of 'ratings'-related columns**
>The 'average rating' and 'ratings count' values were taken into account to make a new 'popularity' value which was then manipulated to convert quantitative values into categorical values for better training.
```python
books['popularity']=(books['average_rating']*books['ratings_count'])/100000
books['popularity']=books['popularity'].apply(changeRating)
```
***Step 3:*** **Treatment of missing values**
```python
books.dropna(inplace=True)
```
***Step 4:*** **Stemming**
>It is a widely-used NLP technqiue to bring individual words into their simplest forms so that the model treats words like 'reads' and 'reading' to be similar in meaning. An NLTK module named PorterStemmer is used for this purpose.

***Step 5:*** **Count Vectorization**
>After the preprocessing steps, SKlearn is used on the final dataframe to make vectors of words based on the count of words.
```python
vect=CountVectorizer(max_features=4000,stop_words='english')
vector=vect.fit_transform(books['label']).toarray()
```
***Step 6:*** **Cosine Similarity**
>It is a computation method which calculates the similarities and differences between two vectors based on the cosine angle difference between them. SKlearn's 'cosine_similarity' module takes the count vector generated after Step 5 as input and outputs a vector showing the proximity of all the datapoints with one another.
```python
proximityVector=cosine_similarity(vector)
```

#### To get the Flask app up and running in your local machine,
1. Head to [deploy branch](https://github.com/jaissugam/Book-Recommendation-System/tree/deployv1)
2. Clone the repo to your local directory.
3. Navigate to your directory.
4. Meet all environment requirements.
```
pip install -r requirements.txt
```
5. Get the Flask running
```
flask run
```

*Deployed on* [Heroku](https://id.heroku.com/login)





