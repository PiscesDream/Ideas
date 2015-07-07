from cnn_mlp import *

cl = raw_load('lines.dat')
print cl

import matplotlib.pyplot as plt
import Image as I
from numpy import *
import theano

dir = '../../Data/pics/'
#arr = array(I.open(dir+'1.JPG').resize((32, 32)).convert('L'), dtype = theano.config.floatX)
arr = array(I.open(dir+'1.JPG').convert('L'), dtype = theano.config.floatX)
l, w = arr.shape
arr = arr/256.

#   f1, ax1 = plt.subplots()
#   f2, ax2 = plt.subplots()
#   ax1.imshow(arr, cmap='gray')
#   ax2.imshow(ans[4], cmap='gray');
#   plt.show()

ans = list(theano.function([], cl.cnn_layers[0].output,
             givens={cl.x:arr.reshape(1, 1, l, w)})()[0])
ans.extend( list(theano.function([], cl.cnn_layers[1].output,
             givens={cl.x:arr.reshape(1, 1, l, w)})()[0]))

import matplotlib.pyplot as plt
for i in range(2):
    for j in xrange(5):
        axs = plt.subplot(2, 5, i*5 + j)
        axs.imshow(ans[i*5 + j], cmap = 'gray', interpolation='None')

plt.show()



#   print ans.shape
#   for i in xrange(4):
#       for j in xrange(5):
#           axs = plt.subplot(4, 5, i * 5 + j)
#           axs.imshow(ans[i * 5 + j], cmap = 'gray')

#   plt.show()
