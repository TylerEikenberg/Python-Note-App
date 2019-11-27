from peewee import *
from datetime import date
db = PostgresqlDatabase('note', user='postgres', password='',
                        host='localhost', port=5432)
db.connect() 

class BaseModel(Model):
    class Meta:
        database = db

# note taking app
# model for people
# model for notes

class Person(BaseModel):
    name = CharField()

class Note(BaseModel):
    date_created = DateField()
    note-content = TextField()

db.create_tables([Person, Note])