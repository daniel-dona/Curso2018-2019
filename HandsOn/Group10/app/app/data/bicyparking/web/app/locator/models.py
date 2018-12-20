# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    ctime = db.Column(db.DateTime, default=db.func.current_timestamp())
    mtime = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# Define a User model
class BicyPoint(Base):

    __tablename__ = 'bicypoint'

    address = db.Column(db.String(255),  nullable=False)
    lat = db.Column(db.Float,  nullable=False)
    lng = db.Column(db.Float,  nullable=False)

    def __init__(self, id, address, lat, lng):
        self.identifier = id
        self.address = address
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return '<BicyPoint [%f, %f]>' % (self.lat, self.lng)

