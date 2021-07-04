from typing_extensions import runtime
import flask 

class ProcessModule:

    def __init__(self):
        self.app = flask.flash(__name__)
        self.app.config["DEBUG"] = True 

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

    def start(self):
        self.app.run()