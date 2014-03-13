from datetime import datetime
from flask import Flask, render_template
from stonecarver import init
app = Flask(__name__)


@app.route("/")
def home():
    #posts = get_posts()
    posts = [{"id": 1, "title": "pouet", "link": "http://tamere.com", "author": "haxe", "date": datetime.now()}]

    return render_template("home.html", posts=posts)


@app.route("/<id>")
def post(id):
    #post = get_post(id)
    post = {"title": "pouet", "link": "http://tamere.com", "author": "haxe", "date": datetime.now(), "text": "this is the <i>text</i>",
            "comments": [{
                "author": "Bram",
                "text": "youplaboum",
            }]}
    return render_template("post.html", post=post)


if __name__ == "__main__":
    init()
    app.run(debug=True)
