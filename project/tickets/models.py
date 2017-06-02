from project import db, bcrypt
from flask_login import UserMixin

class Ticket(db.Model, UserMixin):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    ticket_attendee = db.relationship("User", back_populates="ticket_events")
    ticket_event = db.relationship("Event", back_populates="ticket_attendees")
    is_host = db.Column(db.Boolean)

    def __init__(self, user_id, event_id, is_host=False):
        self.user_id = user_id
        self.event_id = event_id
        self.is_host = is_host