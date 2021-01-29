import configparser
import os


class AppConfig:

    def __init__(self):
        """ Initialise the object """

        self.__default = False
        self.__config = configparser.ConfigParser()
        self.__config_path = os.path.join(os.getcwd(), 'config.cfg')

        if not self.__check_config():
            self.__build_empty_config()
        else:
            self.__load_config()

    def __check_config(self):
        """ Check for config file """
        if not os.path.exists(self.__config_path):
            return False
        else:
            return True

    def __build_empty_config(self):
        """ Build an empty config file"""

        self.__config.add_section('IN_OUT')
        self.__config['IN_OUT']['source'] = 'Set Source Directory'
        self.__config['IN_OUT']['destination'] = 'Set Destination Directory'
        self.__save_config()

        self.__is_dirty = False
        self.__default = True

    def __save_config(self):
        with open(os.path.join(os.getcwd(), 'config.cfg'), 'w') as configfile:
            self.__config.write(configfile)

    def __load_config(self):
        self.__config.read(self.__config_path)

    @property
    def source(self):
        return self.__config['IN_OUT']['source']

    @source.setter
    def source(self, src):
        self.__config['IN_OUT']['source'] = src
        self.__save_config()

    @property
    def destination(self):
        return self.__config['IN_OUT']['destination']

    @destination.setter
    def destination(self, dest):
        self.__config['IN_OUT']['destination'] = dest
        self.__save_config()

    @property
    def is_default(self):
        return self.__default

    def get_value(self, key, value):
        if self.__config.has_option(key, value):
            return self.__config[key][value]
        else:
            print(key, value)
            return 'ERROR'

    def save_folder(self, option, value):
        if not self.__config.has_section('FOLDERS'):
            self.__config.add_section('FOLDERS')
        self.__config['FOLDERS'][option] = value
        self.__save_config()

    @property
    def get_folders(self):
        if self.__config.has_section('FOLDERS'):
            return list(self.__config.items('FOLDERS'))
        else:
            return ''
