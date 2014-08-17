from numpy import array, zeros, ones
from numpy.random import randint, uniform
import time
import matplotlib.pyplot as plt

class Canvas(object):
    
    def __init__(self, raw_image):
        self.img = raw_image

    def Triangle(self, p, color, alpha=.5):
        def k(p1, p2):
            if p1[0] == p2[0]: return None
            return 1. * (p1[1]-p2[1]) / (p1[0]-p2[0])
        color = color * .5

        p = sorted(p, key = lambda x: x[0])
        p1, p2, p3 = p
        k123, k13 = k(p1, p2), k(p1, p3)
        r123, r13 = p1[1], p1[1]
        if k123 > k13:
            for x in range(p1[0], p2[0]):
                r123 += k123
                r13 += k13
                for y in range(int(r13), int(r123)):
                    try:
                        self.img[x, y] -= color
                    except:
                        pass
            k123 = k(p2, p3)
            for x in range(p2[0], p3[0]):
                r123 += k123
                r13 += k13
                for y in range(int(r13), int(r123)):
                    try:
                        self.img[x, y] -= color
                    except:
                        pass

        else:
            for x in range(p1[0], p2[0]):
                r123 += k123
                r13 += k13
                for y in range(int(r123), int(r13)):
                    try:
                        self.img[x, y] -= color
                    except:
                        pass
            k123 = k(p2, p3)
            for x in range(p2[0], p3[0]):
                r123 += k123
                r13 += k13
                for y in range(int(r123), int(r13)):
                    try:
                        self.img[x, y] -= color 
                    except:
                        pass
 
    def truncate(self):
        self.img[self.img > 1.0] = 1.0

    def plot(self, ax):
        self.truncate()
        ax.imshow(self.img, interpolation = 'None')

if __name__ == '__main__':
    can = Canvas(ones((512, 512, 3)))
    can.plot()
    plt.show()
    
    start_time = time.time()
    for i in range(100): 
        can.Triangle(randint(0, 512, size=(3, 2)), uniform(0, 1, size=(3)))
    print 'takes' + str(time.time() - start_time)
    can.plot()
    plt.show()
