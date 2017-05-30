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

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
    # creating a new user; is this even necessary? 
        pass
    return render_template('users/index.html')

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    pass

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    pass

@users_blueprint.route('/logout', methods=['GET'])
def logout():
    pass

@users_blueprint.route('/new')
def new():
    # is this needed anymore?
    pass

@users_blueprint.route('/<int:id>/edit')
def edit(id):
    user = User.query.get(id)
    form = UserForm(obj=user)
    return render_template('users/edit.html', form=form, user=user)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    this_user = User.query.get(id)
    if request.method == b"PATCH":
        form = UserForm(request.form)
        if form.validate():
            if bcrypt.check_password_hash(this_user.password, form.password.data):
                this_user.first_name = form.first_name.data
                this_user.last_name = form.last_name.data
                this_user.email = form.email.data
                this_user.phone_number = form.phone_number.data
                this_user.facebook_url = form.facebook_url.data
                this_user.profile_img_url = form.profile_img_url.data
                db.session.add(this_user)
                db.session.commit()
                return redirect(url_for('users.show', id=id))
            flash({ 'text': "Wrong password, please try again.", 'status': 'danger'})
        return render_template('users/edit.html', form=form, user=this_user)
    if request.method == b"DELETE":
        db.session.delete(this_user)
        db.session.commit()
        return redirect(url_for('users.index'))
    return render_template('users/show.html', user=this_user)










































