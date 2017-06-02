from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project.users.forms import UserForm, LoginForm
from project.events.models import Event, Association
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps

users_blueprint = Blueprint(
  'users',
  __name__,
  template_folder='templates'
)

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('u_id') != current_user.id:
            flash({'text': "Not Authorized", 'status': 'danger'})
            return redirect(url_for('root'))
        return fn(*args, **kwargs)
    return wrapper

@users_blueprint.route('/', methods=['GET'])
def index():
    return render_template('users/index.html', users=User.query.all(), events=Event.query.all())

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            try: 
                new_user = User(
                    first_name = form.first_name.data,
                    last_name = form.last_name.data,
                    email = form.email.data,
                    password = form.password.data
                )
                if form.phone_number.data: 
                    new_user.phone_number = form.phone_number.data
                if form.facebook_url.data:
                    new_user.facebook_url = form.facebook_url.data
                if form.profile_img_url.data:
                    new_user.profile_img_url = form.profile_img_url.data
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
            except IntegrityError as e:
                flash({'text': "Invalid input data", 'status':'danger'})
                return render_template('users/signup.html', form=form)
        return redirect(url_for('root'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            found_user = User.query.filter_by(email = form.email.data).first()
            if found_user:
                is_authenticated = bcrypt.check_password_hash(found_user.password, form.password.data)
                if is_authenticated:
                    login_user(found_user)
                    return redirect(url_for('root'))
            flash({ 'text': "User not found.", 'status': 'danger' })
            return redirect(url_for('users.login'))
    return render_template('users/login.html', form=form)

@users_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash({ 'text': "You have successfully logged out.", 'status': 'success' })
    return redirect(url_for('users.login'))

@users_blueprint.route('/<int:u_id>/edit')
@login_required
@ensure_correct_user
def edit(u_id):
    user = User.query.get(u_id)
    form = UserForm(obj=user)
    return render_template('users/edit.html', form=form, user=user)

@users_blueprint.route('/<int:u_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(u_id):
    this_user = User.query.get(u_id)
    if request.method == b"PATCH":
        form = UserForm(request.form)
        if form.validate():
            if bcrypt.check_password_hash(this_user.password, form.password.data):
                this_user.first_name = form.first_name.data
                this_user.last_name = form.last_name.data
                this_user.email = form.email.data
                if form.phone_number.data: 
                    this_user.phone_number = form.phone_number.data
                if form.facebook_url.data:
                    this_user.facebook_url = form.facebook_url.data
                if form.profile_img_url.data:
                    this_user.profile_img_url = form.profile_img_url.data
                db.session.add(this_user)
                db.session.commit()
                return redirect(url_for('users.show', u_id=this_user.id))
        return render_template('users/edit.html', form=form, user=this_user)
    if request.method == b"DELETE":
        logout_user()
        db.session.delete(this_user)
        db.session.commit()
        flash({ 'text': "You have successfully deleted your account.", 'status': 'success' })
        return redirect(url_for('users.signup'))
    return render_template('users/index.html', users=User.query.all(), events=Event.query.all())










































