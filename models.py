from datetime import datetime
from bucketlist import db

# Creates a Pivot or Junction table for table Tags and Wishes
tags = db.Table('wish_tag',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('wish_id', db.Integer, db.ForeignKey('wish.id'))
)

# Creates the Wishes table
class Wish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(500), nullable=False)
    wish_status = db.Column(db.Boolean, nullable=True, default=False)
    wish_progress = db.Column(db.Boolean, nullable=True, default=False)
    image_filename = db.Column(db.String, default=None, nullable=True)
    image_url = db.Column(db.String, default=None, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    _tags = db.relationship('Tag', secondary=tags, lazy='joined',
                            backref=db.backref('wishitems', lazy='dynamic')) # Many to Many Relationship with the tag table
    
    def __repr__(self):
        return "<Wish '{}' : '{}'>".format(self.title, self.description)

# Creates the Tag table   
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True, index=True)  
    
    def __repr__(self):
        return self.name

# Creates the User table  
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    wish = db.relationship('Wish', backref = 'user', lazy = 'dynamic') # One to Many Relationship with the Wish Table
    password_hash = db.Column(db.String)

    def __repr__(self):
        return "<User %r>" % self.username