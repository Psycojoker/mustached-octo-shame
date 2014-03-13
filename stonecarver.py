from peewee import *
import datetime

db = SqliteDatabase('stones.db')

class Post(Model):
    dbid = PrimaryKeyField()
    title = CharField()
    author = CharField()
    link = CharField()
    text = TextField()
    date = DateField()

    def to_dict(self):
        return {'dbid':self.dbid, 'title':self.title, 'author':self.author, 'link':self.link, 'text':self.text, 'date':self.date}

    class Meta:
        database = db
 
class Comment(Model):
    post = ForeignKeyField(Post, related_name='comments')
    author = CharField()
    text = TextField()
    date = DateField()
    
    def to_dict(self):
        return {'author':self.author, 'text':self.text, 'date':self.date}
    
    class Meta:
        database = db
 
def init():
    db.connect()
    Post.create_table(True)
    Comment.create_table(True)
    Post.create(title='Hello World', author='Bram & Haxe', link = '/', text='Welcome to Mustached Octo Shame !.', date=datetime.datetime.now()).save()

def get_posts():
    return map(lambda p: p.to_dict(), Post.select().order_by(Post.date.desc()))

def get_post_comments(dbid):
    return map(lambda c: c.to_dict(), Post.get(Post.dbid == dbid).comments.order_by(Comment.date.desc()))

def store_post(title, author, link, text, date):
    Post.create(title=title, author=author, link=link, text=text, date=date).save()

def store_comment(post, author, text, date):
    Comment.create(post=post, author=author, text=text, date=date).save()
