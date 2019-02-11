from configparser import ConfigParser

# инициализация парсера конфигов
config_path = 'app/setting/config.ini'
config = ConfigParser()
config.read(config_path)

# получение параметров
MAX_BALANCE = config['transfer']['MAX_BALANCE']

