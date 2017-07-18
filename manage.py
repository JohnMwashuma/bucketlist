""" Initialization of the Database Models and Creating their respective tables """
from bucketlist import app, db
from flask_script import Manager, prompt_bool
from models import User, Wish

manager = Manager(app)

# Create Database Tables
@manager.command
def initdb():
    """ Creates the Database tables of the Imported models above """
    db.create_all()
    print("Initialized database")

# Drop/Delete Database tables
@manager.command
def dropdb():
    """ Deletes the all tables in the database """
    if prompt_bool("Are you sure you want to loose all your data?"):
        db.drop_all()
        print("Dropped the database")

if __name__ == "__main__":
    manager.run()
