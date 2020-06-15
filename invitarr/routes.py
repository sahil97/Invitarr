from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

from invitarr import app, db, bcrypt
from invitarr.models import User
from invitarr.forms import LoginForm, GeneralForm, BotForm, PlexForm
from invitarr import configHandler

db.create_all()

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
    return render_template('login.html', title='Login', form=form)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = GeneralForm()
    if request.method == 'GET':
        user = User.query.all()[0]
        form.username.data = user.username
        form.password.data = user.password
    elif request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.all()[0]
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            flash('Details updated.')
            return redirect(url_for('login'))
    return render_template('index.html', form=form)

@app.route('/bot', methods=['GET', 'POST'])
def bot():
    form = BotForm()
    if form.validate_on_submit():
        try:
            configHandler.change_config_form(form)
            flash('Settings updated.')
        except:
            flash('Some error in updating settings')
    return render_template('bot.html', form = form)

@app.route('/plex', methods=['GET', 'POST'])
def plex():
    form = PlexForm()
    if form.validate_on_submit():
        try:
            configHandler.change_config_form(form)
            flash('Settings updated.')
        except:
            flash('Some error in updating settings')
    return render_template('plex.html', form = form)
