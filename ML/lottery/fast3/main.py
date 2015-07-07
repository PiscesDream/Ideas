from cPickle import load
from numpy import *

a = load(open('./data_20140701001_2014103104.dat', 'r'))
#raw_input(a)
a = a.sum(1)
#raw_input(a)
random.shuffle(a)

import ann

# predict sum
def split(data, time_len):
    data = data - 3 # range from 3 to 18
                    # range from 0 to 15

    l = len(data)
    x = []
    y = []
    for i in range(l - time_len):
        cur = []
        for i_ in range(time_len):
            t = [(_ == data[i+i_] and 1) or 0 for _ in range(16)]
            cur.extend(t)
#            cur.append(t)
#            cur.append(data[i_+i])
        x.append(cur)
        y.append(data[i+time_len])
    
    print data
    x = array(x)
    y = array(y)
    print x
    print y
    return x, y

if __name__ == '__main__':
    time_len = 7

    x, y = split(a, time_len)
    ind = int(len(x) * 0.7)
    train_x = x[:ind]
    train_y = y[:ind]
    test_x = x[ind:]
    test_y = y[ind:]

    cl = ann.ANN(time_len * 16, 16, hiddens = [40, 40, 40], lmbd = 0)
    cl.fit(ann.load_data( ([train_x, train_y], [test_x, test_y]) ), lr = 1.0, n_epochs = inf)
    pass
