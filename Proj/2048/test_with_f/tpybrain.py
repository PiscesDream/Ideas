from load import *
from _2048 import _2048
from numpy import * 

from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer, SigmoidLayer

def convolution(x, flat = False):
#    return x
    def dist(x, y):
        if x==y:
            return x
        else:
            return 0

    ans = []
    for ind in xrange(x.shape[1]):
        ele = x[:, ind].reshape(int(x.shape[0] ** .5), -1)
        addition = []
        for i in xrange(4):
            for j in xrange(4):
                if i+1 < 4:
                    addition.append( dist(ele[i, j], ele[i+1, j]))
                if j+1 < 4:
                    addition.append( dist(ele[i, j], ele[i, j+1]))
        ans.append ( list(ele.flatten())+(addition) ) 
    #    ans.append(addition)
    if flat:
        return array(ans).flatten()
    else:
        return array(ans)               

def con1(x, flat = False, ori = False):
    return convolute(x, [array([[1, -0.5]]), array([[-0.5, 1]]), array([[1], [-0.5]]), array([[-0.5], [1]])], flat, ori)

def convolute(x, con_mats, flat = False, ori = True):
    ans = []
    n, m = x.shape
    a = int(n ** 0.5)

   
    for ind in xrange(m):
        ele = x[:, ind].reshape(a, -1)
        addition = []
        for con_mat in con_mats:
            cn, cm = con_mat.shape
            for i in xrange(a - cn + 1):
                for j in xrange( a - cm + 1):
                    acc = 0
                    for i_ in xrange(cn):
                        for j_ in xrange(cm):
                            acc += ele[i + i_, j + j_] * con_mat[i_, j_];
                    addition.append( acc )
        if ori:            
            ans.append( list(ele.flatten()) + (addition) )
        else:
            ans.append(addition)
    if flat:
        return array(ans).flatten()
    else:
        return array(ans)               

def softmax_dec(board, u, d, l, r, f):
    p = f(con1(board.reshape(-1,1), flat = True))
#    print p
    if all(board == u[0]):
        p[0] = 0
    if all(board == d[0]):
        p[1] = 0
    if all(board == l[0]):
        p[2] = 0
    if all(board == r[0]):
        p[3] = 0
#    p /= p.sum()
#    return random.choice(arange(4), p = p)
    return p.argmax()

if __name__ == '__main__':
    tr_x = load('rec_board.npy')
    tr_y = load('rec_move.npy')

    tr_x = con1(tr_x.T)
    
    print tr_x.shape
    print tr_y.shape

    data = ClassificationDataSet(tr_x.shape[1], 1, nb_classes = 4)
    for ind, ele in enumerate(tr_x):
        data.addSample(ele, tr_y[ind])
    data._convertToOneOfMany()
    print data.outdim

    fnn = buildNetwork(data.indim, 10, 10, data.outdim, hiddenclass=SigmoidLayer, outclass=SoftmaxLayer )
    trainer = BackpropTrainer( fnn, dataset=data)#, momentum=0.1, verbose=True, weightdecay=0.01)   
    for i in xrange(3):
        print trainer.train()
    #trainer.trainUntilConvergence()

    game = _2048(length = 4)
    game.mul_test(100, lambda a, b, c, d, e: softmax_dec(a, b, c, d, e, f = fnn.activate), addition_arg = True)
