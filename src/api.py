from typing_extensions import runtime
from flask import Flask, request
import sys 

import face_module as fm

sys.path.append('utils/')

import conf_loader as conf_l

### Init flask app 
app = Flask.flash(__name__)
app.config["DEBUG"] = True 


# Check current module status

@app.route('/is_alive', methods=['GET'])
def is_alive():
    return ''

# Upload image

@app.route('/upload_image', methods=['POST'])
def upload():
    if request.method == 'POST':

        #TODO Add payload to process 

        ml_m.process("")
    return ''

# Get status of task

@app.route('/get_status', methods=['GET'])
def get_status():
    return ''

if __name__ == "__main__":

    #TODO: Add requir args to constructor 

    CONFIG_PATH = "config/module_conf.ini"
    WEIGHTS_PATH = ""

    cf = conf_l(CONFIG_PATH)
    ml_conf = cf.get("ML")
    api_conf = cf.get("API")

    ml_m = fm(api_conf.get("name"), ml_conf.get("weights_path"), CONFIG_PATH)

    result = ml_m.load()

    if result != 0:
        print("Failed to load module!")
        exit()
    else:
        print("Module loaded succesful!")
    app.run(debug=True)