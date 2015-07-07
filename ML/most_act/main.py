import ga3
import ga5
from cnn import *
from numpy import *
import matplotlib.pyplot as plt
import theano

cl = raw_load('mnist_cnn_raw.dat')

def fitness_f(biont):
    prob = cl.prob(biont.reshape(1,1,28,28))[0]
    return prob[1] 

def gen_f():
    return asarray(random.binomial(1, 0.5, size=(28, 28)), dtype=theano.config.floatX)

def cross_f(a, b):
    x1, x2, y1, y2 = random.randint(0, 28, size=(4,))
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            a[i, j], b[i, j] = b[i, j], a[i, j]
    return a, b

def cross_f2(a, b):
    x1, x2, y1, y2 = random.randint(0, 7, size=(4,))
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    for i in range(x1*4, x2*4+1):
        for j in range(y1*4, y2*4+1):
            a[i, j], b[i, j] = b[i, j], a[i, j]
    return a, b

def mutation_f(biont):
    times = int(28 * 28 * 0.05)
    for i in range(times):
        x1, y1 = random.randint(0, 28, size=(2,))
        biont[x1, y1] = 1 - biont[x1, y1]
    return biont
    
def plot_f(best_biont, best_child):
    plt.clf()
    plt.imshow(best_child, cmap = 'PuBu', interpolation='None', alpha=0.5) 
    plt.imshow(best_biont, cmap = 'PuRd', interpolation='None', alpha=0.5) 
    plt.draw()


if __name__ == '__main__':
    plt.ion()
    plt.show()
    plot_f(gen_f(), gen_f())
    print fitness_f(gen_f())
    raw_input('sizing')

    MyGA = ga5.GA(fitness_f, {'iter_maximum':inf}, 30, gen_f,
                        0.55, cross_f2, 0.15, mutation_f, True, plot_f, 1, lambda a,b: a>b,
                  4)
    MyGA.fit()
