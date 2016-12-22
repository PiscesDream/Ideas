from keras.layers import Input, Dense
from keras.models import Model
import keras
from keras import regularizers

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

keras.backend.theano_backend._set_device('dev1')

# this is the size of our encoded representations
encoding_dim = 16 # 32 floats -> compression of factor 24.5, assuming the input is 784 floats

def plot_encode_decode(encoder, decoder, x_test):
    # encode and decode some digits
    # note that we take them from the *test* set
    encoded_imgs = encoder.predict(x_test)
    decoded_imgs = decoder.predict(encoded_imgs)

    n = 10  # how many digits we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(x_test[i].reshape(28, 28), interpolation='None')
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_imgs[i].reshape(28, 28), interpolation='None')
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.savefig('sample.pdf', dpi=600)
    print 'done'

def plot_max_activation(autoencoder):
    W = autoencoder.layers[1].get_weights()[0].swapaxes(0,1)
    np.savez_compressed('main.npz', data=W)
#   plt.clf()
#   N = 5
#   M = (encoding_dim-1)/N+1
#   plt.figure(figsize=(M, N))
#   for i in range(encoding_dim):
#       x = W[i]/np.sqrt((W[i]**2).sum())
#       ax = plt.subplot(M, N, i + 1)
#       plt.imshow(x.reshape(28, 28), interpolation='None')
#       plt.gray()
#       ax.get_xaxis().set_visible(False)
#       ax.get_yaxis().set_visible(False)
#   plt.subplots_adjust(hspace=0.0, wspace=-1.0)
#   plt.savefig('maxact.pdf')
#   pass

def sparseAE():
    input_img = Input(shape=(784,))
    # add a Dense layer with a L1 activity regularizer
    encoded = Dense(encoding_dim, activation='relu',
                    activity_regularizer=regularizers.activity_l1(10e-5))(input_img)
    decoded = Dense(784, activation='sigmoid')(encoded)
    autoencoder = Model(input=input_img, output=decoded)

    encoder = Model(input=input_img, output=encoded)
    # create a placeholder for an encoded (32-dimensional) input
    encoded_input = Input(shape=(encoding_dim, ))
    # retrieve the last layer of the autoencoder model
    decoder_layer = autoencoder.layers[-1]
    # create the decoder model
    decoder = Model(input=encoded_input, output=decoder_layer(encoded_input))
    return autoencoder, encoder, decoder

def AE():
    # this is our input placeholder
    input_img = Input(shape=(784, ))
    # "encoded" is the encoded representation of the input
    encoded = Dense(encoding_dim, activation='relu')(input_img)
    # "decoded" is the lossy reconstruction of the input
    decoded = Dense(784, activation='sigmoid')(encoded)
    # this model maps an input to its reconstruction
    autoencoder = Model(input=input_img, output=decoded)

    encoder = Model(input=input_img, output=encoded)
    # create a placeholder for an encoded (32-dimensional) input
    encoded_input = Input(shape=(encoding_dim, ))
    # retrieve the last layer of the autoencoder model
    decoder_layer = autoencoder.layers[-1]
    # create the decoder model
    decoder = Model(input=encoded_input, output=decoder_layer(encoded_input))
    return autoencoder, encoder, decoder

if __name__ == '__main__':
    autoencoder, encoder, decoder = sparseAE()
    autoencoder.compile(optimizer='adadelta', 
                        loss='binary_crossentropy')


    from keras.datasets import mnist
    import numpy as np
    (x_train, _), (x_test, _) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
    print x_train.shape
    print x_test.shape

#   autoencoder.load_weights('model.h5')
    autoencoder.fit(x_train, x_train,
                    nb_epoch=100,
                    batch_size=256,
                    shuffle=True,
                    validation_data=(x_test, x_test))
    autoencoder.save_weights('model.h5', overwrite=True)
    
#   plot_encode_decode(encoder, decoder, x_test)
    plot_max_activation(autoencoder)



