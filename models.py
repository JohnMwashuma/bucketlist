""" Bucketlist application classes which are the basically the database tables """
from datetime import datetime
from bucketlist import db

# Creates the Wishes table
class Wish(db.Model):
    """ Creates a Wish Table that will hold all bucketlist wishes """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(500), nullable=False)
    wish_status = db.Column(db.Boolean, nullable=True, default=False)
    wish_progress = db.Column(db.Boolean, nullable=True, default=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    def __repr__(self):
        return "<Wish '{}' : '{}'>".format(self.title, self.description)

# Creates the User table  
class User(db.Model):
    """ Creates a User Table that will hold all bucketlist users """    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    image_filename = db.Column(db.String, default=None, nullable=True)
    image_url = db.Column(db.String, default=None, nullable=True)
    # One to Many Relationship with the Wish Table
    wish = db.relationship('Wish', backref='user', lazy='dynamic') 
    password_hash = db.Column(db.String)

    def __repr__(self):
        return "<User '{}' : '{}'>".format(self.username, self.email) 
    