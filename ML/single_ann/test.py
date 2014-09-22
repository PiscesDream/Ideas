from theano import function
import theano
from theano import tensor as T
from numpy import * 

class neuron(object):
    
    def __init__(self, args, w = None, active_fun = T.tanh):

        if w == None:
            self.w = asarray( random.uniform(low = -1.0,
                                        high = 1.0,
                                        size = (len(args), 1)), dtype = theano.config.floatX)
            active_fun = lambda x: x
        else:
            self.w = w
        self.x = args

        self.linout = 0
        for ind, ele in enumerate(self.x):
            self.linout += ele * self.w[ind]
        self.out = active_fun(self.linout)


if __name__ == '__main__':
    x = T.dscalar('x')

    a = neuron([x])
    c = neuron([x])
    c = neuron([c.out, x])

    temp_x = raw_input('input x:')
    f = function([], c.out, givens=({x:float(temp_x)}))
    print f()
    k = T.grad(c.out, a.w)
