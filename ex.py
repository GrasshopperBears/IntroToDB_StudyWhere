# -- coding: utf-8 --
from app.database import db_session
from app.models import *

print(User.query.all())
print(Building.query.all())
print(Category.query.all())
print(Location.query.all())
print(Slot.query.all())
print(Slottypes.query.all())
print(Reservation.query.all())
print(Review.query.all())