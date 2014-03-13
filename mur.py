from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    #posts = get_posts()
    posts = [{"title": "pouet", "link": "http://tamere.com", "author": "haxe", "date": datetime.now()}]

    return render_template("home.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
