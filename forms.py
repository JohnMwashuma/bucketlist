""" This file contains all the form models used for post requests on the bucket application """
from flask_wtf import Form
from wtforms.fields import StringField, BooleanField
from wtforms.widgets import TextArea




class BucketlistForm(Form):
    """ This is a model for capturing bucket form data """
    title = StringField('title')
    description = StringField('description', widget=TextArea())
    bucket_activity_status = BooleanField('bucket_activity_status')
    bucket_activity_progress = BooleanField('bucket_activity_progress')
    


    