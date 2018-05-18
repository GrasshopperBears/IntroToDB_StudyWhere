from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, reviewForm, registerForm
from flask_login import current_user, login_user, logout_user, login_required
from app.database import db_session
from app.models import *
from sqlalchemy import *


@app.route('/')
def home():
    return render_template('home.html', title='Exp')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("you've already signed in.")
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_id = form.userid.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('login.html', title='Sign In', form=form)


@app.route('/review', methods=['GET', 'POST'])
@login_required
def review():
    review = reviewForm()
    if review.validate_on_submit():
        flash('Review requested for ReviewName {}, like_score={}'.format(
            review.reviewname.data, review.like_score.data))
        return redirect("/")

    return render_template('review.html', title='Review', form=review)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    register = registerForm()
    if register.validate_on_submit():
        user = User(user_id = register.userid.data,user_name=register.username.data
                , password = register.password.data)
        db_session.add(user)
        db_session.commit()
        flash(' ID: {}, 이름={} 님의 회원가입이 완료되었습니다.'.format(
            register.userid.data, register.username.data))
        return redirect("/")

    return render_template('register.html', title='Register', form=register)

@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@app.route('/location', methods=['GET','POST'])
def location():
    location = Location.search_locations_by_category(0)
    return render_template('locations.html', title='Locations', location = location)
