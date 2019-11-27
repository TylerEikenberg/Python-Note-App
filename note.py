from peewee import *
from datetime import date
import pyfiglet
db = PostgresqlDatabase('note', user='postgres', password='',
                        host='localhost', port=5432)
db.connect() 
# pipenv run python note.py 

class BaseModel(Model):
    class Meta:
        database = db

# note taking app
# model for people
# model for notes

class Person(BaseModel):
    full_name = CharField()

class Note(BaseModel):
    date_created = DateField()
    note_content = TextField()

db.create_tables([Person, Note])

# prompt user for full name, create Person from name

def app_intro():
    title = pyfiglet.figlet_format("PyThoughts")
    subtitle = "--A Python note-taking application--\n-\n-"
    print(title)
    print(subtitle)
# app_intro()

def get_user():
    user_name = str(input("Please enter your full name: "))
    new_user = Person(full_name=user_name)
    new_user.save()

get_user()