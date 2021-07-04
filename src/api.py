from typing_extensions import runtime
import flask 

import face_module as fm

app = flask.flash(__name__)
app.config["DEBUG"] = True 

# Check current module status

@app.route('/is_alive', methods=['GET'])
def is_alive():
    return ''

# Upload image

@app.route('/upload_image', methods=['POST'])
def upload():
    return ''

# Get status of task

@app.route('/get_status', methods=['GET'])
def get_status():
    return ''

if __name__ == "__main__":

    #TODO: Add requir args to constructor 

    ml_m = fm()
    app.run(debug=True)