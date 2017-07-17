from bucketlist import app, db
from flask_script import Manager, prompt_bool
from models import User, Wish,Tag

manager = Manager(app)

# Create Database Tables
@manager.command
def initdb():
    db.create_all()
    print("Initialized database")

# Drop/Delete Database tables
@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to loose all your data?"):
        db.drop_all()
        print("Dropped the database")

if __name__ == "__main__":
    manager.run()
