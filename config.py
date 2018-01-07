import os
import sys
import json


class Config:
    def __init__(self, config_file):
        self.__config_file = config_file
        self.__is_config_good = False

    def is_config_good(self):
        return self.__is_config_good

    def set_is_config_good(self, is_good):
        self.__is_config_good = is_good

    def config_file(self):
        return self.__config_file

    def set_config_file(self, config_file):
        self.__config_file = config_file

    def read_from_config_file(self):
        if os.path.isdir(self.__config_file):
            self.__is_config_good = False
            return False
        elif not os.path.isfile(self.__config_file):
            self.__is_config_good = False
            return False

        f = open(self.__config_file, 'r')
        self.__config_text = f.read()
        f.close()
        return True

class JsonConfig(Config):
    def __init__(self, config_file):
        Config.__init__(self, config_file)
        self.__json_config = {}

    def _get_content_from_exist_file(self, config_file):
        f = open(config_file, 'r')
        config_data = f.read()
        f.close()
        return config_data

    def _get_json_config(self, config_data):
        try:
            self.__json_config = json.loads(config_data)
        except Exception, e:
            print "Exception when parse json"
            self.set_is_config_good(False)
            return False

        print "get json config"
        self.set_is_config_good(True)
        return True
        
    def read_from_config_file(self):
        config_file = self.config_file()
        if os.path.isdir(config_file):
            self.set_is_config_good(False)
            return False
        elif not os.path.isfile(config_file):
            self.set_is_config_good(False)
            return False
        
        json_config = self._get_content_from_exist_file(config_file)
        if not self._get_json_config(json_config):
            self.set_is_config_good(False)
            return False

        self.set_is_config_good(True)
        return True
