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
        flash("이미 로그인된 상태입니다.")
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name = form.user_name.data).first()

        if user is None:
            flash('\'{}\' 와 일치하는 사용자를 찾을 수 없습니다.'.format(form.user_name.data), 'error')
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
            flash('비밀번호가 틀렸습니다.', 'error')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('home'))
    return render_template('login.html', title='로그인', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """새로운 회원의 가입을 처리한다."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user = User(user_name   = register_form.user_name.data,
                    person_name = register_form.person_name.data,
                    password    = register_form.password.data
                )
        db_session.add(user)
        db_session.commit()
        flash('어서오세요, {}님! 회원가입이 완료되었습니다. (ID: {})'.format(user.person_name, user.user_name))
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=register_form)


@app.route('/logout')
def logout():
    """현재 사용자를 로그아웃시킨다"""
    logout_user()
    return redirect(url_for('home'))


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


@app.route('/locations/<location_id>/slots', methods = ['GET','POST'])
def view_location_slots(location_id):
    """공부 장소 내의 세미나실의 예약 상태를 조회한다."""
    from datetime import date, datetime, timedelta

    """ 수정 시의 에약을 삭제하기 위해 구현한 부분입니다."""
    begin_date = request.args.get('begin_date')
    slot_id = request.args.get('slot_id')
    if begin_date and slot_id:
        my_reservation = Reservation.query.filter(and_(Reservation.begin_date == begin_date, Reservation.slot_id == slot_id, Reservation.user_id == current_user.get_id())).first()
        flash('기존 예약이 삭제되었습니다. 새로운 예약을 진행해주세요.')
        db_session.delete(my_reservation)
        db_session.commit()


    def datetimerange(begin, end, step_minutes):
        begin_minutes = round((begin.hour * 60 + begin.minute) / step_minutes) * step_minutes
        dt = begin.replace(hour = begin_minutes // 60, minute = begin_minutes % 60, second = 0, microsecond = 0)
        delta = timedelta(minutes = step_minutes)
        while dt < end:
            yield dt
            dt = dt + delta

    form = SlotDateForm()
    if not form.date.data:
        form.date.data = date.today()

    current_date = form.date.data

    location = Location.query.filter_by(id = location_id).first()

    #주중/주말에 따른 예약 가능 시간대를 확인한다.
    if current_date.weekday == 5 or current_date.weekday == 6:
        available_begin = location.available_begin_weekend
        available_end   = location.available_end_weekend
    else:
        available_begin = location.available_begin_weekday
        available_end   = location.available_end_weekday

    #예약 가능한 시간대를 datetime 형식으로 변환한다
    available_begin = datetime.combine(current_date, available_begin)
    available_end   = datetime.combine(current_date, available_end)

    SEGMENT_SIZE = app.config['RESERVATION_SEGMENT_SIZE']

    for slot in location.slots:
        segments = dict()

        for dt in datetimerange(available_begin, available_end, SEGMENT_SIZE):
            segments[dt] = { 'is_reserved': False }

        #예약 가능한 시간대에 놓인 예약 항목을 불러온다
        reservations = Reservation.query \
            .filter(Reservation.slot_id == slot.id) \
            .filter(Reservation.begin_date < available_end) \
            .filter(Reservation.end_date > available_begin) \
            .all()

        for reservation in reservations:
            for dt in datetimerange(reservation.begin_date, reservation.end_date, SEGMENT_SIZE):
                if dt in segments:
                    segments[dt]['is_reserved'] = True
                    segments[dt]['person_name'] = reservation.user.person_name

        if segments:
            slot.segments = segments

    return render_template('location-slots.html', title = location.name + ' 예약하기',
        slots = location.slots, form = form)


@app.route('/my_reservations', methods = ['GET','POST'])
@login_required
def my_reservations():
    my_reservations = Reservation.query.filter_by(user_id = current_user.id).all()
    return render_template('my-reservations.html', title = 'My Reservation', my_reservations = my_reservations)


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
    my_reservation = Reservation.query.filter(and_(Reservation.slot_id == slot_id, Reservation.user_id == current_user.get_id())).first()
    if not my_reservation:
                my_reservation = Reservation(slot_id = slot_id, user_id = current_user.get_id())
    else:
        flash('하루에 예약은 한 건만 가능합니다. 기존에 있는 예약을 확인해주세요.')
        return redirect(url_for('home'))

    """time string을 만들기 위해 사용할 것입니다."""
    def timemaker(time):
        if time == 0:
            return '0000'
        elif 100 <= time <= 900:
            return '0'+str(time)
        else:
            return str(time)

    reservation_form = ReservationForm()
    """시작 시간 기준으로 뒤에 얼마만큼 예약이 가능한지를 확인하여 selectField에 반영합니다."""
    for i in range(1,slot.max_reserve_time+1):
        time_for_checking_maximum = int(begin_time) + i*100
        if time_for_checking_maximum >= 2400:
            date_string_for_checking_maximum = date + ' ' + timemaker(time_for_checking_maximum-2400)
            date_for_checking_maximum = datetime.datetime.strptime(date_string_for_checking_maximum, "%Y-%m-%d %H%M")
            replace_day = date_for_checking_maximum.day + 1
            corres_month = date_for_checking_maximum.month
            if corres_month is 1 or 3 or 5 or 7 or 8 or 10 or 12:
                if replace_day > 31:
                    replace_day -= 31
                    corres_month += 1
            elif corres_month is 4 or 6 or 9 or 11:
                if replace_day > 30:
                    replace_day -= 30
                    corres_month += 1
            else:
                if replace_day > 28:
                    replace_day -= 28
                    corres_month += 1
            date_for_checking_maximum = date_for_checking_maximum.replace(month = corres_month, day = replace_day)
        else:
            date_string_for_checking_maximum = date + ' ' + timemaker(time_for_checking_maximum)
            date_for_checking_maximum = datetime.datetime.strptime(date_string_for_checking_maximum, "%Y-%m-%d %H%M")
        for j in range(len(reservation_for_slot)):
            if date_for_checking_maximum > reservation_for_slot[j].begin_date and begin_date < reservation_for_slot[j].begin_date:
                reservable_time = i-1
                break

    reservation_form.group_number.choices = [(i,i) for i in range(slot.minimum_capacity, slot.maximum_capacity+1)]
    reservation_form.using_time.choices = [(i,i) for i in range(1, reservable_time+1)]

    if request.method == 'POST':
        if reservation_form.submit_save.data:
            # 이미 저장한 reservation가 없으면 새로 생성한다.
            end_time_int  = int(begin_time) + reservation_form.using_time.data*100
            if end_time_int >= 2400:
                end_time_string = date + ' ' + timemaker(end_time_int-2400)
                end_date = datetime.datetime.strptime(end_time_string, "%Y-%m-%d %H%M")
                replace_day = end_date.day + 1
                corres_month = end_date.month
                if corres_month is 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    if replace_day > 31:
                        replace_day -= 31
                        corres_month += 1
                elif corres_month is 4 or 6 or 9 or 11:
                    if replace_day > 30:
                        replace_day -= 30
                        corres_month += 1
                else:
                    if replace_day > 28:
                        replace_day -= 28
                        corres_month += 1
                end_date = end_date.replace(month = corres_month, day = replace_day)
            else:
                end_time_string = date + ' ' + timemaker(end_time_int)
                end_date = datetime.datetime.strptime(end_time_string, "%Y-%m-%d %H%M")
            
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

