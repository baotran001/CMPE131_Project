from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length
from app.models import User
from flask import redirect, flash

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
     username = StringField('Username', validators=[DataRequired()])
     password = PasswordField('Password', validators=[DataRequired()])
     repeatPassword = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
     submit = SubmitField('Register')

    #checks if username is available
     def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class HomeForm(FlaskForm):
    message = StringField('enter message', validators=[DataRequired()])
    post = SubmitField('Post')

class EditForm(FlaskForm):
    dark = BooleanField('Check for dark mode')
    light = BooleanField('light mode')
    profile_picture = FileField('Profile Picture')
    username = StringField('Username')
    password = PasswordField('New Password')
    confirmPassword = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Save changes')

 
    #checks if username is available
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
            

        
    


        