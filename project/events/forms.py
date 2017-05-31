from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, Email, Length

class EventForm(FlaskForm):
    date = DateTimeField('date',  format='%d/%m %H:%M', validators=[DataRequired()])
    location_name = StringField('location_name', validators=[DataRequired()])
    location_address = StringField('location_address', validators=[DataRequired()])