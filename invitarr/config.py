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


def change_config(config, key, value):
    """
    Function to change the key, value pair in config
    """
    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH)

        config.set(BOT_SECTION, key, value)
        with open('invitarr/bot/config1.ini', 'w') as configfile:
            config.write(configfile)    
    except Exception as e:
        print(e)
        print("Cannot change config.")
        
    