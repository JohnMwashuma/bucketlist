from flask_wtf import Form
from wtforms.fields import StringField, BooleanField
from wtforms.widgets import TextArea


class BucketlistForm(Form):
    title = StringField('title')
    description = StringField('description', widget=TextArea())
    wish_status = BooleanField('wish_status')
    wish_progress = BooleanField('wish_progress')
    