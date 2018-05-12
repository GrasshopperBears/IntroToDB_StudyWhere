from sqlalchemy import *
from app.database import Base

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    username = Column(String(50), primary_key=True, unique=True)
    email = Column(String(120))
    password = Column(String(50), unique=True)
    create_time = Column(TIMESTAMP)

    def __init__(self, name=None, email=None, password=None, create_time=None):
        self.username = name
        self.email = email
        self.password = password
        self.create_time = create_time

    def __repr__(self):
        return '<User %r>' % (self.username)