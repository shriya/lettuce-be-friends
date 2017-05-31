from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project.users.forms import UserForm, LoginForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps

events_blueprint = Blueprint(
  'events',
  __name__,
  template_folder='templates'
)

@events_blueprint.route('/', methods=['GET', 'POST'])
def index():
    pass

@events_blueprint.route('/new')
def new():
    pass

@events_blueprint.route('/<int:e_id>/edit')
def edit(e_id):
    pass

@events_blueprint.route('/<int:e_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(e_id):
    pass