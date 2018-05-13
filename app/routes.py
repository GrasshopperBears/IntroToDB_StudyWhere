from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, reviewForm, registerForm
from app.models import *


@app.route('/')
def home():
    return render_template('home2.html', title = 'CS360 Team5')


@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect("/")
    return render_template('login.html', title = 'Sign In', form= form)

@app.route('/review', methods=['GET', 'POST'])
def review():
    review = reviewForm()
    if review.validate_on_submit():
        flash('Review requested for ReviewName {}, like_score={}'.format(
            review.reviewname.data, review.like_score.data))
        return redirect("/")

    return render_template('review.html', title='Review', form=review)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register = registerForm()
    if register.validate_on_submit():
        flash(' ID: {}, 이름={} 님의 회원가입이 완료되었습니다.'.format(
            register.userid.data, register.username.data))
        return redirect("/")

    return render_template('register.html', title='Register', form=register)

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    locations = Location.query.all()
    return render_template('locations.html', title='공부할 장소 찾기',locations=locations) 