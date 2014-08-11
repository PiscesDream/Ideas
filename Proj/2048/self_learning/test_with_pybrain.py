from _2048_self import _2048
from numpy import * 

from pybrain.datasets            import ClassificationDataSet
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer, SigmoidLayer

def softmax_dec(board, u, d, l, r, f):
#    print board.flatten()
    p = f(board.flatten())
#    print p
    if all(board == u[0]):
        p[0] = -1
    if all(board == d[0]):
        p[1] = -1
    if all(board == l[0]):
        p[2] = -1
    if all(board == r[0]):
        p[3] = -1
#    p /= p.sum()
#    return random.choice(arange(4), p = p)
    return p.argmax()

if __name__ == '__main__':
    data = ClassificationDataSet(16, 1, nb_classes = 4)
    fnn = buildNetwork(16, 10, 10, 4, hiddenclass=SigmoidLayer, outclass=SoftmaxLayer )

    game = _2048(length = 4, pick_rate = 0.2)
    for i in xrange(200):
        print 'Learning %02d round(s)' % i
        tr_x, tr_l = game.mul_test(10, lambda a,b,c,d,e: softmax_dec(a,b,c,d,e,f = fnn.activate), addition_arg = True)
        data.setField('input', tr_x)
        data.setField('target', tr_l.reshape(-1, 1))
        data._convertToOneOfMany()

        trainer = BackpropTrainer(fnn, dataset=data)#, momentum=0.1, verbose=True, weightdecay=0.01)
        print trainer.train()

'''
best child
-------------------------------------------------------------------------
max round: 0589 	| avr round: 215.40
max point: 8300 	| avr point: 2400.40
max block: 512
'''
