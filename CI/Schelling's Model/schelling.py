from plot import plot
import matplotlib.pyplot as plt
from numpy import *

def p_choice(p, shift = 0):
    t = random.rand()
    acc = .0
    for ind, ele in enumerate(p):
        acc += ele
        if acc >= t:
            return ind + shift            


class schelling(object):

    def ind2co(self, ind):
        x = ind / self.size[1]
        y = ind % self.size[1]
        return (x, y)

    def __init__(self, size, full, p):
        self.total = reduce(lambda a, b: a * b, list(size), 1)
        self.size = size
        self.empty = []

        self.a = zeros(self.total)
        idx = random.permutation(self.total)
        for ind in xrange(int(self.total * full)):
            self.a[idx[ind]] = p_choice(p, 1)
        for ind, ele in enumerate(self.a):
            if ele == 0:
                self.empty.append(ind)

    def get_grid(self):
        return self.a.reshape(self.size)

    def run(self, tol, tol_f, sense_r = 1, move_dis = None,
            maxiter = 50, 
            plot_fun = None, plot_interval = 1, 
            tol_rate_to_num = False):                             
        kx = []
        ky = []
        for x in xrange(-sense_r, sense_r+1, 1):
            for y in xrange(-sense_r, sense_r+1, 1):
                if x != 0 or y != 0:
                    kx.append(x)
                    ky.append(y)

        if tol_rate_to_num == True:
            tol = map(lambda x: x * len(kx), tol)

        iteration = 0
        while iteration < maxiter:
            iteration += 1
            ind = random.randint(0, self.total)
            while self.a[ind] == 0:
                ind = random.randint(0, self.total)

            friends = 0
            enemy = 0
#            print map(lambda x: ind + x[0] * self.size[1] + x[1], zip(kx, ky))
            friend_list = []
            for xm, ym in zip(kx, ky):
                try:
                    if self.a[ind + xm * self.size[1] + ym] == self.a[ind]:
                        friends += 1
#                        friend_list.append([ind + xm * self.size[1] + ym])
                    else:
                        if self.a[ind + xm * self.size[1] + ym] != 0:
                            enemy += 1
                except:
                    pass

#            print friends                                        
            if tol_f(friends, enemy, tol[int(self.a[ind])-1]):
#                print 'moving'
                ind0 = random.randint(0, len(self.empty))                

                flag = True
                if move_dis != None:
                    ind0_co = self.ind2co(ind0)
                    ind_co = self.ind2co(ind)
                    dist = abs(ind_co[0] - ind0_co[0]) + abs(ind_co[1] - ind0_co[1]) 
                    if dist > move_dis[int(self.a[ind])-1]:
                        flag = False
                        
                if flag:
                    self.a[self.empty[ind0]] = self.a[ind]
                    self.a[ind] = 0                          
                    self.empty[ind0] = ind

            if plot_fun != None and iteration % plot_interval == 0:
                plot_fun(self.get_grid())
                print iteration

def sim_plot(x):
    plot(x)
    plt.draw()

def tol_f1(friends, enemy, tol):
    return friends < tol

def tol_f2(friends, enemy, tol):
    return friends-enemy < tol

def tol_f3(friends, enemy, tol):
    return friends > tol * enemy

def tol_f4(f, e, t):
    return tol_f1(f, e, t * 3) or tol_f2(f, e, t)

if __name__ == '__main__':
    a = schelling((40, 70), 0.7, [0.6, 0.1, 0.1, 0.1, 0.1])
    plt.ion()
#    plt.axes([1,1,1,1])
    plot(a.get_grid())
    plt.draw()
    plt.show()
    raw_input('sizing')

    a.run(tol = [0.13, 0.02, 0.02, 0.01, 0.01], tol_f = tol_f4, tol_rate_to_num = True,
         move_dis = None,#[10, 10, 10, 5, 5],
         sense_r = 3,
         maxiter = inf,
         plot_fun = sim_plot, plot_interval = 10000)
    raw_input('done')
