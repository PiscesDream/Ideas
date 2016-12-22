from keras.layers import Input, Dense
from keras.models import Model, Sequential
import keras
from keras import regularizers
from keras.layers import Input, Dense, Convolution2D, MaxPooling2D, UpSampling2D, Flatten
from keras.utils.np_utils import to_categorical

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

keras.backend.theano_backend._set_device('dev1')

# this is the size of our encoded representations
encoding_dim = 16 # 32 floats -> compression of factor 24.5, assuming the input is 784 floats

if __name__ == '__main__':
    from keras.datasets import mnist
    import numpy as np
    (trainx, trainy), (testx, testy) = mnist.load_data()
    print trainx.shape
    print testx.shape
    trainx = trainx.reshape(-1, 1, 28, 28)
    testx  = testx.reshape(-1, 1, 28, 28)
    trainy = to_categorical(trainy)
    testy  = to_categorical(testy)

    m = Sequential([
        Convolution2D(16, 3, 3, activation='relu', input_shape=(1, 28, 28)),
        MaxPooling2D((2, 2)),
        Convolution2D(32, 3, 3, activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(500, activation='relu'),
        Dense(10, activation='softmax')
    ])
    m.compile(optimizer='adadelta',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

#   m.load_weights('model.h5')
    m.fit(trainx, trainy,
                    nb_epoch=30,
                    batch_size=300,
                    shuffle=True,
                    validation_data=(testx, testy))

    m.save_weights('model.h5', overwrite=True)
    open('model.json', 'w').write(m.to_json())

    



