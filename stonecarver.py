from peewee import *
import datetime

db = SqliteDatabase('stones.db')

class Post(Model):
    title = CharField()
    author = CharField()
    link = CharField()
    text = TextField()
    date = DateField()

    class Meta:
        database = db
 
class Comment(Model):
    author = CharField()
    text = TextField()
    date = DateField()
    
    class Meta:
        database = db
 
def init():
    db.connect()
    Post.create_table(True)
    Comment.create_table(True)
    Post.create(title='Hello World', author='Bram & Haxe', link = '/', text='Welcome to Mustached Octo Shame !.', date=datetime.datetime.now()).save()

def get_posts():
    return list(Post.select().order_by(Post.date.desc()))
