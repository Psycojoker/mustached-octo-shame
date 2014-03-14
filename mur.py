from datetime import datetime
from flask import Flask, render_template
from stonecarver import init, get_posts, get_post
app = Flask(__name__)


@app.route("/")
def home():
    posts = get_posts()
    return render_template("home.html", posts=posts)


@app.route("/<id>")
def post(id):
    post = get_post(id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    init()
    app.run(debug=True)
