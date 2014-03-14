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
    if not Post.table_exists():
        db.connect()
        Post.create_table(True)
        Comment.create_table(True)
        Post.create(title='Hello World', author='Bram & Haxe', link = '/', text='Welcome to Mustached Octo Shame !.', date=datetime.datetime.now()).save()

def get_posts():
    db.connect()
    p = map(lambda p: p.to_dict(), Post.select().order_by(Post.date.desc()))
    return p

def get_post(dbid):
    db.connect()
    p = Post.get(Post.dbid == dbid).to_dict()
    p['comments'] = get_post_comments(dbid)
    return p

def get_post_comments(dbid):
    db.connect()
    c = map(lambda c: c.to_dict(), Post.get(Post.dbid == dbid).comments.order_by(Comment.date.desc()))
    return c

def store_post(title, author, link, text, date):
    db.connect()
    Post.create(title=title, author=author, link=link, text=text, date=date).save()

def store_comment(post, author, text, date):
    db.connect()
    Comment.create(post=post, author=author, text=text, date=date).save()
