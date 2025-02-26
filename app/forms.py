# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class URLForm(FlaskForm):
    url: StringField = StringField('URL', validators=[DataRequired(message="Please fill out this field."), URL(message="Please enter a valid URL.")])
    submit: SubmitField = SubmitField('Shorten')
