from numpy import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_single(data, ax):
    ax.imshow(data, interpolation='none', cmap = cm.Greens)

def plot_eco(count, data):    
    fig, axs = plt.subplots(count, 1, sharex = True, sharey = True)
    for i in xrange(row):
        for j in xrange(col):     
            ind = random.randint(0, data.shape[0])
            plot_dig(data[ind, :], axs[i,j])

