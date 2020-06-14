from flask import render_template, flash

from invitarr import app
from invitarr.forms import BotForm
from invitarr import config

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/bot', methods=['GET', 'POST'])
def bot():
    env_form = BotForm()
    if env_form.validate_on_submit():
        flash('Settings updated.')
        print(env_form)
    return render_template('bot.html', form = env_form)