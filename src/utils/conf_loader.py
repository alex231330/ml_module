import configparser
import os
import re 

class ConfigLoader():

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = configparser.ConfigParser()

    def read(self):
        if os.path.isfile(self.config_path):
            self.config.read(self.config_path)
            return 0
        else: 
            print("Error! Specific path isn`t file!")
            return 1   

    def get_section(self, name):
        
        conf_dict = {}

        if name in self.config:
            for key in self.config[name]:
                conf_dict[key] = self.config[name][key]
            return conf_dict
        else:
            print("Error! No such section")
            return {}
    
    