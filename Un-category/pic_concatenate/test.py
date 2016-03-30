import matplotlib.pyplot as plt
import cPickle 
import numpy as np

S = 10

if __name__ == '__main__':
    size, (trainx, trainy), (testx, testy) = cPickle.load(open('../../Data/lfw/data.dat', 'r'))    
    a = np.concatenate([trainx[0], testx[0]])

    L = size[0]/S
    #a = a.reshape(a.shape[0], L, L, S, S) 
    print a.shape

    N = a.shape[0]
    x, y = np.random.randint(0, L, size=(2,))
    l = []
    vis = np.zeros((L, L), dtype=bool)
    inq = np.zeros((L, L), dtype=bool)
    inq[x, y] = True
    index = np.zeros((L, L), dtype=int)
    l.append((x, y))
    while l:
        x, y = l[0]
        l.pop(0)
        print('\n{} is extending ...'.format((x, y)))

        cost = np.zeros(N)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x+dx
            ny = y+dy
            if not (0 <= nx < L and 0 <= ny < L): continue
            if not vis[nx, ny]: continue
            print('Checking {} against {}'.format((x, y), (nx, ny)))

            ind = index[nx, ny]
            if (dx, dy) == (0, -1): # right constrains its left
                cost += ((a[:, x*S:(x+1)*S, y*S-1] - a[ind, x*S:(x+1)*S, y*S])**2).sum(1)
            if (dx, dy) == (0, 1): # left constrains its right 
                cost += ((a[:, x*S:(x+1)*S, (y+1)*S] - a[ind, x*S:(x+1)*S, (y+1)*S-1])**2).sum(1)
            if (dx, dy) == (1, 0): # top constrains its bottom 
                cost += ((a[:, (x+1)*S, y*S:(y+1)*S] - a[ind, (x+1)*S-1, y*S:(y+1)*S])**2).sum(1)
            if (dx, dy) == (-1, 0): # bottom constrains its top 
                cost += ((a[:, x*S-1, y*S:(y+1)*S] - a[ind, x*S, y*S:(y+1)*S])**2).sum(1)
        index[x, y] = cost.argmin() 
        vis[x, y] = True


        for dx, dy in zip([1, -1, 0, 0], [0, 0, -1, 1]):
            nx = x+dx
            ny = y+dy
            if not (0 <= nx < L and 0 <= ny < L): continue
            if not inq[nx, ny]:
                l.append((nx, ny))
                inq[nx, ny] = True
    np.set_printoptions(linewidth=200)
    print index

    new = np.zeros_like(a[0])
    for x in xrange(L):
        for y in xrange(L):
            new[x*S:(x+1)*S, y*S:(y+1)*S] = a[index[x, y], x*S:(x+1)*S, y*S:(y+1)*S]
    plt.imshow(new, cmap='binary')
    plt.show()


