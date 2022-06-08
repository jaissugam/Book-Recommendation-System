from flask import Flask,render_template,request,flash
from recom import recommend

app=Flask(__name__)
app.secret_key = 'a#xtQ1$%op'

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        flash('Hold on..Fetching your next reads!')
        book=request.form['book']
        recoms=recommend(book)
        flash('You might enjoy reading the following books...')
        return render_template('home.html',recoms=recoms)
    else:
        return render_template('home.html')
