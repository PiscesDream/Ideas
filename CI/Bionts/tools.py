import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap as lcm
from matplotlib.colors import hex2color as h2c

def plot(data):
    plt.imshow(data, interpolation='none',
    cmap = lcm(['white', #h2c('#ffffff'), 
                'skyblue','orange',
                'green', 'red', 
                'pink']))


from numpy.random import rand    

def p_choice(p, shift = 0):
    p = map(lambda x: float(x)/sum(p), p)
    t = rand()
    acc = .0
    for ind, ele in enumerate(p):
        acc += ele
        if acc >= t:
            return ind + shift            

def sense_r2grid(sense_r, pos = [0, 0], circle = True):
    kx = []
    ky = []
    for x in xrange(-sense_r+pos[0], sense_r+1+pos[0], 1):
        for y in xrange(-sense_r+pos[1], sense_r+1+pos[1], 1):
            if x != pos[0] or y != pos[1]:
                if not circle or abs(pos[0]-x)+abs(pos[1]-y) <= sense_r:

                    kx.append(x)
                    ky.append(y)            
    return kx, ky                
