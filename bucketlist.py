from flask import Flask, render_template, url_for

app = Flask(__name__)

# Route to All Public Wishes 
@app.route('/')
def index():
    return render_template('allwishes.html')

# Route for Creating a New Wish
@app.route('/create')
def NewWish():
    return render_template('wish-form.html')

# Route to a User's all Wishes i.e. Public and Private
@app.route('/mywishes')
def MyWishes():
    return render_template('all-my-wishes.html')

# Route to a User's Public Wishes
@app.route('/mypublicwishes')
def MyPublicWishes():
    return render_template('public-wishes.html')

# Route to a User's Private Wishes
@app.route('/myprivatewishes')
def MyPrivateWishes():
    return render_template('private-wishes.html')

# Route to a User's Profile 
@app.route('/profile')
def Profile():
    return render_template('manage.html')

if __name__ == "__main__":
    app.run(debug=True)