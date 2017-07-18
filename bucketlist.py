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
db = SQLAlchemy(app)

# An Empty list for holding bucket list items
bucket_list_activities = []

# Method for storing the wish
def store_bucket_list_item(title, description, wish_status, wish_progress):
    bucket_list_activities.append(dict(
        title=title,
        user='John',
        description=description,
        wish_status=wish_status,
        wish_progress=wish_progress, 
        date=datetime.utcnow()
    ))

# Returns sorted bucketitems by date created in terms of the latest bucket
def get_bucket_list_activities(num):
    return sorted(bucket_list_activities, key=lambda bm: bm['date'], reverse=True)[:num]

# Route to All Public Wishes 
@app.route('/index')
@app.route('/')
def index():
    """ Returns allwishes Template """
    return render_template('allwishes.html', bucket_list_activities = get_bucket_list_activities(2))

# Route for Creating a New Wish
@app.route('/create', methods=['GET', 'POST'])
def create():
    """ Returns a wish form for creating new wishes """
    form = BucketlistForm()
    if request.method == "POST":
        title = form.title.data
        description = form.description.data
        wish_status = form.wish_status.data
        wish_progress = form.wish_progress.data
        store_bucket_list_item(title, description, wish_status, wish_progress)
        return redirect(url_for('index'))
    return render_template('wish-form.html', form = form)

# Route to a User's all Wishes i.e. Public and Private
@app.route('/mywishes')
def MyWishes():
    """ Returns all wishes for the logged in user """
    return render_template('all-my-wishes.html')

# Route to a User's Public Wishes
@app.route('/mypublicwishes')
def MyPublicWishes():
    """ Returns all public wishes for the logged in user """
    return render_template('public-wishes.html')

# Route to a User's Private Wishes
@app.route('/myprivatewishes')
def MyPrivateWishes():
    """ Returns all private wishes for the logged in user """
    return render_template('private-wishes.html')

# Route to a User's Profile 
@app.route('/profile')
def Profile():
    """ Returns a logged in user profile page """
    return render_template('manage.html')

if __name__ == "__main__":
    app.run(debug='True')
