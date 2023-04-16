from flask import Flask, render_template
import requests
import json

def get_the_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

app = Flask(__name__)

@app.route("/")
def index():
    meme_pic, subreddit = get_the_meme()
    return render_template("meme_page.html", meme_pic = meme_pic, subreddit = subreddit)

if __name__ == "__main__":
    app.run()

