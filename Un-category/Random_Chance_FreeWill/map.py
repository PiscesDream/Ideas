import matplotlib.pyplot as plt
from numpy import * 

def f1(x, theta = 3.9):
    return theta * (1-x) * x

if __name__ == '__main__':

    times = 50
  
    x0 = 0.2
    x = list(arange(times))
    y = [x0]
    for t in xrange(times-1):
        y.append(f1(y[-1]))

    x0 = 0.201
    x2 = list(arange(times))
    y2 = [x0]
    for t in xrange(times-1):
        y2.append(f1(y2[-1]))            

    plt.plot(x, y)
    plt.plot(x2, y2, 'red')
    plt.show()
