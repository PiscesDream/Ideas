from numpy import exp
<<<<<<< HEAD
import matplotlib.pyplot as plt

=======
>>>>>>> c6871fc3fcda7f1717c52c8983a736ed830911cb
Default_gene = '0' * 50 + '1' * 50
Default_rep_req = 30
Growth_f = lambda x: 1.0/(1.0+exp(0.02*(-x+250)))
Growth_g = lambda x: 2.0 * Growth_f(x) * (1 - Growth_f(x))
<<<<<<< HEAD

if __name__ == '__main__':
    size = 500
    plt.plot(range(size), map(Growth_f, range(size)))
    plt.show()
=======
>>>>>>> c6871fc3fcda7f1717c52c8983a736ed830911cb
