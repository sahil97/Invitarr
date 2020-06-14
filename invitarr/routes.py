from flask import render_template, flash

from invitarr import app
from invitarr.forms import GeneralForm, BotForm, PlexForm
from invitarr import configHandler

@app.route('/', methods=['GET', 'POST'])
def home():
    form = GeneralForm()
    if form.validate_on_submit():
        try:
            configHandler.change_config_form(form)
            flash('Settings updated.')
        except:
            flash('Some error in updating settings')
    return render_template('index.html', form = form)

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
