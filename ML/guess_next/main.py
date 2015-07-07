from cPickle import load, dump
from numpy import *

import theano
import os
from theano import shared
from ann import ANN

char2int = {}
int2char = {}

data_size = 60000
data_len = 10
char_size = None 


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
        #if ord(char) < 127:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == ' ':
            char = char.lower()
            text.append(char)
            pre_char = char
    text = ''.join(text)
    start = random.randint(2000)
    print text[start:start + 1000]
   
    global char2int, int2char, char_size
    char_set = set(text)
    char2int = dict(zip(char_set, range(len(char_set))))
    int2char = dict(zip(range(len(char_set)), char_set))
    char_size = len(char2int)
    print char_set
    print len(text)
    return text

def sample_data(text, sample_num = 60000, data_len = 300):
    '''
        shouldn't do the normalization here
        'cos the distribution should be the same
    '''
    global char2int, int2char
    x = []
    y = []

    char_size = len(char2int)

    l = len(text)
    for i in xrange(sample_num):
        start = random.randint(0, l-data_len-1)
        lable = char2int[text[start+data_len+1]]

        content = text[start: start + data_len]
        content = map(lambda x: char2int[x], content)

        x__ = zeros( (data_len, char_size) )
        for ind, c in enumerate(content):
            x__[ind, c] = 1

        x.append(x__.flatten())
        y.append(lable)

    x = asarray(x, dtype = theano.config.floatX)
    y = asarray(y, dtype = int32).flatten()
    return x, y

def train(text, continue__ = 0):
    global data_size, data_len, char_size

    data = sample_data(text, sample_num = data_size, data_len = data_len)
    print data[0].shape
    print data[1].shape
    l = int(data_size * 0.7)
    datasets = [(shared(data[0][:l]), shared(data[1][:l])),
                (shared(data[0][l:]), shared(data[1][l:]))]

#ann
    theano.config.exception_verbosity='high'
    theano.config.on_unused_input='ignore'

    if not continue__:
        cl = ANN(data_len * char_size, char_size, hiddens = [100, 100], lmbd = 0)
        cl.fit(datasets, lr = theano.tensor.cast(2, theano.config.floatX), n_epochs = 200, batch_size = 200)

        dump(cl, open('save.dat', 'wb'))
    else:
        try:
            os.rename('save.dat', 'origin.dat')
        except:
            pass
        cl = load(open('origin.dat','rb'))
        print cl
        cl.fit(datasets, lr = theano.tensor.cast(1, theano.config.floatX), n_epochs = 100, batch_size = 200)

        dump(cl, open('save.dat', 'wb'))

def translate(vector):
    return int2char[vector.argmax()]

def create(predictor = None, text_len = 1000):
    text = []
    s = []

    for i in range(data_len):
        v = zeros((char_size,))
        word = random.randint(0, char_size)
        v[word] = 1
        text.append(v)
        s.append(int2char[word])

    for i in xrange(data_len, text_len):
        x = array(text[-data_len:]).reshape(1, -1)
        p = predictor(array(x))
        word = random.choice(range(char_size), p = p)
#        word = p.argmax()

        v = zeros((char_size,));v[word] = 1
        text.append(v)
        s.append(int2char[word])
    print ''.join(s)

if __name__ == '__main__':
    text = load_data()

    print char2int
    print int2char

    cl = load(open('save.dat', 'rb'))
    def ann_predictor(v):
        return cl.prob(v)[0]

    def knn_predictor(v, k = 20):
        x, y = sample_data(text, sample_num = 300, data_len = data_len)
        acc = zeros((char_size,))

        for x_, y_ in zip(x, y):
            acc[y_] += 1/((v - x_) ** 2).sum()

        return acc/float(acc.sum())

    #train(text)
    create(ann_predictor, 200)
