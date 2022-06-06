from flask import Flask,render_template,request
from recom import recommend

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/recom',methods=['GET','POST'])
def recom():
    book=request.form['book']
    recoms=recommend(book)
    return (" | ".join(recoms))