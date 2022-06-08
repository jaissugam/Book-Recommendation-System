from flask import Flask,render_template,request
from recom import recommend

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        book=request.form['book']
        recoms=recommend(book)
        return render_template('home.html',recoms=recoms)
    else:
        return render_template('home.html')
