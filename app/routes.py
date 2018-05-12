from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, reviewForm


@app.route('/')
def home():
    return render_template('home.html', title = 'Exp')


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