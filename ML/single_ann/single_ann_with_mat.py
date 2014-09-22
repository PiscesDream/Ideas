'''
    realize with matrix
'''

import theano
import theano.tensor as T
from theano import function, grad
from numpy import *
from ga import GA

class neuron_map(object):
    
    def __init__(self, num = 20, density=0.5, input, output):
        
        w_value = asarray(random.uniform(-1, 1, size = (num, num)), dtype=theano.config.floatX)
        b_value = asarray(random.uniform(-1, 1, size = (num)), dtype=theano.config.floatX)
        act_value = asarray(random.binomial(n=1, p=density, 1, size = (num, num)), dtype=theano.config.floatX)

        w = theano.shared(value=w_value, borror=True)
        b = theano.shared(value=b_value, borrow=True)
        neurons = T.dvector('neurons')
        neurons[0] = input
        for ind in range(1, num):
            neurons[ind] = 
        '''
            stuck here, how to implement a recursive one??
        '''
        


