import matplotlib.pyplot as plt
import cPickle
import matplotlib as mpl

from numpy import *

colorbar = ['blue', 'green', 'red', 'yellow']

def plot(data, datay):
    for ele, y in zip(data, datay):
        plt.text(ele[0], ele[1], str(y), color = colorbar[y])
    plt.xlim([-2, 2]);plt.ylim([-2, 2])

def plot_all(self, bound = 2):
    x, y = meshgrid(linspace(-bound, bound, 100),linspace(-bound, bound, 100))
    data = concatenate([x.reshape(-1, 1), y.reshape(-1, 1)], 1)
    pred = self.pred(data).reshape(x.shape)
    cmap = mpl.colors.LinearSegmentedColormap.from_list('cmap', colorbar, 256)
    plt.imshow(pred, interpolation = None, cmap = cmap)



if __name__ == '__main__':
    plot_all(1)

    size = 10000

    data = random.uniform(-2, 2, size = (size, 2))
    datay = []
    rule = 'complex'
    if rule == 'complex':
        for (x, y) in data:
            if y > -x+2 or y < -x-2:
                plt.text(x, y, 'B', color = 'black')
                datay.append(1)
            elif y < -1 and x > 1:
                plt.text(x, y, 'C', color = 'red') 
                datay.append(2)
            elif x ** 2 + y ** 2 < 1:
                plt.text(x, y, 'A', color = 'blue')
                datay.append(0)
            else:
                plt.text(x, y, 'D', color = 'green')
                datay.append(3)
    else:
        for (x, y) in data:
            if y > 0 and x > 0:
                plt.text(x, y, 'B', color = 'black')
                datay.append(1)
            elif y > 0 and x < 0:
                plt.text(x, y, 'C', color = 'red') 
                datay.append(2)
            elif y < 0 and x < 0:
                plt.text(x, y, 'A', color = 'blue')
                datay.append(0)
            else:
                plt.text(x, y, 'D', color = 'green')
                datay.append(3)
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.show()

    for i in range(4):
        print '%d: %d' % (i, datay.count(i))
       
    cPickle.dump((array(data), array(datay)), open('data.dat', 'wb'), True)
