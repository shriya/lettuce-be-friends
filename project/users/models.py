from project import db, bcrypt
from flask_login import UserMixin
from project.tickets.models import Ticket
from project.events.models import Event

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    phone_number = db.Column(db.String(10))
    facebook_url = db.Column(db.Text)
    profile_img_url = db.Column(db.Text)
    events = db.relationship("Event", backref='user')
    ticket_events = db.relationship("Ticket", back_populates="ticket_attendee")

    def __init__(self, first_name, last_name, email, password, phone_number='555-555-5555', facebook_url='https://www.facebook.com/', profile_img_url='http://i.imgur.com/C86jBp4.png'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.phone_number = phone_number
        self.facebook_url = facebook_url
        self.profile_img_url = profile_img_url

    def get_attending_events(self):
        return db.session.query(Ticket,Event).filter(Ticket.event_id==Event.id).filter(Ticket.user_id==self.id).all()
        # returns array of tuples with (Ticket, Event)
        # iterate [i][j]

        # self.ticket_events.filter_by(user_id=user.id)