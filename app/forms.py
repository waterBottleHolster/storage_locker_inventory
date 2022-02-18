from cgitb import enable
from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    plan = StringField('Plan', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    url = HiddenField('URL', validators=[DataRequired()])
    # url is just a formatted title: lower case and underscores instead of spaces
    description = StringField('Desc.', validators=[DataRequired()])
    submit = SubmitField('Save')

class ItemCommentsForm(FlaskForm):
    date = StringField('Date', validators=[DataRequired()])
    comment = StringField('Comment', validators=[DataRequired()])
