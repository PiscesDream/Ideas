from copy import deepcopy
from numpy import ones_like, array
import matplotlib.pyplot as plt

class CA(object):
    '''
        Cellular Automata with:
            Numerical grid
            Circular/Null boundary
            Moore neighbourhood
    '''
    
    def __init__(self, init, radius, rule, circular = False, Null = .0): 
        '''
            init: initial grid
            radius: sense radius
            rule: update rule, arg is a list
            circular: boundary rule
        '''
        self.grid = init
        self.w, self.h = self.grid.shape
        self.radius = radius
        self.rule = rule
        self.circular = circular
        self.Null = Null

    def update(self):
        newgrid = ones_like(self.grid) * self.Null

        for x in range(self.w):
            for y in range(self.h):
                args = []
                for kx in range(-self.radius, self.radius+1):
                    for ky in range(-self.radius, self.radius+1):
                        if 0 <= x+kx < self.w and 0 <= y+ky < self.h:
                            args.append(self.grid[x+kx, y+ky])
                        else:
                            if self.circular:
                                args.append(
                                    self.grid[(x+kx >= self.w and (x+kx - self.w)) or (x+kx < self.w and x+kx),
                                              (y+ky >= self.h and (y+ky - self.h)) or (y+ky < self.h and y+ky)])
                            else:
                                args.append(self.Null)
                newgrid[x][y] = self.rule(array(args))
        self.grid = newgrid
        return newgrid

    def get_grid(self):
        return self.grid

    def plot(self):
        plt.imshow(self.grid, interpolation = 'none', cmap = 'binary')#or cmap = 'gray'
