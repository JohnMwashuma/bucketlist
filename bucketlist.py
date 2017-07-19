""" Routes to the project's templates and logic for CRUD """
from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from forms import BucketlistForm

app = Flask(__name__)



# Secret key for managing sessions
app.config['SECRET_KEY'] = '\xe0\x9c\xd0o\xc8\x11\rrF\x0e\xe3\x9a\xae\xaa\xb3E\x82\th\xa6\x11\xfcW?'


# An Empty list for holding bucket activities
bucket_activities = []

# Method for storing the Bucket activities
def store_bucket_activity(title, description, bucket_activity_status, bucket_activity_progress):
    """ Appends or adds a bucket_activity property to the bucket_list_activities variable """  
    bucket_activities.append(dict(
        title=title,
        user='John',
        description=description,
        bucket_activity_status=bucket_activity_status,
        bucket_activity_progress=bucket_activity_progress, 
        date=datetime.utcnow()
    ))


def get_bucket_activities(num):
    """ Returns sorted bucket activities by date created in terms of the latest bucket """
    return sorted(bucket_activities, key=lambda bm: bm['date'], reverse=True)[:num]

# Route to All Public Bucket Activities 
@app.route('/index')
@app.route('/')
def index():
    """ Returns bucket activities Templates """
    return render_template('all_bucket_activities.html', bucket_activities = get_bucket_activities(2))

# Route for Creating a New Bucket activity
@app.route('/create', methods=['GET', 'POST'])
def create_bucket_activity():
    """ Returns a bucket form for creating new bucket activities """
    form = BucketlistForm()
    if request.method == "POST":
        title = form.title.data
        description = form.description.data
        bucket_activity_status = form.bucket_activity_status.data
        bucket_activity_progress = form.bucket_activity_progress.data
        store_bucket_activity(title, description, bucket_activity_status, bucket_activity_progress)
        return redirect(url_for('index'))
    return render_template('bucket_activity_form.html', form = form)

# Route to a User's bucket activities i.e. Public and Private activities
@app.route('/my_bucket_activities')
def my_bucket_activities():
    """ Returns all bucket activities for the logged in user """
    return render_template('my_bucket_activities.html')

# Route to a User's Public bucket activities
@app.route('/my_public_bucket_activities')
def my_public_bucket_activities():
    """ Returns all bucket activities for the logged in user """
    return render_template('my_public_bucket_activities.html')

# Route to a User's Private bucket activities
@app.route('/my_private_bucket_activities')
def my_private_bucket_activities():
    """ Returns all bucket activities for the logged in user """
    return render_template('my_private_bucket_activities.html')

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
