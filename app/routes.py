from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm, EmptyForm, HomeForm, RegisterForm, EditForm, DeleteAccountForm, SearchBarForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from werkzeug.utils import secure_filename
import uuid as uuid
import os
from app import db
from flask import url_for
from flask import request, make_response

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
    
        #print(current_form.username.data, current_form.password.data)
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
        # if user tries to follow a nonexistent user, send user to home page
        if user is None:
            flash('User {} does not exist!'.format(username))
            return redirect(url_for('home'))
        # if user tries to follow themselves, send user to profile page    
        if user == current_user:
            flash('Unable to follow yourself...')
            return redirect(url_for('profile', username=username, form=form))
        # follows intended user and sends user to intended user's profile page
        current_user.follow(user)
        db.session.commit()
        return redirect(url_for('profile', username=username, form=form))
    else:
        return redirect(url_for('home'))
 
#Cathleen
@myapp_obj.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=username).first()
        # if user tries to unfollow a nonexistent user, send user to home page
        if user is None:
            flash('User {} does not exist!'.format(username))
            return redirect(url_for('home'))
        # if user tries to unfollow themselves, send user to profile page
        if user == current_user:
            flash('You cannot unfollow yourself!')
            return redirect(url_for('profile', username=username, form=form))
        # unfollows intended user and sends user to intended user's profile page
        current_user.unfollow(user)
        db.session.commit()
        return redirect(url_for('profile', username=username, form=form))
    else:
        return redirect(url_for('home'))

@myapp_obj.route('/user/<username>/home', methods=['POST', 'GET'])
@login_required
def home(username):
    current_form = HomeForm()
    '''
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    '''
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
        #if len(current_form.profile_picture.data)!= 0:
            #current_form.profile_picture.data.save(os.path.join(myapp_obj.config['UPLOAD_FOLDER'],current_form.profile_picture.data))
            #user.set_picture(str(uuid.uuid1()) + '_' + secure_filename(current_form.profile_picture.data))
            #flash('Successfully changed your picture')
        if len(current_form.username.data) != 0:
            user.set_username(current_form.username.data) 
            flash('Successfully changed username')
        if len(current_form.password.data) != 0:
            user.set_password(current_form.password.data)
            flash('Successfully changed password')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('edit.html', user=username, form=current_form)

#Baotran
@myapp_obj.route("/set")
@myapp_obj.route("/set/<theme>")
def set_theme(theme="light"):
    res = make_response(redirect(request.referrer))
    if theme == 'dark':
            res.set_cookie("theme","light",max_age=60*60*24*365*10)
    if theme == 'light':
            res.set_cookie("theme","light",max_age=60*60*24*365*10)
    res.set_cookie("theme", theme)
    return res
  


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
    form = EmptyForm()
    user = User.query.filter_by(username=username).first_or_404()
    num = 0
    for follower in user.followers:
        num +=1
    return render_template('profile.html', user=user, form=form, num=num)

#Baotran
@myapp_obj.route('/user/<username>/followers')
@login_required
def followers(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('followers.html', user=user)

@myapp_obj.route('/user/<username>/message')
@login_required
def privateMessage(username):
    return render_template('message.html')


#Kolby
@myapp_obj.route('/user/<username>/deleteAccount', methods=['POST', 'GET'])
@login_required
def deleteAccount(username):
    current_form = DeleteAccountForm()
    if not current_user.is_authenticated:
        flash('You are not logged in!')
        return redirect(url_for('register'))

    local_user = User.query.filter_by(username=username).first_or_404()
    if current_form.validate_on_submit():
        if User.check_password(local_user, current_form.confirmPassword.data) \
                and User.check_password(local_user, current_form.password.data):
            flash('You have deleted your account!', 'success')
            db.create_all()
            db.session.delete(local_user)
            logout_user()
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash('Invalid password!')
    return render_template('deleteAccount.html', form=current_form, user=current_user)

#Hieu
@myapp_obj.route('/user/<username>/search', methods=["POST", 'GET'])
@login_required
def search(username):
    form = SearchBarForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.search.data).first()
        if user is None:
            flash('User does not exist')
        else:
            num = 0
            for follower in user.followers:
                num += 1
            return render_template('profile.html',form=form, user=user, num=num)
    return render_template('searchPage.html',form=form, user=username)
