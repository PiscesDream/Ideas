from keras.models import model_from_json
from keras.utils.np_utils import to_categorical
import keras
keras.backend.theano_backend._set_device('dev1')

from keras.datasets import mnist
import numpy as np
(trainx, trainy), (testx, testy) = mnist.load_data()
print trainx.shape
print testx.shape
trainx = trainx.reshape(-1, 1, 28, 28)
testx  = testx.reshape(-1, 1, 28, 28)
trainy = to_categorical(trainy)
testy  = to_categorical(testy)

def sigmoid(x):
    return 1./(1.+np.exp(-x))

def binary(x):
    return np.sign(x)

if __name__ == '__main__':
    m = model_from_json(open('modified.json').readline())
    m.load_weights('modified.h5')
    print 'loaded'

#   w, b = m.layers[2].get_weights()
#   m.layers[2].set_weights([binary(w), b])
#   m.layers[2].trainable = False

#   import ipdb
#   ipdb.set_trace()

    m.compile(optimizer='adadelta',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    m.fit(trainx, trainy, batch_size=1000, verbose=1)

    m.save_weights('modified.h5', overwrite=True)
    open('modified.json', 'w').write(m.to_json())
