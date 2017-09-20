from prj.sql import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
import datetime


class User(Base):
    __tablename__ = "User"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, default='')
    phone = Column('phone', String, default='')
    password = Column('password', String, default='')


    def __init__(self, name, phone='', password=''):
        self.name = name
        self.phone = phone
        self.password = password

    def __repr__(self):
        return "<User('%s')>" % self.name
