from numpy import exp
import matplotlib.pyplot as plt

Default_gene = '0' * 50 + '1' * 50
Default_rep_req = 30
Growth_f = lambda x: 1.0/(1.0+exp(0.02*(-x+250)))
Growth_g = lambda x: 2.0 * Growth_f(x) * (1 - Growth_f(x))

if __name__ == '__main__':
    size = 500
    plt.plot(range(size), map(Growth_f, range(size)))
    plt.show()
