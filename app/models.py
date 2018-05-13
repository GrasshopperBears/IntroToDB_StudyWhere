# -- coding: utf-8 --

from sqlalchemy import *
from app.database import Base

class User(Base):
    __tablename__ = 'USER'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    user_id = Column(String(15), primary_key=True, unique=True)
    user_name = Column(String(10), unique = True)
    password_hash = Column(String(150), unique=True)
    
    def __init__(self, user_id = None, name=None, password=None):
        self.user_id =user_id 
        self.name = name
        self.password_hash = password

    def __repr__(self):
        return '<User: id is %r, name is %r>' % (self.user_id, self.user_name)

class Building(Base):
    __tablename__ = 'BUILDING'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    building_number = Column(String(6), primary_key=True, unique=True)
    building_name = Column(String(80), unique=True)

    def __init__(self, number=None, name=None):
        self.building_number = number
        self.building_name = name

    def __repr__(self):
        return '<Building number: %r, Buillding name: %r>' % (self.building_number, self.building_name)

class Category(Base):
    __tablename__ = 'CATEGORY'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    category_number = Column(Integer, unique=True, primary_key=True)
    type = Column(String(20), unique=True)

    def __init__(self, number= None, type = None):
        self.category_number = number
        self.category_type = type

    def __repr__(self):
        return '<CATEGORY number: %r, CATEGORY name: %r>' % (self.category_number, self.type)

class Location(Base):
    __tablename__ = 'LOCATION'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    location_number = Column(Integer, unique=True, primary_key=True)
    location_name = Column(String(30), unique=True)
    building_code = Column(String(6), ForeignKey(Building.building_number), unique=True)
    category_number = Column(Integer, ForeignKey(Category.category_number), unique=True)
    available_begin_weekday = Column(TIME)
    available_end_weekday = Column(TIME)
    available_begin_weekend = Column(TIME)
    available_end_weekend = Column(TIME)

    def __init__(self, number=None, name=None, code=None, category_number=None, abw = None,
                    aew = None, a_b_end = None, a_e_end = None):
        self.location_number = number
        self.location_name = name
        self.building_code = code
        self.category_number = category_number
        self.available_begin_weekday = abw
        self.available_end_weekday = aew
        self.available_begin_weekend = a_b_end
        self.available_end_weekend = a_e_end

    def __repr__(self):
        return '<Location_name = %r, Location_number = %r, Buildig_code = %r>' %(self.location_name, self.location_number, 
            self.building_code)


class Slottypes(Base):
    __tablename__= 'SLOTTYPES'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    slot_number = Column(Integer, unique=True, primary_key=True)
    slot_type = Column(String(30))
    maximum_capacity = Column(Integer)

    def __init__(self, slot_number=None, slot_type=None, 
        maximum_capacity=None):
        self.slot_number = slot_number
        self.slot_type = slot_type
        self.maximum_capacity = maximum_capacity
        
    def __repr__(self):
        return '<Slot type number: %r, Slot type: %r>' % (self.slot_number, self.slot_type)

class Slot(Base):
    __tablename__= 'SLOT'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    slot_id = Column(Integer, unique=True, primary_key=True)
    slot_name = Column(String(50), unique=True)
    slot_location = Column(Integer, ForeignKey(Location.location_number), unique=True)
    slot_type = Column(Integer, ForeignKey(Slottypes.slot_number), unique=True)
    max_reserve_time = Column(Integer)
    minimum_capacity = Column(Integer)
    
    def __init__(self, slot_id=None, slot_name=None, slot_location=None, 
        slot_type=None, max_reserve_time=None, minimum_capacity=None):
        self.slot_id = slot_id
        self.slot_name = slot_name
        self.slot_location= slot_location
        self.slot_type = slot_type
        self.max_reserve_time = max_reserve_time
        self.minimum_capacity = minimum_capacity

    def __repr__(self):
        return '<Slot id: %r, Slot name : %r>' % (self.slot_id, self.slot_name)

class Reservation(Base):
    __tablename__ = 'RESERVATION'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    reservation_id = Column(Integer, primary_key=True, unique=True)
    reserve_slot = Column(Integer, ForeignKey(Slot.slot_id), unique=True)
    user_id = Column(String(15), ForeignKey(User.user_id), unique=True)
    begin_date = Column(DATETIME, unique=True)
    end_date = Column(DATETIME, unique=True)
    num_people = Column(Integer, unique=True)
    reservation_purpose = Column(String(50))

    def __init__(self, reservation_id=None, reservation_slot=None, user_id=None,
            begin_date=None, end_date=None, num_people=None, reservation_purpose=None):
            self.reservation_id = reservation_id
            self.reserve_slot = reservation_slot
            self.user_id = user_id
            self.begin_date = begin_date
            self.end_date = end_date
            self.num_people = num_people
            self.reservation_purpose = reservation_purpose

    def __repr__(self):
        return '<예약 ID: %r, 예약 장소: %r, 예약 시작: %s, 예약 종료: %r' %(
            self.reservation_id, self.reservation_slot, self.begin_date, self.end_date)

class Review(Base):
    __tablename__ = 'REVIEW'
    __table_args__ = {'mysql_collate': ' utf8_general_ci'}
    review_number = Column(Integer, primary_key=True, unique=True)
    user_id = Column(String(15), ForeignKey(User.user_id), unique=True)
    location_number = Column(Integer, ForeignKey(Location.location_number), unique=True)
    like_score = Column(Integer)
    crowded_score = Column(Integer)
    comment = Column(String(300))
    timestamp = Column(TIMESTAMP, unique=True)

    def __init__(review_number=None, user_id=None, location_number=None, like_score=None,
            crowded_score=None, comment=None, timestamp=None):
            self.review_number = review_number
            self.user_id = user_id
            self.location_number = location_number
            self.like_score = like_score
            self.crowded_score = crowded_score
            self.comment = comment
            self.timestamp = timestamp

    def __repr__(self):
        return '<review number: %r, like_score: %r, crowded_score: %r>' %(
            self.review_number, self.like_score, self.crowded_score)            
