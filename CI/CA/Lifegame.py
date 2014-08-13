import CA
from numpy.random import binomial
import matplotlib.pyplot as plt

def life_game_rule(k):
    cur = k[len(k)/2]
    t = (k==1).sum() - cur
    return (cur == 1 and int(t==2 or t==3)) or (cur != 1 and int(t==3))

if __name__ == '__main__':
    simulator = CA.CA(binomial(1, 0.15, (20, 40)), 1, life_game_rule, circular = True)

    plt.ion()
    simulator.plot()
    raw_input('sizing')
    iter = 0
    while iter < 1000:
        plt.clf()
        simulator.update()
        simulator.plot()
        plt.draw()

