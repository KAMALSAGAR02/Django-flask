from flask import Flask, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from extensions import db, login_manager
from models import User
from forms import RegistrationForm, LoginForm


# ---------------- APP CONFIG ----------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


# ---------------- ADMIN ----------------
admin = Admin(app, name='Admin Panel')
admin.add_view(ModelView(User, db.session))


# ---------------- USER LOADER ----------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------------- ROUTES ----------------
@app.route('/')
def index():
    # Redirect to home if logged in, else login
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html', name=current_user.username)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Please login.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# ---------------- CREATE DB & RUN ----------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
