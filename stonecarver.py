from peewee import *

class Post(Model):
    title = CharField()
    author = CharField()
    link = CharField()
    text = TextField()
    date = DateField()
 
class Comment(Model):
    author = CharField()
    text = TextField()
    date = DateField()
