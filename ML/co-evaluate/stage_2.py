import cPickle
import ann
import theano 
import numpy
from createData import plot_all, plot
from numpy.random import choice

import matplotlib.pyplot as plt
import theano.tensor as T

def load_data(num = None):

    data, y = cPickle.load(open('data.dat', 'rb'))

    less_xx = 0
    if less_xx:
        less = min([(y==i).sum() for i in set(y)])
        count = dict(zip(set(y), [0] * len(set(y))))
        new_data, new_y = [], []
        for ele, eley in zip(data, y):
            if count[eley] >= less: continue
            count[eley] += 1

            new_data.append(ele)
            new_y.append(eley)

        data, y = numpy.array(new_data), numpy.array(new_y)

    ind = numpy.random.permutation(data.shape[0])
    data = data[ind]
    y = y[ind]

    ind = int(len(y) * 0.7)
    train_set, test_set = (data[:ind], y[:ind]), (data[ind:], y[ind:])

    plot(*test_set)
    raw_input('pause')

    def shared_dataset(data_xy, borrow=True, num = None):
        data_x, data_y = data_xy

        if num:
            data_x = data_x[:num]
            data_y = data_y[:num]

        print data_x.shape, data_y.shape

        shared_x = theano.shared(numpy.asarray(data_x,
                                 dtype=theano.config.floatX),
                                 borrow=borrow)
        shared_y = theano.shared(numpy.asarray(data_y,
                                 dtype=theano.config.floatX),
                                 borrow=borrow)
        return shared_x, T.cast(shared_y, 'int32')

#    valid_set_x, valid_set_y = shared_dataset(valid_set, num = num)
    train_set_x, train_set_y = shared_dataset(train_set, num = num)
    test_set_x, test_set_y = shared_dataset(test_set, num = num)

    rval = [(train_set_x, train_set_y), #(valid_set_x, valid_set_y),
            (test_set_x, test_set_y)]
    return rval

def plot_in_f2(self):
    plt.clf()
    pred = self.pred() 
    plot(self.x.get_value(), pred)
    plt.draw()

def plot_in_f(self):
    plt.clf()
    plot_all(self, 10)
    plt.draw()

def test():
    plt.ion()
    plt.show()

    datasets = load_data()

    cl = ann.ANN(2, 4, hiddens=[4], lmbd = 0.)
    cl.fit(datasets, lr = 0.01, batch_size = 100, n_epochs = 1000)

    print cl.get_neg_log(data, T.cast(y, 'int32')).mean()

if __name__ == '__main__':
    theano.config.exception_verbosity='high'
    plt.ion()
    plt.show()

#    test()

    data, y = cPickle.load(open('data.dat', 'rb'))
    y = numpy.asarray(y, dtype = 'int32')
    total = len(y)
    size = int(total * 0.05)
#    data, y = theano.shared(data, borrow = True), T.cast(theano.shared(y, borrow = True), 'int32')
    
    #3 generation-long memory
    memory = [[0] * total] * 3

    #random sample training sample
    ind = choice(total, size)

    cl = ann.ANN(2, 4, hiddens=[4], lmbd = 0.)

    max_iteration = 10
    iteration = 0
    while iteration < max_iteration: 
        train_set = (theano.shared(data[ind]), theano.shared(y[ind]))

        def plot_in_f2(self):
            plt.clf()
            pred = self.pred(train_set[0]) 
            plot(train_set[0].get_value(), pred)
            plt.draw()

        cl.fit((train_set, train_set), lr = 0.01, batch_size = 100, n_epochs = 300,
                plot = plot_in_f2, plot_interval = 299)

        fitness = cl.get_neg_log(data, y)
        
        #update the memory
        memory.pop(0)
        memory.append(fitness)
        #print numpy.sum(memory, 0)
        #raw_input( numpy.array(memory) )
        
        #non-weighted memory
#       p = numpy.sum(memory, 0)
#       p = p/p.sum()

        #weighted memory
        p = numpy.array(memory)
        p = p[2] + 0.5 * p[1] * 0.1 * p[0]
        p = p/p.sum()

        #resample
        ind = choice(total, size, p = p)



