import module
import os 
import sys

import numpy as np

# Add utils folder
sys.path.append('./utils')

import toolkits
import utils as ut

class face_module(module):

    def __init__(self, name, weight_path, config_path):
        self.path = weight_path
        self.name = name
        self.model_eval = None

    def load(self):
        toolkits.initialize_GPU()

        # ==> loading the pre-trained model.
        import model
        
        model_eval = model.Vggface2_ResNet50(mode="eval")

        # TODO: Add config loader and print here useful data about what`s happening

        print('Running model with next configuration'.format(self.name, self.weight_path, args.aggregation, args.loss, args.benchmark))

        if self.weight_path:
            if os.path.isfile(self.weight_path):
                self.model_eval.load_weights(self.weight_path, by_name=True)
                print('==> successfully loaded the model {}'.format(self.weight_path))
                return 0
            else:
                raise IOError('==> can not find the model to load {}'.format(self.weight_path))
                return 1 
        return 0

    def process(self, payload):
        
        num_faces = len(payload)

        im_array = np.array([ut.load_data(path=i, shape=(224, 224, 3), mode='eval') for i in payload])
        f = self.model_eval.predict(im_array, batch_size=self.conf.batch_size)
        start = c * self.conf.batch_size
        end = min((c + 1) * self.conf.batch_size, num_faces)
        face_feats[start:end] = f
        if c % 500 == 0:
            print('-> finish encoding {}/{} images.'.format(c*args.batch_size, num_faces))
        return 0