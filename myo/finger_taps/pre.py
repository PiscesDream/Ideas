import numpy as np
import cPickle
import sys 

if __name__ == '__main__':
    if len(sys.argv) == 1:
        N = 50000
        L = 10
    else:
        N, L = tuple(sys.argv[1:])

#   rawx = [[] for i in range(4)]
#   for i in range(2, 6):
#       for lines in open('./data/%dth.txt'%i):
#           rawx[i-2].append(map(float, lines.strip().split('\t')))
#       rawx[i-2] = rawx[i-2][-2000:]
#   rawx = np.array(rawx)
#   cPickle.dump(rawx, open('./data/rawx.npy', 'w')) 

    rawx = cPickle.load(open('./data/rawx.npy', 'r')) 
    print rawx.shape

    x = []
    y = []
    for _ in range(N):
        label = np.random.randint(0, 4)
        xstart = np.random.randint(0, 2000-L)
        y.append(label)
        x.append(rawx[label][xstart:xstart+L])#flatten())
    x = np.array(x)
    y = np.array(y)


    cPickle.dump((x, y), open('./data/data.npy', 'w')) 
    print 'done'
