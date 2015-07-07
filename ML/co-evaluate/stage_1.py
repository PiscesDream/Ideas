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
    #test_set
    sep = int(total * 0.7)
    train_set = (data[:sep], y[:sep])
    test_set = (theano.shared(data[sep:]), theano.shared(y[sep:]))
#    data, y = theano.shared(data, borrow = True), T.cast(theano.shared(y, borrow = True), 'int32')
    single_step = 2000

    #random sample training sample
    ind = choice(sep, size)


    def plot_in_f2(self, iteration_save=None):
        plt.clf()
        pred = self.pred(train_batch[0]) 
        plot(train_batch[0].get_value(), pred)
        if iteration_save:
            plt.savefig('./pics/iter_'+str(iteration_save)+'.jpg')
        plt.draw()

    single_train = 0
    if single_train:
        train_batch = (theano.shared(train_set[0]), theano.shared(train_set[1]))
        large = 1000
        cl = ann.ANN(2, 4, hiddens=[4], lmbd = 0.)
        cl.fit((train_batch, test_set), lr = 0.01, batch_size = 100, n_epochs = large,
                plot = plot_in_f2, plot_interval = 200)

    mode = 'inf-memory'
    
    if mode == 'normal':
        max_iteration = 20
        iteration = 0
        while iteration < max_iteration: 
            train_batch = (theano.shared(train_set[0][ind]), theano.shared(train_set[1][ind]))

            cl = ann.ANN(2, 4, hiddens=[4], lmbd = 0.)
            cl.fit((train_batch, test_set), lr = 0.01, batch_size = 100, n_epochs = single_step, 
                    plot = plot_in_f2, plot_interval = single_step)

            fitness = cl.get_neg_log(*train_set)
            p = fitness/fitness.sum()

            #resample
            ind = choice(sep, size, p = p)

    if mode == 'memory':
        #3 generation-long memory
        memory = [[0] * sep] * 2
        max_iteration = numpy.inf
        iteration = 0
        while iteration < max_iteration: 
            iteration += 1
            train_batch = (theano.shared(train_set[0][ind]), theano.shared(train_set[1][ind]))

            cl = ann.ANN(2, 4, hiddens=[4], lmbd = 0.)
            cl.fit((train_batch, test_set), lr = 0.01, batch_size = 100, 
                    n_epochs = single_step+iteration,
                    plot = plot_in_f2,
                    plot_interval = single_step+iteration)

            fitness = cl.get_neg_log(*train_set)

            #update the memory
            memory.pop(0)
            memory.append(fitness)
            #print numpy.sum(memory, 0)
            #raw_input( numpy.array(memory) )
            
            #non-weighted memory
            #p = numpy.sum(memory, 0)
            #p = p/p.sum()

            #weighted memory
            p = numpy.array(memory)
            p = p[1] + p[0] 
            p = p/p.sum()

            #resample
            ind = choice(sep, size, p = p)


    if mode == 'inf-memory':
        memory = numpy.zeros((sep, )) 
        max_iteration = numpy.inf
        iteration = 0
        while iteration < max_iteration: 
            iteration += 1
            train_batch = (theano.shared(train_set[0][ind]), theano.shared(train_set[1][ind]))

            cl = ann.ANN(2, 4, hiddens=[4], lmbd = 0.)
            cl.fit((train_batch, test_set), lr = 0.01, batch_size = 100, 
                    n_epochs = single_step+iteration,
                    plot = plot_in_f2,
                    plot_interval = single_step+iteration)

            fitness = cl.get_neg_log(*train_set)

            # normalize & memorize
            memory = memory + fitness/fitness.sum()
            memory = memory/memory.sum()

            #resample
            p = memory
            ind = choice(sep, size, p = p)




