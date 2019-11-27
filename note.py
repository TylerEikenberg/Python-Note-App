from peewee import *
import datetime
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
    note_title = CharField()
    note_content = TextField()
    date_created = CharField()
    user_name = CharField()

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
    return user_name

    # create note title
    # create note content
    # user should be able to view all notes
    # user should be able to find a specific note
def get_selection():
    selection = str(input("To create a note enter CREATE\nTo view all notes enter VIEW\nTo find a specific note enter FIND\nEnter your selection: "))
    if selection == 'CREATE':
        start_create()
    # elif selection == 'VIEW':
    #     # start view()
    # elif selection == 'FIND':
    #     # start find()

def start_create(username):
    title = str(input("What would you like to title your note as? "))
    content = str(input("Write your note: "))
    date = datetime.datetime.now()
    new_note = Note(note_title=title, 
                    note_content=content, 
                    date_created=date, 
                    user_name=username)
    new_note.save()


    

start_create("Tyler Eikenberg")