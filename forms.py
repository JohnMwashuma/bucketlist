""" This file contains all the form models used for post requests on the buckelist application """
from flask_wtf import Form
from wtforms.fields import StringField, BooleanField
from wtforms.widgets import TextArea




class BucketlistForm(Form):
    """ This is a model for capturing buckelist form data """
    title = StringField('title')
    description = StringField('description', widget=TextArea())
    bucket_item_status = BooleanField('bucket_item_status')
    bucket_item_progress = BooleanField('wisbucket_item_progress')
    


    