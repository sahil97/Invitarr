from flask import render_template, flash

from invitarr import app
from invitarr.forms import BotForm
from invitarr import configHandler

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/bot', methods=['GET', 'POST'])
def bot():
    env_form = BotForm()
    if env_form.validate_on_submit():
        try:
            configHandler.change_config_form(env_form)
            flash('Settings updated.')
        except:
            flash('Some error in updating settings')
    return render_template('bot.html', form = env_form)