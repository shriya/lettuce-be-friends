from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project.events.models import Event
from project.events.forms import EventForm
from project.tickets.models import Ticket
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps
from datetime import datetime

events_blueprint = Blueprint(
  'events',
  __name__,
  template_folder='templates'
)

@events_blueprint.route('/', methods=['GET', 'POST'])
def index(u_id):
    host = User.query.get(u_id)
    if request.method == "POST":
        form = EventForm(request.form)
        if form.validate():
            new_event = Event(request.form['date'], request.form['location_name'], request.form['location_address'])
            host.events.append(new_event)
            db.session.add(host)
            db.session.commit()
            ticket = Ticket(user_id=u_id, event_id=new_event.id, is_host=True)
            db.session.add(ticket)
            db.session.commit()
            return redirect(url_for('events.index', u_id=host.id))
        return render_template('events/new.html', form=form, u_id=host.id)
    events = host.events
    return render_template('events/index.html', u_id=host.id, events=events, host=host)

@events_blueprint.route('/new')
def new(u_id):
    host = User.query.get(u_id)
    form = EventForm(request.form)
    return render_template('events/new.html', form=form, host=host, u_id=host.id)

@events_blueprint.route('/<int:e_id>/edit')
def edit(u_id, e_id):
    host = User.query.get(u_id)
    event = Event.query.get(e_id)
    form = EventForm(obj=event)
    return render_template('events/edit.html', form=form, host=host, u_id=host.id, e_id=event.id, event=event)

@events_blueprint.route('/<int:e_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(u_id, e_id):
    host = User.query.get(u_id)
    event = Event.query.get(e_id)
    if request.method == b"PATCH":
        form = EventForm(request.form)
        if form.validate():
            event.date = datetime.strptime(request.form['date'], '%d/%m %H:%M')
            event.location_name = request.form['location_name']
            event.location_address = request.form['location_address']
            db.session.add(event)
            db.session.commit()
            attendees = Ticket(user_id=u_id, event_id=event.id, is_host=True)
            db.session.add(event)
            db.session.commit()
            return redirect(url_for('events.index', u_id=host.id))
        return render_template('events/edit.html', form=form, u_id=host.id, host=host, e_id=event.id, event=event)
    if request.method == b"DELETE":
        db.session.delete(event)
        db.session.commit()
        return redirect(url_for('events.index', u_id=host.id))
    return render_template('events/show.html', event=event, e_id=event.id, u_id=host.id, host=host)






