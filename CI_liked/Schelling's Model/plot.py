import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap as lcm
from matplotlib.colors import hex2color as h2c
from numpy import *

def plot(data):
    plt.imshow(data, interpolation='none') 
#    cmap = lcm(['white', #h2c('#ffffff'), 
#                'skyblue','orange',
#                'green', 'red', 
#                'pink']))

if __name__ == '__main__':
#    plot([[[0.1,0.3,0.3],[0.3,0.2,0.1],[0.3,0.3,0.2]],[[0.1,0.3,0.3],[0.2,0.2,0.2],[0.4,0.3,0.1]],[[0.2,0.3,0.1],[0.1,0.2,0.2],[0.1,0.2,0.1]]])
    a = random.rand(2,2,4)
    for i in a:
        for j in i:
            j[3] = 1
    print a[0][0] 
    plot(a)            
    plt.show()
