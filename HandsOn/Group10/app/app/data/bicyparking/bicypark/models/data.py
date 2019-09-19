#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Column, Integer, Float, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Define a base model for other database tables to inherit
class Data(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    ctime = Column(DateTime, default=func.current_timestamp())
    mtime = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())


class BicyPoint(Data):
    __tablename__ = 'bicypoint'

    address = Column(String(255),  nullable=False)
    lat = Column(Float,  nullable=False)
    lng = Column(Float,  nullable=False)

    def __init__(self, id, address, lat, lng):
        self.identifier = id
        self.address = address
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return '<BicyPoint [%f, %f]>' % (self.lat, self.lng)

