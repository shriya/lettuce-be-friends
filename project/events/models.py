from project import db, bcrypt
from flask_login import UserMixin
from datetime import datetime
from project.tickets.models import Ticket

class Event(db.Model, UserMixin):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    location_name = db.Column(db.Text)
    location_address = db.Column(db.Text)
    sold_out = db.Column(db.Boolean)
    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    host = db.relationship("User", backref='event')
    ticket_attendees = db.relationship("Ticket", back_populates="ticket_event")

    def __init__(self, date, location_name, location_address):
        self.date = datetime.strptime(date, '%d/%m %H:%M')
        self.location_name = location_name
        self.location_address = location_address

    def get_attendees(self):
        # return self.ticket_attendees.filter_by(event_id=self.id)
        return db.session.query(Ticket,User).filter(Ticket.user_id==User.id).filter(Ticket.event_id==self.id).all()






