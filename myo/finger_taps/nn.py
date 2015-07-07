from mnist_mlp import cnn
import cPickle
import theano.tensor as T
from theano import shared
import numpy as np

if __name__ == '__main__':
    x, y = cPickle.load(open('./data/data.npy', 'r')) 
    x = x.reshape(-1, 1, 8, 8)
    y = np.asarray(y, dtype ='int32') 
    print x.shape

    i = int(y.shape[0] * 0.7)
    train_x = shared(x[:i])
    train_y = shared(y[:i])
    test_x = shared(x[i:])
    test_y = shared(y[i:])

    ReLU = lambda x: T.max([x, T.zeros_like(x)], 0)

    k = cnn(dim_in = 1, size_in = x[0][0].shape, size_out = 4, 
            nkerns = [(10, (1, 3), (1, 1))], 
            nhiddens=[100, 40],
            activation=ReLU)#T.nnet.sigmoid)
    k.fit([(train_x, train_y), (test_x, test_y)], n_epochs = 1000, batch_size = 100, learning_rate = 0.0001)

