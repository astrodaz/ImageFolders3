import configparser
import os


class AppConfig:

    def __init__(self):
        """ Initialise the object """
        if not self.__check_config():
            self.__build_empty_config()

    @staticmethod
    def __check_config(self):
        """ Check for config file """
        if not os.path.exists(os.path.join(os.getcwd(), 'config.cfg')):
            return False
        else:
            return True

    def __build_empty_config(self):
        """ Build an empty config file"""
