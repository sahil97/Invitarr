from flask import render_template

from invitarr import app
from invitarr.forms import EnvForm

@app.route('/', methods=['GET'])
def home():
    env_form = EnvForm()
    return render_template('index.html', form = env_form)