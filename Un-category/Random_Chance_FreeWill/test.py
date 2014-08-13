import test_module 
from numpy import *
import ann

def fully_unpre(bits, data_size):
    return list(random.randint(0, bits, size = (data_size)))

def biased_coin(bits, data_size, p):
    p = array(p) * 1.0 / sum(p)
    l = list(random.rand(data_size))
    q = [None] * data_size
    acc = 0
    for ind in xrange(bits):
        acc += p[ind]
        for ind2, ele2 in enumerate(l):
            if ele2 < acc:
                l[ind2] = inf
                q[ind2] = ind        
    return q


def markov_chain(bits, data_size, pmat):
    q = [random.randint(0, bits)]
    l = list(random.rand(data_size-1))
    for p in l:
        acc = 0
        for ind in xrange(bits):
            acc += pmat[q[-1]][ind]
            if p <= acc:
                q.append(ind)
                break
    return q

def random_guessor(arg):
    return random.randint(0, 2, size = (arg.shape[0]))

if __name__ == '__main__':
    print markov_chain(2, 100, [[0.9, 0.1],[0.1, 0.9]])

    #test_sys(self, fun, data_size, sample_len, bits, args = None):

    print '='*10, 'fair coin', '='*10
    test = test_module.test_sys(fully_unpre, 40, 5, 2)
    
    test.check('random_guess', random_guessor)

    ann_cl = ann.NeuralNetworkClassifier([50, 20])
    test.check('ann', ann_cl.predict, ann_cl.fit)


    print '='*10, 'biased coin', '='*10
    test = test_module.test_sys(biased_coin, 5000, 100, 2, args = [0.7, 0.3])
    
    test.check('random_guess', random_guessor)

    ann_cl = ann.NeuralNetworkClassifier([50, 20])
    test.check('ann', ann_cl.predict, ann_cl.fit)


    print '='*10, 'markov_chain', '='*10
    test = test_module.test_sys(markov_chain, 3000, 1, 2, args = [[0.5, 0.5],[0.3, 0.7]])

    test.check('random_guess', random_guessor)

    ann_cl = ann.NeuralNetworkClassifier([100, 50, 30, 20])
    test.check('ann', ann_cl.predict, ann_cl.fit)

     
