from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project.events.models import Event
from project.tickets.models import Ticket
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps
from datetime import datetime

tickets_blueprint = Blueprint(
  'tickets',
  __name__,
  template_folder='templates'
)

@tickets_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        user = current_user
        e_id = 2
        # I think this is broken.  You want Event.query.all
        # also e_id is not defined. you probably want it in
        # the route that you are posting to
        event = Event.query.get(e_id)
        new_ticket = Ticket(user_id=user.id, event_id=event.id)
        user.ticket_events.append(new_ticket)
        db.session.add(user)
        db.session.commit()
        # Fixed to be url_for('tickets.index')
        return redirect(url_for('tickets.index'))

    events_list = current_user.get_attending_events()
    events = []
    for i in range(0, len(events_list)):
        events.append(events_list[i][1])
    return render_template('tickets/index.html', events=events)

# index
# GET - shows all events you're attending
# POSTING - add ticket to event

@tickets_blueprint.route('/<int:e_id>', methods=['GET', 'DELETE'])
def show(e_id):
    event = Event.query.get(e_id)
    if request.method == b"DELETE":
        found_ticket = db.session.query(Ticket).filter(Ticket.event_id==e_id).filter(Ticket.user_id==current_user.id).first()
        db.session.delete(found_ticket)
        db.session.commit()
        flash({ 'text': "You have successfully removed your ticket for this event.", 'status': 'success' })
        # This also needs to be  a url_for()
        return redirect('tickets.index')
    return render_template('tickets/show.html', event=event)

# show
# DELETE - remove ticket from event (/<int:t_id>)
