import Image as I
from numpy import *

import ann

import theano
import theano.tensor as T

import matplotlib.pyplot as plt

def matrix():
    im = I.open('./1.JPG').convert('L').resize((252, 142))

    hid1 = 20
    hid2 = 20
    hid3 = 20
    lr = 0.001

    X = array(im)/256.
    W1 = theano.shared(random.uniform(-1, 1, size=(X.shape[1], hid1)))
    W2 = theano.shared(random.uniform(-1, 1, size=(hid1, hid2)))
    W3 = theano.shared(random.uniform(-1, 1, size=(hid2, hid3)))

    Y1 = T.nnet.sigmoid( theano.dot(X, W1) )
    Y2 = T.nnet.sigmoid( theano.dot(Y1, W2) )
    Y3 = T.nnet.sigmoid( theano.dot(Y2, W3) )
    Y4 = T.nnet.sigmoid( theano.dot(Y3, W3.T) )
    Y5 = T.nnet.sigmoid( theano.dot(Y4, W2.T) )
    Y6 = T.nnet.sigmoid( theano.dot(Y5, W1.T) )

    Z = Y6
    loss = T.sum((Z - X) ** 2)
    W1_grad = T.grad(loss, W1)
    W2_grad = T.grad(loss, W2)
    W3_grad = T.grad(loss, W3)


    test_model = theano.function([], loss)
    train_model = theano.function([], loss, updates={W1:W1-lr*W1_grad,
                                                     W2:W2-lr*W2_grad,
                                                     W3:W3-lr*W3_grad})

    plt.ion()
    plt.imshow(X, cmap='gray') 
    plt.draw()
    raw_input('pause')

    maxiter = 100
    iteration = 0
    while iteration < maxiter:
        iteration += 1
        print 'Loss:', train_model()

        new = Z.eval()
        plt.imshow(new, cmap='gray')
        plt.draw()

def test_ann():
    im = array(I.open('./1.JPG').convert('L').resize((252, 142)))
    reconstructor = ann.ANN(prod(im.shape), prod(im.shape), hiddens = [1])
    reconstructor.fit(im, lr = 0.1) 

if __name__ == '__main__':
#   matrix()
    test_ann()
