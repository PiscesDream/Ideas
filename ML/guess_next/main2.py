from cPickle import load, dump
from numpy import *

import theano
import os
from theano import shared
from ann import ANN

import string

data_size = 100000
data_len = 7 

alphabet = string.lowercase+string.uppercase+' '
alphanum = len(alphabet)
alphamap = dict( zip( alphabet, eye(alphanum)) )  


def load_data():
    data = load(open('../../Data/WikiSpider/100.dat', 'rb'))

    raw_text = reduce(lambda x, y: x + y[1], data, '')
    text = []
    pre_char = ' '
    for char in raw_text:
        if char == '\n' or char == ' ':
            if pre_char == '\n' or pre_char == ' ': 
                continue;
            else:
                char = ' '
        if char in alphabet:
            char = char.lower()
            text.append(char)
            pre_char = char
    text = ''.join(text)
    start = random.randint(2000)
    print text[start:start + 1000]
   
    return text

def sample_data(text, sample_num = data_size, data_len = data_len):
    '''
        shouldn't do the normalization here
        'cos the distribution should be the same
    '''
    x = []
    y = []
    for _ in range(sample_num):
        pos = random.randint(data_len+1, len(text))
        row = []
        for i in range(1, data_len+1):
            row.extend(alphamap[text[pos-i]])
        
        x.append(row)
        y.append(alphabet.index(text[pos]))

    x = array(x)
    y = array(y, dtype='int32')
    print 'x.shape:', x.shape 
    print 'y.shape:', y.shape 
    return x, y


def train(mode='new', train_times=100, lr=0.1, **kwargs):
    global data_len

    if mode in ['new', 'continue']:
        text = load_data()
        data = sample_data(text)
        print data[0].shape
        print data[1].shape
        l = int(data_size * 0.7)
        datasets = [(shared(data[0][:l]), shared(data[1][:l])),
                    (shared(data[0][l:]), shared(data[1][l:]))]

#ann
        theano.config.exception_verbosity='high'
        theano.config.on_unused_input='ignore'

    if mode=='new':
        cl = ANN(data_len * alphanum, alphanum, hiddens = [300, 300, 200], lmbd = 0)
        cl.fit(datasets, lr = theano.tensor.cast(lr, theano.config.floatX), n_epochs = train_times, batch_size = 200)

        dump(cl, open('save.dat', 'wb'))
    elif mode=='continue':
        try:
            os.rename('save.dat', 'origin.dat')
        except:
            pass
        cl = load(open('origin.dat','rb'))
        print cl
        cl.fit(datasets, lr = theano.tensor.cast(lr, theano.config.floatX), n_epochs = train_times, batch_size = 200)

        dump(cl, open('save.dat', 'wb'))

    elif mode=='create':
        cl = load(open('origin.dat','rb'))
        create(**kwargs)

    return cl

def translate(vector):
    return int2char[vector.argmax()]

def create(predictor = None, text_len = 300):
    text = []
    random_start = '    pyt'#''.join(random.choice(list(alphabet), 5))
    print 'random_start: [%s]' % random_start

    cur = map(lambda x: alphamap[x], random_start)
    for _ in range(text_len):
        x = array(cur).reshape(1, -1) 
        p = predictor(x)
        #y = random.choice(list(alphabet), p = p)
        y = alphabet[p.argmax()]
        
        cur.pop(0)
        cur.append(alphamap[y])
        
        text.append(y)

    print ''.join(text)
    return text

if __name__ == '__main__':
#    train('new', lr=1, train_times=10)
#    train('continue', lr=0.1, train_times=10)

    cl = load(open('save.dat', 'rb'))
    def ann_predictor(v):
        return cl.prob(v)[0]

    train('create', predictor=ann_predictor)


