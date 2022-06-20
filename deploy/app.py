from flask import Flask,render_template,request,flash,abort
from recom import recommend
from preprocess import listBooks

app=Flask(__name__)
app.secret_key = 'a#xtQ1$%op'

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        book=request.form['book']
        recoms=recommend(book)
        if len(recoms)>0:
            flash('You might enjoy reading the following books...')
            return render_template('home.html',recoms=recoms,books=listBooks())
        else:
            return abort(404)
    else:
        return render_template('home.html',books=listBooks())

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page-not-found.html'),404

if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0")