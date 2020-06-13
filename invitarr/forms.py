from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, RadioField
from wtforms.validators import Required

class EnvForm(FlaskForm):
    

    discord_bot_token = StringField('Discord Bot Token',
                                validators=[Required()])

    role_id =  IntegerField('Role Id',
                                validators=[Required()])

    plex_user = StringField('Plex User',
                                validators=[Required()])
    plex_pass = StringField('Plex Pass',
                                validators=[Required()])
    plex_server_name = StringField('Plex Server Name',
                                validators=[Required()])
    plex_libs = StringField('Plex Libs',
                                validators=[Required()])
    channel_id = IntegerField('Channel Id',
                                validators=[Required()])
    owner_id = IntegerField('Owner Id',
                                validators=[Required()])
    # Type
    aru_choices = [('Off', 'Off'),('On','On')]
    auto_remove_user = RadioField('Match Type',
                            choices = aru_choices,
                            validators=[Required()])

    submit = SubmitField('Save Changes')

    