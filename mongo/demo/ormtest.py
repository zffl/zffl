import pymongo

from mongoengine import *
from mongoengine.connection import _get_db

connect(db='mongoenginetest')

class Person(Document):
    name = StringField()
    age = IntField() 
    
if __name__ == '__main__':
    person = Person(name="Test User", age=20)
    person.save()