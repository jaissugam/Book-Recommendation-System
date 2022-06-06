from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/recom')
def recommend():
    book=request.args['book']
    return book