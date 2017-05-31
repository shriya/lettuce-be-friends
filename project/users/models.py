from project import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    phone_number = db.Column(db.String(10), unique=True)
    facebook_url = db.Column(db.Text)
    profile_img_url = db.Column(db.Text)
    events = db.relationship('Event', backref='host', lazy='dynamic')

    def __init__(self, first_name, last_name, email, password, phone_number='555-555-5555', facebook_url='https://www.facebook.com/', profile_img_url='http://i.imgur.com/C86jBp4.png'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.phone_number = phone_number
        self.facebook_url = facebook_url
        self.profile_img_url = profile_img_url