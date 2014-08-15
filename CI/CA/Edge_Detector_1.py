import CA
from numpy.random import binomial
from numpy import dot, array, zeros, log, log2
import matplotlib.pyplot as plt
import Image as I

def detector(cur_grid, arg_grid):
    '''
        based on contrast
    '''
    l = arg_grid.shape[2]
    acc = zeros(arg_grid.shape[:2])
    for i in range(l/2):
        acc += (log2(arg_grid[:, :, i]) - log(arg_grid[:, :, l-i-1])) ** 2
#alpha = .9, portation = .2 is good

    ind = acc.flatten().argsort()[::-1]
    l, w = arg_grid.shape[:2]
    bp = int(l * w * .1)
#.2 no noise, little fuzzy
    for i in range(bp):
        cur_grid[ind[i]/w, ind[i]%w] = 1.
    for i in range(bp, l * w):
        cur_grid[ind[i]/w, ind[i]%w] = 0.
    return cur_grid


if __name__ == '__main__':
    img = array(I.open('Pics/road.jpg').resize((1024, 548)).convert('L'))
    img = img/float(img.max())
    simulator = CA.CA(img, radius = 1, rule = detector, global_update = True)



    plt.ion()
    simulator.plot()
    raw_input('sizing')
    iter = 0
    while iter < 1000:
        plt.clf()
        simulator.update()
        simulator.plot()
        plt.draw()
        raw_input('pause')
