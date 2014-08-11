''' 
    Pick a person
    Neighbors in 9 directions 
    P(do with feature) = similarity 
        if someone like us, we interact
        else we don't change our behavior

    Features 5
    Traits 12 (the #set of feature)
'''

from numpy import array
from numpy.random import randint, rand
import matplotlib.pyplot as plt

class cul_grid(object):
    
    def __init__(self, features = 4, traits = 6, gridsize = (40, 20)):
        self.traits = traits
        self.features = features
        self.gridsize = gridsize
        self.H, self.W = gridsize
        
        self.grid = randint(self.traits, size = self.gridsize + (self.features,))

    def update(self):
        row = randint(self.H)
        col = randint(self.W)
        a = self.grid[row, col]
        for kx, ky in zip([-1,0,1,0],[0,-1,0,1]):
            nx = row + kx
            ny = col + ky
            if not (0 <= nx < self.H and 0 <= ny < self.W): continue
            b = self.grid[nx, ny]
            p = (a==b).mean()
            for ind, (x, y) in enumerate(zip(a, b)):
                if rand() < p and x != y:
                    b[ind] = x
            self.grid[nx, ny] = b

    def plot(self):
#        rec =[]
        #down, left, up, right
        shift = array([[-.5, -.5], [-.5, .5], [.5, .5], [.5, -.5]])
        for x in range(self.H):
            for y in range(self.W):
                cur = self.grid[x, y]
                for k in range(4):
                    p1 = shift[k] + [x, y]
                    p2 = shift[k-1] + [x, y]
                    nx, ny = shift[k] + shift[k-1] + [x, y]
                    if not (0 <= nx < self.H and 0 <= ny < self.W): alpha = 1
                    else: 
                        alpha = (cur != self.grid[nx, ny]).mean()
#                        rec.append(alpha)
                    plt.plot([p1[0],p2[0]], [p1[1],p2[1]], color = 'black', alpha = alpha)
#        print array(alpha).mean() 

if __name__ == '__main__':
    M = cul_grid()
    iter = 0
    plt.ion()
    plt.show()
    plt.draw()
    raw_input('sizing')
    while iter < 100000:
        iter += 1
        M.update()

        if iter % 100 == 0:
            plt.clf()
            M.plot()
            plt.draw()
