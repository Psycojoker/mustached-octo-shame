from datetime import datetime
from flask import Flask, render_template, request, redirect
from stonecarver import init, get_posts, get_post, store_post
app = Flask(__name__)


@app.route("/")
def home():
    posts = get_posts()
    return render_template("home.html", posts=posts)

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template("new.html")
    else:
        store_post(request.form["title"], request.form["author"], request.form["link"], request.form["text"], datetime.now())
        return redirect("/")

@app.route("/<int:id>")
def post(id):
    post = get_post(id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    init()
    app.run(debug=True)
