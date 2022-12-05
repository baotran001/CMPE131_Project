from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm, EmptyForm, HomeForm, RegisterForm, EditForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from app import db
from flask import url_for
from flask import request

@myapp_obj.route('/private')
@login_required
def private():
    return 'Hi this is a private page'

@myapp_obj.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@myapp_obj.route('/', methods=['POST', 'GET'])
def login():
    #Checks if user is logged in already
    if current_user.is_authenticated:
        return redirect(url_for('home', username=current_user.username))

    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/')

        # login user
        #REMEMBER ME DOES NOT WORK
        login_user(user, remember=current_form.remember_me.data)
        flash('quick way to debug')
        flash('another quick way to debug')
        #print(current_form.username.data, current_form.password.data)

        msg = current_form.username.data, current_form.password.data
        flash(msg)
        return redirect(url_for('home', username=current_form.username.data))
    login_page_message = 'Sign In'
    return render_template('login.html', login_page_message=login_page_message, form=current_form)

@myapp_obj.route('/user/<username>')
@login_required
def user(username):

    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts, form=form)

#Cathleen
@myapp_obj.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} does not exist!'.format(username))
            return redirect(url_for('base'))     # fix url for?
        if user == current_user:
            flash('Unable to follow yourself...')
            return redirect(url_for('user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash('You are following {}!'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('base')) # fix url for?

#Cathleen
@myapp_obj.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        if user is None:
            flash('User {} not found.'.format(username))
            return redirect(url_for('base')) # fix url for?
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash('You are not following {}.'.format(username))
        return redirect(url_for('user', username=username))
    else:
        return redirect(url_for('base')) # fix url for?


#Baotran
@myapp_obj.route('/user/<username>/home', methods=['POST', 'GET'])
@login_required
def home(username):
    current_form = HomeForm()
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('home.html', user=user, form=current_form)

#Baotran
@myapp_obj.route('/user/<username>/setting', methods=['POST', 'GET'])
@login_required
def edit(username):
    user = User.query.filter_by(username=username).first_or_404()
    current_form = EditForm()
    flash(current_form.validate_on_submit())
    if current_form.validate_on_submit():
        if not User.check_password(user,current_form.confirmPassword.data):
            flash('Invalid password!')
            return redirect(url_for('setting', username=username))
        if len(current_form.username.data) != 0 :
            user.set_username(current_form.username.data) 
            flash('Successfully changed username')
            db.session.commit()
        if len(current_form.password.data) != 0:
            user.set_password(current_form.password.data)
            flash('Successfully changed password')
            db.session.commit()
        return redirect(url_for('login'))
    return render_template('edit.html', user=username, form=current_form)


#Baotran
@myapp_obj.route('/register', methods=['POST', 'GET'])
def register():
    #checks if user is logged in (true) or no (false)
    if current_user.is_authenticated:
        return redirect(url_for('home', current_user.username))
    current_form = RegisterForm()
    #checks if data was accepted by all field validators when submitted
    if current_form.validate_on_submit():
        user = User(username=current_form.username.data)
        user.set_password(current_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!')
        return redirect(url_for('login'))
    return render_template('register.html', form=current_form)

#Baotran
@myapp_obj.route('/user/<username>/userProfile')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('profile.html', user=user)

#Baotran
@myapp_obj.route('/user/<username>/followers')
@login_required
def followers(username):
    return render_template('followers.html')

#Baotran
@myapp_obj.route('/user/<username>/message')
@login_required
def privateMessage(username):
    return render_template('message.html')

