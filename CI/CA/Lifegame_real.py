import CA
from numpy.random import binomial, uniform
import matplotlib.pyplot as plt


def life_game_rule(k):
    cur = k[len(k)/2]
    t = k.sum() - cur
    if cur >= .5:
        if 2 <= t < 4:
            return 1.0
#2.0,3.0 funny pattern
        else:
            return cur/2.0
#            return cur/2.000000001
#tipping point, 2.0 -> grid, little more? no grid
    else:
        if 3 <= t < 4:
            return 1.
        else:
            return 0.

if __name__ == '__main__':
    simulator = CA.CA(binomial(1, 0.15, (40, 40)), 1, life_game_rule, circular = False)

    plt.ion()
    simulator.plot()
    raw_input('sizing')
    iter = 0
    while iter < 1000:
        plt.clf()
        simulator.update()
        simulator.plot()
        plt.draw()
#        raw_input('pause')
