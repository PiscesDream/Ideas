from copy import deepcopy
from numpy import ones_like, array, zeros
import matplotlib.pyplot as plt

class CA(object):
    '''
        Cellular Automata with:
            Numerical grid
            Circular/Null boundary
            Moore neighbourhood
    '''
    
    def __init__(self, init, radius, rule, circular = False, Null = .0, global_update = False): 
        '''
            init: initial grid
            radius: sense radius
            rule: update rule
                -local update: arg is a list
                -global update: cur grid, arg as a 3d array
            circular: boundary rule
        '''
        self.grid = init
        self.w, self.h = self.grid.shape
        self.radius = radius
        self.rule = rule
        self.circular = circular
        self.Null = Null
        self.global_update = global_update

    def update(self): 
        if self.global_update:
            arg_grid = zeros((self.grid.shape+((2 * self.radius+1) ** 2,)))
        else:
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
                if self.global_update:
                    arg_grid[x][y] = args
                else:
                    newgrid[x][y] = self.rule(array(args))
        if self.global_update:
            self.grid = self.rule(self.grid, arg_grid)
        else:
            self.grid = newgrid
        return self.grid

    def get_grid(self):
        return self.grid

    def plot(self):
        plt.imshow(self.grid, interpolation = 'none', cmap = 'binary')#or cmap = 'gray'
