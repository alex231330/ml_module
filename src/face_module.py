import os

import numpy as np

import io
from PIL import Image

# Add utils folder

import utils.toolkits as toolkits
import utils.utils as ut
from utils.conf_loader import ConfigLoader as conf_l

import tensorflow.compat.v1 as tf
from tensorflow.python.keras.backend import set_session
from tensorflow.python.keras.models import load_model

from mtcnn.mtcnn import MTCNN

class FaceModule():

    def __init__(self, name, weight_path, config_path):
        self.weight_path = weight_path
        self.name = name
        self.model_eval = None
        self.config = conf_l(config_path)
        self.ml_conf = self.config.get_section("ML")

        if len(self.ml_conf) == 0:
            print("Wrong config!")

    def load(self):
        tf.disable_v2_behavior()
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        session = tf.Session(config=config)

        # ==> loading the pre-trained model.
        # import model

        # self.model_eval = model.Vggface2_ResNet50(mode="eval")

        # TODO: Add config loader and print here useful data about what`s happening

        print('Running model with next configuration'.format(self.name, self.weight_path, self.ml_conf.get("feature_dim"),
                                                             self.ml_conf.get("batch_size")))

        path_to_load = self.ml_conf.get("weights_path")

        global graph
        global sess
        graph = tf.get_default_graph()
        sess = tf.Session()

        set_session(sess)       

        self.detector = MTCNN()

        # if os.path.isfile("C:/Users/Alex/Documents/Projects/ml_module_rest/weights/weights_old.h5"):
        #     self.model_eval = load_model(
        #         "C:/Users/Alex/Documents/Projects/ml_module_rest/weights/weights_old.h5")
        #     print('==> successfully loaded the model {}'.format(self.weight_path))
        #     return 0
        # else:
        #     raise IOError(
        #         '==> can not find the model to load {}'.format(self.weight_path))
        #     return 1
        return 0

    def process(self, payload):

        #im_array = np.array([ut.load_data(path=i, shape=(224, 224, 3), mode='eval') for i in payload])

        image = Image.open(io.BytesIO(payload))

        #im_array = np.array([ut.load_data(img=image, shape=(224, 224, 3), mode='eval')])
        with graph.as_default():
            set_session(sess)
            # preds = self.model_eval.predict(
            #     im_array, batch_size=int(self.ml_conf.get("batch_size")))

            result = self.detector.detect_faces(np.array(image))
            
            #print(ut.decode_predictions(preds))
            print(result)

        return result
