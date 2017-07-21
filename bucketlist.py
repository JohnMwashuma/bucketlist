""" Routes to the project's templates and logic for CRUD """

import random
from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect,  session
from forms import BucketlistActivitiesForm, LoginForm, SignUpForm
from models import User,BucketlistActivities
from flask_moment import Moment


app = Flask(__name__)
bucketListActivities = BucketlistActivities()
user = User()


# Secret key for managing sessions
app.config['SECRET_KEY'] = '\xe0\x9c\xd0o\xc8\x11\rrF\x0e\xe3\x9a\xae\xaa\xb3E\x82\th\xa6\x11\xfcW?'


# for displaying timestamps
moment = Moment(app)


# Route to All Public Bucket List Activities 
@app.route('/index')
@app.route('/')
def index():
    """ Returns bucket list activities Templates """   

    return render_template('bucket_list_activities.html' , bucket_list_activities = bucketListActivities.get_bucket_list_activities(4),)



# Route for Creating a New Bucket List Activity
@app.route('/create', methods=['GET', 'POST'])
def create_bucket_list_activity():
    """ Returns a bucket form for creating new bucket list activities """

    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:        
        form = BucketlistActivitiesForm()
        if request.method == "POST":
            bucket_list_name=form.bucket_list_name.data
            user = get_username()
            bucket_list_activity_id=random.randint(1,100)
            title = form.title.data
            description = form.description.data            
            bucketListActivities.create_bucket_list_activities(user,bucket_list_activity_id,title, description,bucket_list_name)
            return redirect(url_for('index'))
        return render_template('bucket_list_activity_form.html', form = form,  heading = "Create a Bucket List Activity")



# Route to the bucket_list_activities edit page
@app.route('/edit_bucket_list_activities/<int:bucket_list_activity_id>', methods=['GET','POST'])
def edit_bucket_list_activities(bucket_list_activity_id):
    """ Returns a bucket form for editing a bucket list activity """

    # Retrieve a bucket list activitity based on the bucket_list_activity_id provided
    bucket_list_activity = bucketListActivities.get_bucket_list_activity(bucket_list_activity_id)


    # Fills the form with data received from the model
    form = BucketlistActivitiesForm(data=bucket_list_activity)
    if request.method == "POST": 
        bucket_list_name=form.bucket_list_name.data
        description = form.description.data
        title = form.title.data         
        bucketListActivities.edit_bucket_list_activities(bucket_list_activity_id,title,bucket_list_name, description)
        return redirect(url_for('index'))
    return render_template('bucket_list_activity_form.html', form = form, heading = "Edit a Bucket List Activity")



# Route for deleting a bucket_list_activity
@app.route('/delete_bucket_list_activity/<int:bucket_list_activity_id>', methods=['GET', 'POST'])
def delete_bucket_list_activity(bucket_list_activity_id):
    """ Deletes a bucket list activity """

    bucketListActivities.delete_bucket_list_activities(bucket_list_activity_id)      
    return redirect(url_for('index'))
    


# Route to the login page
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    """ Returns a login page """

    form = LoginForm()
    if request.method == "POST":
        if user.login_user(form.username.data,form.password.data) == True:
            session['logged_in'] = True  
            session['username'] = form.username.data         
            return redirect(url_for('index'))
    return render_template('login.html',form = form)
    


# Route to the logout page
@app.route('/logout')
def logout(): 
    """ Logs Out a User """

    session['logged_in'] = False
    return redirect(url_for('index'))


# Route to the signup page
@app.route('/signup',methods=['GET', 'POST'])
def signup():
    """ Returns a signup page """

    form = SignUpForm()
    if request.method == "POST":
        username=form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        session['username'] = form.username.data  # Assigns the username to the username session variable      
        user.register_new_user(username,password,confirm_password)        
        session['logged_in'] = True # Intializes the session
        return redirect(url_for('index'))
    return render_template('signup.html', form = form) 



def get_username():
    """ Returns the name of the logged in user """
    
    if 'username' in session:
        username = session['username']
    return username  



if __name__ == "__main__":
    app.run(debug=True)
