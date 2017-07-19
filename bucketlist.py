from flask import Flask, render_template, url_for

app = Flask(__name__)



# Route to All Public bucket activities 
@app.route('/')
def index():
    return render_template('all_bucket__activities.html')

# Route for Creating a New Bucket activity
@app.route('/create')
def NewBucketActivity():
    return render_template('bucket_activities_form.html')

# Route to a User's all bucket activities i.e. Public and Private
@app.route('/my_bucket_activities')
def my_bucket_activities():
    return render_template('all_my_bucket_activities.html')

# Route to a User's Public bucket activities
@app.route('/my_public_bucket_activities')
def my_public_bucket_activities():
    return render_template('my_public_bucket_activities.html')

# Route to a User's Private bucket activities
@app.route('/my_private_bucket_activities')
def my_private_bucket_activities():
    return render_template('my_private_bucket_activities.html')

# Route to a User's Profile 
@app.route('/profile')
def Profile():
    return render_template('manage.html')

if __name__ == "__main__":
    app.run(debug=True)