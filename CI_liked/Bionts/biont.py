from numpy import *
from tools import *
from copy import copy, deepcopy
import matplotlib.pyplot as plt

class eco_world(list):
    def isfood(self, x, y):
        return self[x][y][0] == 'food'

    def enempty(self, x, y):
        self[x][y] = ('empty', 0)

    def enfood(self, x, y):
        self[x][y] = ('food', 1)

    def inrange(self, x, y):
        return 0 <= x < len(self) and 0 <= y < len(self[0])

class micro_system(object):           
    def __init__(self, row = 70, col = 70, 
        sys_size = 30, 
        food_density = 0.005, food_quality = 0.4, food_w = 100.0, food_create_speed = 5, food_revive = False):

        self.row = row
        self.col = col
        self.food_w = food_w
        self.food_quality = food_quality
        self.food_revive = food_revive
        self.food_create_speed = food_create_speed

        self.world = eco_world([])
        for i in xrange(row):
            self.world.append([])
            for j in xrange(col):
                self.world[i].append(('empty', 0))

        for i in xrange(int(row * col * food_density)):
            x, y = self.pick_a_pos()
            self.world[x][y] = ('food', food_quality)

#        age = 0, aging = 0.02,
#        hungry = 0, cost_sec = 0.02,
#        sense_r = 5, move_speed = 1, w = 0.01,
#        color = [0, 1, 0]):

        self.bionts = []
        for i in xrange(sys_size):
            x, y = self.pick_a_pos()
            _sense_r = random.randint(1, 8)
            _move_speed = random.randint(1, 4)
            _sense_r = 6
#            _move_speed = 2
            _w = random.rand()/10
            _color = random.rand(3)
            self.bionts.append(biont(init_pos = [x, y], sense_r = _sense_r, move_speed = _move_speed,
                                    w = _w, color = _color))

    def inrange(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.col

    def pick_a_pos(self):
        return random.randint(0, self.row), random.randint(0, self.col)

    def day(self, date):    
        for ind, ele in enumerate(self.bionts):            
            if ele == None or not ele.live():
                if ele != None:
                    print '%03dth biont: {%s} died in %05dth day.' % (ind, str(ele), date)
                self.bionts[ind] = None#biont(list(self.pick_a_pos()))
                continue

            x, y = ele.run(self.world, self.food_w)
            while not self.inrange(x, y):
                x, y = ele.run(self.world, self.food_w)
            ele[0], ele[1] = x, y                

            if self.inrange(x, y):
                if self.world.isfood(x, y):
                    ele.fit(self.food_quality)
                    self.world.enempty(x, y)

                    if self.food_revive:
                        x, y = self.pick_a_pos()
                        while self.world.isfood(x, y):
                            x, y = self.pick_a_pos()
                        self.world.enfood(x, y)                
            else:
                ele[0], ele[1] = self.pick_a_pos()

    def run(self, maxiter = 100):
        iteration = 0 
        food_create_acc = 0
        while iteration < maxiter:
            iteration += 1
            self.day(iteration)

            food_create_acc += self.food_create_speed
            while (food_create_acc > 1):
                food_create_acc -= 1
                x, y = self.pick_a_pos()
                while self.world.isfood(x, y):
                    x, y = self.pick_a_pos()
                self.world.enfood(x, y)
 
            self.plot()

    def plot(self):
        plt.clf()
        img = deepcopy(self.world)
        for i in xrange(self.row):
            for j in xrange(self.col):
                if img.isfood(i, j):
                    img[i][j] = [1, 0, 0, 1]
                else:
                    img[i][j] = [1, 1, 1, 1]
        for ele in self.bionts:
            if ele != None:
                img[ele[0]][ele[1]] = map(lambda x: x*(1-ele.age), ele.color)+[1.0-ele.hungry]
        plt.imshow(img, interpolation = 'none')
        plt.draw()
#        plt.pause(0.1)
#        raw_input('pause')

class biont(object):        
    
    def __init__(self, init_pos,
        age = 0, aging = 0.05,
        hungry = 0, cost_sec = 0.02,
        sense_r = 5, move_speed = 1, w = 0.01,
        color = [0, 1, 0]):

        self.pos = init_pos   

        self.age = age
        self.aging = aging

        self.hungry = hungry
        self.cost_sec = cost_sec

        self.sense_r = sense_r
        self.move_speed = move_speed
        self.w = w

        self.color = color

        self.direction = random.rand(4)

#       up, down, left, right

    def __str__(self):
        return 'aging = %lf| cost_sec = %lf| sense_r = %d| move_speed = %d| w = %lf' % \
            (self.aging, self.cost_sec, self.sense_r, self.move_speed, self.w)

    def live(self):
        self.hungry += self.cost_sec
        self.age += self.aging * self.hungry
        if self.age >= 1 or self.hungry >= 1:
            return False
        else:
            return True

    def fit(self, food):
        self.hungry -= food
        if self.hungry < 0:
            self.hungry = 0

    def run(self, world, food_w):  
        self.direction = map(lambda x: x * self.w+random.rand(), self.direction)
        r = self.sense_r
        
        tuple_grid = sense_r2grid(r, self.pos)
        grid = zip(tuple_grid[0], tuple_grid[1])
        for x, y in grid:
            if world.inrange(x, y):
                if world.isfood(x, y) > 0:
                    if x > self.pos[0]:
                        self.direction[1] += (r-(x-self.pos[0]))*food_w
                    elif x < self.pos[0]:
                        self.direction[0] += (r-(self.pos[0]-x))*food_w
                    if y > self.pos[1]:
                        self.direction[3] += (r-(y-self.pos[1]))*food_w
                    elif y < self.pos[1]:
                        self.direction[2] += (r-(self.pos[1]-y))*food_w
        
        tuple_grid = sense_r2grid(self.move_speed, self.pos)
        move_grid = zip(tuple_grid[0], tuple_grid[1])
        grid_w = [0] * len(move_grid)
        food_grid = []
        for ind, (x, y) in enumerate(move_grid):
            if world.inrange(x, y) and world.isfood(x, y):
                food_grid.append((x, y))
            if x > self.pos[0]:
                grid_w[ind] += self.direction[1] * (r - (x-self.pos[0]))
#                print 'grid_w[%d] += %lf * (%d - (%d-%d))' % (ind, self.direction[1], r, x, self.pos[0]) 
            elif x < self.pos[0]:
                grid_w[ind] += self.direction[0] * (r - (self.pos[0]-x))
#                print 'grid_w[%d] += %lf * (%d - (%d-%d))' % (ind, self.direction[0], r, self.pos[0], x) 
            if y > self.pos[1]:
                grid_w[ind] += self.direction[3] * (r - (y-self.pos[1]))
#                print 'grid_w[%d] += %lf * (%d - (%d-%d))' % (ind, self.direction[3], r, y, self.pos[1]) 
            elif y < self.pos[1]:
                grid_w[ind] += self.direction[2] * (r - (self.pos[1]-y))
#                print 'grid_w[%d] += %lf * (%d - (%d-%d))' % (ind, self.direction[2], r, self.pos[1], y) 
#        print 'pos\t',self.pos                
#        print 'dir\t',self.direction
#        print 'next\t',move_grid
#        print 'p_\t',grid_w
#        raw_input('pause')                        
        if len(food_grid) == 0:               
            move = p_choice(grid_w)
            ans = move_grid[move]
#            self.pos[0] = move_grid[move][0]
#            self.pos[1] = move_grid[move][1]
        else:
            move = random.randint(0, len(food_grid))
            ans = food_grid[move]
#            self.pos[0] = food_grid[move][0]
#            self.pos[1] = food_grid[move][1]

        return tuple(ans)

    def __setitem__(self, index, val):
        try:
            self.pos[index] = val
        except:
            pass

    def __getitem__(self, index):
        try:
            return self.pos[index]
        except:
            pass                     

if __name__ == '__main__':
    plt.ion()
    plt.show()

    a = micro_system()
    a.plot()
    raw_input('sizing')
    a.run(maxiter = inf)

    raw_input('done')
