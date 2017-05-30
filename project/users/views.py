from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project.users.forms import UserForm, LoginForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps

users_blueprint = Blueprint(
  'users',
  __name__,
  template_folder='templates'
)

# def ensure_correct_user(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs.get('id') != current_user.id:
#             flash({'text': "Not Authorized", 'status': 'danger'})
#             return redirect(url_for('root'))
#         return fn(*args, **kwargs)
#     return wrapper

@users_blueprint.route('/', methods=['GET'])
def index():
    pass

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    pass

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    pass

@users_blueprint.route('/logout', methods=['GET'])
def logout():
    pass

@users_blueprint.route('/new', methods=['GET'])
def new():
    pass

@users_blueprint.route('/<int:id>/edit', methods=['GET'])
def edit(id):
    pass

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    pass










































