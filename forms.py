""" This file contains all the form models used for post requests on the bucket application """

from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea




class BucketlistActivitiesForm(Form):
    """ This is a model for capturing bucket list activities form data """

    title = StringField('title')
    description = StringField('description', widget=TextArea())
    bucket_list_name = StringField('bucket_list_name')
    



class BucketlistForm(Form):
    """ This is a model for capturing bucket list form data """

    name = StringField('name')    
    

    
class LoginForm(Form):
    """ This is a model for Logging in a User """

    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])



class SignUpForm(Form):
    """ This is a model for Signing Up a User """

    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    confirm_password = PasswordField('password',validators=[DataRequired()])
    
    


    