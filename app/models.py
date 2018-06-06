# -- coding: utf-8 --

from sqlalchemy import Column, Integer, String, ForeignKey, TIME, DATETIME, TIMESTAMP, Float
from sqlalchemy.orm import relationship, backref
from app.database import Base, db_session
from flask_login import UserMixin
from app import login


class User(UserMixin, Base):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    id            = Column(Integer, primary_key=True, unique=True)
    user_name     = Column(String(15), unique=True)
    person_name   = Column(String(10))
    password_hash = Column(String(150))

    def __init__(self, id=None, user_name=None, person_name=None, password=None):
        from werkzeug.security import generate_password_hash
        self.id            = id
        self.user_name     = user_name
        self.person_name   = person_name
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User: id is %r, user_name is %r>' % (self.id, self.user_name)

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Building(Base):
    __tablename__ = 'buildings'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    building_code = Column(String(6), primary_key=True, unique=True)
    name          = Column(String(80), unique=True)

    def __init__(self, building_code=None, name=None):
        self.building_code = building_code
        self.name          = name

    def __repr__(self):
        return '<Building code: %r, name: %r>' % (self.building_code, self.name)


class LocationCategory(Base):
    __tablename__ = 'location_categories'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    id      = Column(Integer, unique=True, primary_key=True)
    name    = Column(String(20), unique=True)

    def __init__(self, id=None, name=None):
        self.id     = id
        self.name   = name

    def __repr__(self):
        return '<LocationCategory id: %r, name: %r>' % (self.id, self.name)


class Location(Base):
    __tablename__ = 'locations'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    id              = Column(Integer, unique=True, primary_key=True)
    name            = Column(String(30), unique=True)
    building_code   = Column(String(6), ForeignKey(Building.building_code), unique=True)
    category_id     = Column(Integer, ForeignKey(LocationCategory.id), unique=True)
    available_begin_weekday = Column(TIME)
    available_end_weekday   = Column(TIME)
    available_begin_weekend = Column(TIME)
    available_end_weekend   = Column(TIME)
    avg_like_score    = Column(Float)
    num_like_score    = Column(Integer)
    avg_crowded_score = Column(Float)
    num_crowded_score = Column(Integer)

    building        = relationship('Building', backref = 'locations')
    category        = relationship('LocationCategory', backref = 'locations')

    def __init__(self, id=None, name=None, code=None, category_id=None, abw=None,
                    aew=None, a_b_end=None, a_e_end=None):
        self.id             = id
        self.name           = name
        self.building_code  = code
        self.category_id    = category_id
        self.available_begin_weekday    = abw
        self.available_end_weekday      = aew
        self.available_begin_weekend    = a_b_end
        self.available_end_weekend      = a_e_end
        self.avg_like_score = 0.0
        self.num_like_score = 0
        self.avg_crowded_score = 0.0
        self.num_like_score = 0

    def __repr__(self):
        return '<Location id: %r, name: %r, building code: %r>' %(self.id, self.name, self.building_code)

    def get_avg_like_score(self):
        # from sqlalchemy.sql import func
        # result = db_session.query(func.avg(Review.like_score).label('average')) \
        #                    .filter(Review.location_id == self.id, Review.like_score != 0) \
        #                    .first()
        # if result.average:
        #     return float(result.average)
        # else:
        #     return None
        return self.avg_like_score

    def get_avg_crowded_score(self):
        # from sqlalchemy.sql import func
        # result = db_session.query(func.avg(Review.crowded_score).label('average')) \
        #                    .filter(Review.location_id == self.id, Review.crowded_score != 0) \
        #                    .first()
        # if result.average:
        #     return float(result.average)
        # else:
        #     return None
        return self.avg_crowded_score


class Slot(Base):
    """예약할 수 있는 공간의 최소 단위 (세미나실, 강의실 등)"""
    __tablename__= 'slots'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    id                  = Column(Integer, unique=True, primary_key=True)
    name                = Column(String(50), unique=True)
    location_id         = Column(Integer, ForeignKey(Location.id), unique=True)
    max_reserve_time    = Column(Integer)
    minimum_capacity    = Column(Integer)
    maximum_capacity    = Column(Integer)

    location            = relationship('Location', backref = 'slots')

    def __init__(self, id=None, name=None, location_id=None, max_reserve_time=None, minimum_capacity=None, maximum_capacity=None):
        self.id                 = id
        self.name               = name
        self.location_id        = location_id
        self.max_reserve_time   = max_reserve_time
        self.maximum_capacity   = maximum_capacity
        self.minimum_capacity   = minimum_capacity

    def __repr__(self):
        return '<Slot id: %r, name : %r>' % (self.id, self.name)


class Reservation(Base):
    """한 user가 한 slot을 예약한 항목"""
    __tablename__ = 'reservations'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    id          = Column(Integer, primary_key=True, unique=True)
    slot_id     = Column(Integer, ForeignKey(Slot.id), unique=True)
    user_id     = Column(Integer, ForeignKey(User.id), unique=True)
    begin_date  = Column(DATETIME, unique=True)
    end_date    = Column(DATETIME, unique=True)
    num_people  = Column(Integer, unique=True)
    reservation_purpose = Column(String(50))

    user        = relationship('User', backref = 'reservations')
    slot        = relationship('Slot', backref = 'reservations')

    def __init__(self, id=None, slot_id=None, user_id=None,
            begin_date=None, end_date=None, num_people=None, reservation_purpose=None):
            self.id         = id
            self.slot_id    = slot_id
            self.user_id    = user_id
            self.begin_date = begin_date
            self.end_date   = end_date
            self.num_people = num_people
            self.reservation_purpose = reservation_purpose

    def __repr__(self):
        return '<예약 ID: %r, 예약 장소: %r, 예약 시작: %s, 예약 종료: %s' %(
            self.reservation_id, self.reservation_slot, self.begin_date, self.end_date)


class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    id              = Column(Integer, primary_key=True, unique=True)
    user_id         = Column(Integer, ForeignKey(User.id), unique=True)
    location_id     = Column(Integer, ForeignKey(Location.id), unique=True)
    like_score      = Column(Integer)
    crowded_score   = Column(Integer)
    comment         = Column(String(300))
    timestamp       = Column(TIMESTAMP, unique=True)

    user            = relationship('User', backref = 'reviews')
    location        = relationship('Location', backref = 'reviews')

    def __init__(self, id=None, user_id=None, location_id=None,
            like_score=None, crowded_score=None, comment=None, timestamp=None):
            self.id             = id
            self.user_id        = user_id
            self.location_id    = location_id
            self.like_score     = like_score
            self.crowded_score  = crowded_score
            self.comment        = comment
            self.timestamp      = timestamp

    def __repr__(self):
        return '<review id: %r, like_score: %r, crowded_score: %r>' %(self.id, self.like_score, self.crowded_score)

    like_score_to_text = ('선택하지 않음', '싫어요', '보통', '좋아요')
    def get_like_score_text(self):
        try:
            return type(self).like_score_to_text[self.like_score or 0]
        except IndexError:
            return type(self).like_score_to_text[0]

    crowded_score_to_text = ('선택하지 않음', '한산함', '보통', '많음')
    def get_crowded_score_text(self):
        try:
            return type(self).crowded_score_to_text[self.crowded_score or 0]
        except IndexError:
            return type(self).crowded_score_to_text[0]