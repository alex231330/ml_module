import configparser
import os

class ConfigLoader():

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = configparser.ConfigParser()
   
    
    def get_section(self, name):
        
        conf_dict = {}
        if os.path.isfile(self.config_path):
            self.config.read(self.config_path)

        if name in self.config:
            for key in self.config[name]:
                conf_dict[key] = self.config[name][key]
            return conf_dict
        else:
            print("Error! No such section")
            return {}
    
    