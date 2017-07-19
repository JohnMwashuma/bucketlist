""" Database connection string and routes to the project's templates """
from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import BucketlistForm

app = Flask(__name__)

# Secret key for managing sessions
app.config['SECRET_KEY'] = '\xe0\x9c\xd0o\xc8\x11\rrF\x0e\xe3\x9a\xae\xaa\xb3E\x82\th\xa6\x11\xfcW?'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:6927Mwashi@localhost/bucketlist'
app.config['DEBUG'] = True
db = SQLAlchemy(app)

# An Empty list for holding bucket list items
bucket_list_activities = []

# Method for storing the Bucket list items
def store_bucket_list_item(title, description, bucket_item_status, bucket_item_progress):
    """ Appends or adds a bucketlist_item property to the bucket_list_activities variable """  
    bucket_list_activities.append(dict(
        title=title,
        user='John',
        description=description,
        bucket_item_status=bucket_item_status,
        bucket_item_progress=bucket_item_progress, 
        date=datetime.utcnow()
    ))


def get_bucket_list_activities(num):
    """ Returns sorted bucketitems by date created in terms of the latest bucket """
    return sorted(bucket_list_activities, key=lambda bm: bm['date'], reverse=True)[:num]

# Route to All Public Bucket List Activies 
@app.route('/index')
@app.route('/')
def index():
    """ Returns bucketitems Templates """
    return render_template('all_bucket_list_items.html', bucket_list_activities = get_bucket_list_activities(2))

# Route for Creating a New Bucketlist Item
@app.route('/create', methods=['GET', 'POST'])
def create_bucket_activity():
    """ Returns a bucketlist form for creating new bucketlist activities """
    form = BucketlistForm()
    if request.method == "POST":
        title = form.title.data
        description = form.description.data
        bucket_item_status = form.bucket_item_status.data
        bucket_item_progress = form.bucket_item_progress.data
        store_bucket_list_item(title, description, bucket_item_status, bucket_item_progress)
        return redirect(url_for('index'))
    return render_template('bucket_list_form.html', form = form)

# Route to a User's bucketlist activities i.e. Public and Private Items
@app.route('/my_bucket_list_items')
def my_bucket_list_items():
    """ Returns all bucketlist activities for the logged in user """
    return render_template('my_bucket_list_items.html')

# Route to a User's Public bucketlist activities
@app.route('/my_public_bucket_items')
def my_public_bucket_items():
    """ Returns all bucketlist activities for the logged in user """
    return render_template('my_public_bucket_items.html')

# Route to a User's Private bucketlist activities
@app.route('/my_private_bucket_items')
def my_private_bucket_items():
    """ Returns all bucketlist activities for the logged in user """
    return render_template('my_private_bucket_items.html')

# Route to the login page
@app.route('/login')
def login():    
    return render_template('login.html')

# Route to the signup page
@app.route('/signup')
def signup():    
    return render_template('signup.html')

# Route to a User's Profile 
@app.route('/profile')
def update_profile():
    """ Returns a logged in user profile page """
    return render_template('manage.html')

if __name__ == "__main__":
    app.run(debug=True)
