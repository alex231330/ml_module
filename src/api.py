import ntpath
from flask import Flask, request, jsonify
import requests
import logging
import sys 
import os
import shutil


from face_module import FaceModule as fm

from  utils.conf_loader import ConfigLoader as conf_l

UPLOAD_FOLDER = './media'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

### Init flask app 
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check current module status

@app.route('/is_alive', methods=['GET'])
def is_alive():
    return ''

# Upload image

@app.route('/process_image', methods=['GET'])
def upload():
    content = request.json
    output = ""
    print(content, file=sys.stderr)
    if request.method == 'GET':
        uuid = content['uuid']
        header = {'accept': '*/*'}
        
        res = requests.get("http://185.12.125.77:8080/api/show?uuid=" + uuid , allow_redirects=True, headers=header)


        if res.ok:
            app.logger.info(res.headers)
            open('{}/img.png'.format(UPLOAD_FOLDER), 'wb').write(res.content)
            output = ml_m.process(res.content)
        else:
            return jsonify({"Result" : 1, "Description" : "Wrong UUID"})

        #TODO Add payload to process 

    return jsonify({"Result" : 0, "Description" : "OK", "Output": output})

# Get status of task

@app.route('/get_status', methods=['GET'])
def get_status():
    return ''

if __name__ == "__main__":

    #TODO: Add requir args to constructor 

    CONFIG_PATH = "config/module_conf.ini"

    cf = conf_l(CONFIG_PATH)
    ml_conf = cf.get_section("ML")
    api_conf = cf.get_section("API")

    print(ml_conf)

    ml_m = fm(api_conf.get("name"), ml_conf.get("weights_path"), CONFIG_PATH)

    result = ml_m.load()

    if result != 0:
        print("Failed to load module!")
        exit()
    else:
        print("Module loaded succesful!")
    app.run()