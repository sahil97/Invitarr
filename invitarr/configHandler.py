import configparser
config = configparser.ConfigParser()

CONFIG_PATH = 'invitarr/bot/config.ini'
BOT_SECTION = 'bot_envs'

def get_config():
    """
    Function to return current config
    """
    try:
        config.read(CONFIG_PATH)
        return config
    except Exception as e:
        print(e)
        print('error in reading config')
        return None


def change_config(key, value):
    """
    Function to change the key, value pair in config
    """
    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)

        config.set(BOT_SECTION, key, str(value))
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)    
    except Exception as e:
        print(e)
        print("Cannot change config.")
        
def change_config_form(form_output):
    """
    Function to change config on the basis of form_output from web
    """
    config_keys = ['discord_bot_token', 'plex_user', 'plex_pass', 'role_id', 'plex_server_name'
                    'plex_libs', 'owner_id', 'channel_id', 'auto_remove_user']

    for key in config_keys:
        try:
            if key == 'plex_libs':
                pass
            else:
                change_config(key, form_output[key].data)
        except:
            pass