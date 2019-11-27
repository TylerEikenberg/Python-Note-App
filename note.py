from peewee import *
import datetime
import pyfiglet
import sys
db = PostgresqlDatabase('note', user='postgres', password='',
                        host='localhost', port=5432)
db.connect() 
# pipenv run python note.py 

# Note db Models ------------------------------------
class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    full_name = CharField()

class Note(BaseModel):
    note_title = CharField()
    note_content = TextField()
    date_created = CharField()
    user_name = CharField()

db.create_tables([Person, Note])
# --------------------------------------------------


# intro to app
def app_intro():
    title = pyfiglet.figlet_format("PyThoughts")
    subtitle = "--A Python note-taking application--\n-\n-"
    print(title)
    print(subtitle)
# get users name
def get_user():
    # user_name = str(input("\nPlease enter your full name: "))
    # new_user = Person(full_name=user_name)
    # new_user.save()
    # return user_name
    user_name = str(input("\nPlease enter your full name: "))
    user_exists = Person.select().where(Person.full_name == user_name)
    if (not user_exists):
        new_user = Person(full_name=user_name)
        new_user.save()
    elif(user_exists):
        Note.select().where(Note.user_name == user_name)
        # print(f'\nHere are your current notes:\n{notes}')
    return user_name

def get_selection(username):
    print(f'\n\nHello {username}!\n')
    selection = str(input("\nTo create a note enter CREATE\nTo view all notes enter VIEW\nTo find a specific note enter FIND\nEnter your selection: "))
    if selection == 'CREATE':
        start_create(username)
    # elif selection == 'VIEW':
    #     # start view()
    # elif selection == 'FIND':
    #     # start find()

def start_create(username):
    title = str(input("\nWhat would you like to title your note as? "))
    content = str(input("\nWrite your note: "))
    date = datetime.datetime.now()
    new_note = Note(note_title=title, 
                    note_content=content, 
                    date_created=date, 
                    user_name=username)
    new_note.save()
    print(f'\n{date}\n{title}\n---\n{content}\n---')
    new_selection = str(input("\nWould you like to create a new note or return to the main menu? (CREATE or MENU. q to exit): "))
    if new_selection == "CREATE":
        start_create(username)
    elif new_selection == "MENU":
        get_selection(username)
    elif new_selection == "q":
        sys.exit(0)


def start_app():
    app_intro()
    username = get_user()
    get_selection(username)

start_app()    

#   todo  
#   user should be able to view all notes
#   user should be able to find a specific note


