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
        self.img[self.img > 0] = 1.0

    def plot(self, ax):
        self.truncate()
        ax.imshow(self.img, cmap='binary', interpolation = 'None')

    def line(self, p1, p2, color, widthx = 2, widthy = 2):
        delta = []
        for x in range(0, widthx+1):
            for y in range(0, widthy+1):
                delta.append((x,y))

        if abs(p1[0] - p2[0]) > abs(p1[1] - p2[1]):
            if p2[0] < p1[0]:
                p1, p2 = p2, p1
            m = (p1[1]-p2[1])*1.0/(p1[0] - p2[0])
            y = p1[1] 
            for x in range(int(p1[0]), int(p2[0])):
                for d in delta:
                    try:
                        self.img[x+d[0],int(y)+d[1]] += color
                    except:
                        pass
                y += m 
        else:
            if p2[1] < p1[1]:
                p1, p2 = p2, p1
            m = (p1[0]-p2[0])*1.0/(p1[1] - p2[1])
            x = p1[0] 
            for y in range(int(p1[1]), int(p2[1])):
                for d in delta:
                    try:
                        self.img[int(x)+d[0],int(y)+d[1]] += color
                    except:
                        pass
                x += m 


if __name__ == '__main__':
    size = 32

#   fig, ax = plt.subplots()
#   can.plot(ax)
#   plt.show()
    
    start_time = time.time()

    data = []
    datay = []
    print 'create 30000 images'
    for times in range(30000):
        edges = randint(2, 5)

        can = Canvas(zeros((size, size), dtype=int))
        for i in range(edges): 
            #can.Triangle(randint(0, 128, size=(3, 2)), 1)
            x = randint(0, size, size=(2))
            y = randint(0, size, size=(2))
            while ((x-y)**2).sum() ** .5 < size * .7:
                x = randint(0, size, size=(2))
                y = randint(0, size, size=(2))
            can.line(x, y, 1, 0, 0)

#       fig, ax = plt.subplots()
#       can.plot(ax)
#       plt.show()

        data.append(can.img.flatten())
        datay.append([edges])

    data = array(data)
    datay = array(datay)
    
    print data
    print datay


    import cPickle as p
    p.dump((data, datay), open('edges234.dat', 'wb'), True)

    print 'takes' + str(time.time() - start_time)


