import os
import configparser

current = os.path.dirname(__file__)
configpath = os.path.join(current, '../conf/config.ini')


class Config_util:

    def __init__(self, config_path=configpath):
        self.__config_path = config_path
        self.__conf = configparser.ConfigParser()
        self.__conf.read(self.__config_path, encoding='utf-8')

    def url_ini(self, sec, option):
        value = self.__conf.get(sec, option)
        return value

    @property
    def get_url_path(self):
        value = self.url_ini('default', 'url')
        return value


Config = Config_util()

if __name__ == '__main__':
    config_u = Config_util()
    print(config_u.get_url_path)
