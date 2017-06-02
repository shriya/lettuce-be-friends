from project import db, bcrypt
from flask_login import UserMixin
from datetime import datetime

class Event(db.Model, UserMixin):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    location_name = db.Column(db.Text)
    location_address = db.Column(db.Text)
    sold_out = db.Column(db.Boolean)
    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    host = db.relationship("User", backref='event')
    association_attendees = db.relationship("Association", back_populates="association_event")

    def __init__(self, date, location_name, location_address):
        self.date = datetime.strptime(date, '%d/%m %H:%M')
        self.location_name = location_name
        self.location_address = location_address

class Association(db.Model, UserMixin):

    __tablename__ = 'association'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    association_attendee = db.relationship("User", back_populates="association_events")
    association_event = db.relationship("Event", back_populates="association_attendees")
    is_host = db.Column(db.Boolean)

    def __init__(self, user_id, event_id, is_host=False):
        self.user_id = user_id
        self.event_id = event_id
        self.is_host = is_host








