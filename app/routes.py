from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app
from app.forms import LoginForm, reviewFormOld, registerForm, LocationListFilterForm, ReviewForm
from flask_login import current_user, login_user, logout_user, login_required
from app.database import db_session
from app.models import *


# @app.route('/static/<path:path>')
# def send_static_files(path):
#     """정적 파일(이미지, CSS, JS 등)을 제공한다."""
#     return send_from_directory('/static/', path)


@app.route('/')
def home():
    return render_template('home.html', title='Home')


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
    review = reviewFormOld()
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


@app.route('/locations', methods=['GET','POST'])
def locations():
    """모든 공부 장소의 목록을 필터로 분류하여 보여준다."""
    form = LocationListFilterForm()

    locations = Location.query.all()

    return render_template('locations.html', title='Locations', form = form, locations = locations)

@app.route('/locations/<location_id>', methods=['GET','POST'])
def view_location(location_id):
    location = Location.query.filter_by(location_number = location_id).first()

    reviews_per_page = 5
    current_review = request.args.get('current_review', 0)
    review_pages = [ i for i in range(0, len(location.reviews), reviews_per_page) ]
    current_page = current_review // reviews_per_page * reviews_per_page
    review_pagination = {
        'current_review': current_review,
        'reviews_per_page': reviews_per_page,
        'pages': review_pages,
        'current_page': current_page
    }
    review_pagination['prev_page'] = max(0, current_page - reviews_per_page)
    if review_pages:
        review_pagination['next_page'] = min(review_pages[-1], current_page + reviews_per_page)
    else:
        review_pagination['next_page'] = 0

    return render_template('location-view.html', title=location.location_name, location = location, review_pagination = review_pagination)


@app.route('/locations/<location_id>/review', methods=['GET','POST'])
@login_required
def review_location(location_id):
    from datetime import datetime

    #user = User.query.filter_by(user_id = )

    location = Location.query.filter_by(location_number = location_id).first()                  #TODO 존재하지 않는 location일 경우 처리
    my_review = Review.query.filter_by(user_id = current_user.get_id(), location_number = location_id).first() #TODO 실제 username 사용하기
    if not my_review:
        my_review = Review(user_id = current_user.get_id(), location_number = location_id)                     #TODO 실제 username 사용하기

    form = ReviewForm()
    if request.method == 'POST':
        if form.submit_save.data:
            my_review.like_score    = form.like_score.data
            my_review.crowded_score = form.crowded_score.data
            my_review.comment       = form.comment.data
            my_review.timestamp     = datetime.now()
            my_review.review_number = 2                                                         #TODO Use new review number
            db_session.add(my_review)
            db_session.commit()
        elif form.submit_delete:
            db_session.delete(my_review)
            db_session.commit()

        return redirect(url_for('view_location', location_id = location_id))
    
    form.comment.data       = my_review.comment
    form.like_score.data    = str(my_review.like_score)
    form.crowded_score.data = str(my_review.crowded_score)

    return render_template('location-review.html', title=location.location_name, form = form)


@app.route('/locations/<location_id>/reservations')
def choose_slot_for_location(location_id):
    location = Location.query.filter_by(location_number = location_id).first()
    slot = Slot.query.filter_by(slot_location = location.location_number).all()
    return render_template('location-rooms.html', title='Choose slot', location = location, slot = slot)

@app.route('/locations/<location_id>/add_reservation', methods = ['GET','POST'])
def add_reservation(location_id):
    location = Location.query.filter_by(location_number = location_id).first()
    slot = Slot.query.filter_by(slot_location = location.location_number).all()
    reservation_for_slot = Reservation.query.filter_by(reserve_slot = slot.slot_id).all()
    return render_template('reserve-room.html', title = reservation, location = location, slot = slot, reservation = reservation_for_slot)

@app.route('/my_reservations', methods = ['GET','POST'])
@login_required
def my_reservations():
    my_reservations = Reservation.query.filter_by(user_id = current_user.user_id).all()
    return render_template('my-reservations.html', my_reservations = my_reservations)

@app.route('/reservation/<reservation_id>', methods=['GET','POST'])
@login_required
def reservation_modify(reservation_id):
    chosen_reservation = Reservation.query.filter_by(reservation_id = reservation_id).first()
    if current_user.user_id != chosen_reservation.user_id:
        return redirect("/")
    return redirect("/")