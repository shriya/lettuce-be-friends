from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, Email, Length

class EventForm(FlaskForm):
    # I think you meant to switch the format.
    # Probably should be %m/%d %H:%M
    # Also it may be easier to use something like moment.js
    # on the front end to convert the string to what you're
    # expecting on the server.
    date = DateTimeField('date',  format='%d/%m %H:%M', validators=[DataRequired()])
    location_name = StringField('location_name', validators=[DataRequired()])
    location_address = StringField('location_address', validators=[DataRequired()])
