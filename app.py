from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import json
import requests

app = Flask(__name__)

app.secret_key = "csfakjfsadfasklfjhsb"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1172'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

def get_the_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route('/')
def home():
    meme_pic, subreddit = get_the_meme()
    return render_template("home.html", meme_pic = meme_pic, subreddit = subreddit)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('home'))
    
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = cur.fetchone()
        cur.close()
        if user is not None:
            if password == user[2]:
                session['name'] = user[0]
                session['email'] = user[1]
                meme_pic, subreddit = get_the_meme()
                return render_template("home.html", meme_pic = meme_pic, subreddit = subreddit)
            else:
                return "Error password and email not matched"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    meme_pic, subreddit = get_the_meme()
    return render_template("home.html", meme_pic = meme_pic, subreddit = subreddit)

if __name__ == '__main__':
    app.run(debug=True)