from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app
from app.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from app.database import db_session
from app.models import *
from sqlalchemy import and_


# @app.route('/static/<path:path>')
# def send_static_files(path):
#     """정적 파일(이미지, CSS, JS 등)을 제공한다."""
#     return send_from_directory('/static/', path)


@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """로그인을 위해 사용자의 ID, 비밀번호 입력을 받는다."""
    if current_user.is_authenticated:
        flash("you've already signed in.")
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name = form.user_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('login.html', title='로그인', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """새로운 회원의 가입을 처리한다."""
    if current_user.is_authenticated:
        return redirect("/")
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = User(user_name   = register_form.user_name.data,
                    person_name = register_form.person_name.data,
                    password    = register_form.password.data
                )
        db_session.add(user)
        db_session.commit()
        flash('어서오세요, {}님! 회원가입이 완료되었습니다. (ID: {})'.format(user.person_name, user.user_name))
        return redirect("/")

    return render_template('register.html', title='Register', form=register_form)


@app.route('/logout')
def logout():
    """현재 사용자를 로그아웃시킨다"""
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
    """한 공부 장소에 대한 평점과 한줄평의 목록을 보여준다."""
    location = Location.query.filter_by(id = location_id).first()

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

    return render_template('location-view.html', title=location.name, location = location, review_pagination = review_pagination)


@app.route('/locations/<location_id>/review', methods=['GET','POST'])
@login_required
def review_location(location_id):
    """한 공부 장소에 대한 평점과 한줄평을 남기거나, 기존의 평점/한줄평을 수정/삭제할 수 있다."""
    from datetime import datetime

    #user = User.query.filter_by(user_id = )

    location = Location.query.filter_by(id = location_id).first()                  #TODO 존재하지 않는 location일 경우 처리
    my_review = Review.query.filter_by(user_id = current_user.get_id(), location_id = location_id).first()

    form = ReviewForm()
    if request.method == 'POST':
        if form.submit_save.data:
            # 이미 저장한 review가 없으면 새로 생성한다.
            if not my_review:
                my_review = Review(user_id = current_user.get_id(), location_id = location_id)

            my_review.like_score    = form.like_score.data
            my_review.crowded_score = form.crowded_score.data
            my_review.comment       = form.comment.data
            my_review.timestamp     = datetime.now()
            db_session.add(my_review)
            db_session.commit()
        elif form.submit_delete:
            if my_review:
                db_session.delete(my_review)
                db_session.commit()

        return redirect(url_for('view_location', location_id = location_id))

    # 저장한 리뷰가 있으면 그 내용을 불러온다.
    if my_review:
        form.comment.data       = my_review.comment
        form.like_score.data    = str(my_review.like_score)
        form.crowded_score.data = str(my_review.crowded_score)

    return render_template('location-review.html', title=location.name, form = form)


@app.route('/locations/<location_id>/reservations')
def choose_slot_for_location(location_id):
    location = Location.query.filter_by(id = location_id).first()
    slot = Slot.query.filter_by(location_id = location.id).all()
    return render_template('location-rooms.html', title='Choose slot', location = location, slot = slot)


@app.route('/locations/<location_id>/add_reservation', methods = ['GET','POST'])
def add_reservation(location_id):
    location = Location.query.filter_by(id = location_id).first()
    slot = Slot.query.filter_by(location_id = location.id).all()
    reservation_for_slot = Reservation.query.all()
    # return render_template('reserve-room.html', title = reservation, location = location, slot = slot, reservation = reservation_for_slot)
    return render_template('home.html')


@app.route('/my_reservations', methods = ['GET','POST'])
@login_required
def my_reservations():
    my_reservations = Reservation.query.filter_by(user_id = current_user.id).all()
    return render_template('my-reservations.html', my_reservations = my_reservations)


@app.route('/reservation/<reservation_id>', methods=['GET','POST'])
@login_required
def reservation_modify(reservation_id):
    """아직 구현된 링크가 없어 임시로 홈 화면으로 가도록 설정해놓았습니다."""
    chosen_reservation = Reservation.query.filter_by(id = reservation_id).first()
    if current_user.id != chosen_reservation.user_id:
        return redirect(url_for('home'))
    return render_template('home.html')

@app.route('/locations/<location_id>/slots/<slot_id>', methods = ['GET','POST'])
@login_required
def edit_reservation(location_id, slot_id):
    import datetime
    location = Location.query.filter_by(id = location_id).first()
    slot = Slot.query.filter_by(id = slot_id).first()
    reservation_for_slot  = Reservation.query.filter_by(slot_id = slot_id).all()
    date = request.args.get('date')
    begin_time = request.args.get('begin_time')
    begin_date_string = date + ' ' + begin_time
    begin_date = datetime.datetime.strptime(begin_date_string, "%Y-%m-%d %H%M")
    reservable_time = slot.max_reserve_time
    my_reservation = Reservation.query.filter(and_(Reservation.slot_id == slot_id, Reservation.user_id == current_user.get_id(), Reservation.begin_date == begin_date)).first()

    reservation_form = ReservationForm()
    for i in range(1,slot.max_reserve_time+1):
        time_for_checking_maximum = str(int(begin_time) + i*100)
        date_string_for_checking_maximum = date + ' ' + time_for_checking_maximum
        date_for_checking_maximum = datetime.datetime.strptime(date_string_for_checking_maximum, "%Y-%m-%d %H%M")
        for j in range(len(reservation_for_slot)):
            if date_for_checking_maximum > reservation_for_slot[j].begin_date:
                reservable_time = i-1
                break


    reservation_form.group_number.choices = [(i,i) for i in range(slot.minimum_capacity, slot.maximum_capacity+1)]
    reservation_form.using_time.choices = [(i,i) for i in range(1, reservable_time+1)]

    if request.method == 'POST':
        if reservation_form.submit_save.data:
            # 이미 저장한 review가 없으면 새로 생성한다.
            end_time = str(int(begin_time) + reservation_form.using_time.data*100)
            end_time_string = date + ' ' + end_time
            end_date = datetime.datetime.strptime(end_time_string, "%Y-%m-%d %H%M")
            if not my_reservation:
                my_reservation = Reservation(slot_id = slot_id, user_id = current_user.get_id())

            my_reservation.begin_date = begin_date
            my_reservation.end_date = end_date
            my_reservation.num_people = reservation_form.group_number.data
            my_reservation.reservation_purpose = reservation_form.purpose.data
            db_session.add(my_reservation)
            db_session.commit()
            flash('예약이 성공적으로 완료되었습니다.')
            return redirect(url_for('home'))
        elif reservation_form.submit_cancel:
            return redirect(url_for('home'))

    return render_template('edit_reservation.html', title = '예약 추가 정보 입력', form = reservation_form, date = date, begin_time = begin_time, slot = slot)

