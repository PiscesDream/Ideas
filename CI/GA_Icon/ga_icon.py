import ga4
import matplotlib.pyplot as plt
from numpy import ones, array, log
from numpy.random import randint, uniform
from canvas_tool import Canvas
import Image as I

ori = array(I.open('google.jpeg').resize((32, 32)), dtype=float)/255

class biont(object):
    
    def __init__(self, size = 32, n = 10):
        self.n = n
        self.size = size
        self.tris = [(randint(0, size, size=(3, 2)),
                      uniform(0, 1, size =(3))) for k in range(n)]

    def recreate(self):
        self.can = Canvas(ones((self.size, self.size, 3)))
        for ele in self.tris:
            self.can.Triangle(*ele)
        self.can.truncate() 

def fitness(biont):
    global ori
    biont.recreate()
    return ((biont.can.img - ori)**2).sum()

def generate():
    return biont()

def crossover(fa, ma):
    for i in range(randint(0, fa.n)):
        faind = randint(0, fa.n)
        maind = randint(0, ma.n)
        fa.tris[faind], ma.tris[maind] = ma.tris[maind], fa.tris[faind]
    return fa, ma

'''def mutation(biont):
    for i in range(10):
        ind = randint(0, biont.n)
        biont.tris[ind] = (randint(0, biont.size, size=(3, 2)),
                           uniform(0, 1, size=(3)))
    return biont'''
def mutation(dc):
    tmp = biont()
    tmp.recreate()
    return tmp

main_figure = plt.figure('best_biont')
bbax = main_figure.add_subplot(111)
sub_figure = plt.figure('best_child')
bcax = sub_figure.add_subplot(111)
plt.ion()
plt.show()
bbax.imshow(ori)
def plot(biont, child):
    global bbax, bcax, main_figure, sub_figure
    bbax.clear()
    bcax.clear()
    biont.can.plot(bbax)
    child.can.plot(bcax)
    main_figure.canvas.draw()
    sub_figure.canvas.draw()

if __name__ == '__main__':

    raw_input('resize')
    MyGA = ga4.GA(fitness_f = fitness, 
                  terminator = {'fitness_thresold':0},
                  generation_size = 500 ,
                  generation_init = generate,
                  crossover_vs_survival = 0.95,
                  crossover_f = crossover, 
                  mutation_rate = 0.15, 
                  mutation_f = mutation, 
                  plot = True, 
                  plot_f = plot, 
                  plot_interval = 1, 
                  cmp_f = lambda a,b: a<b,
                  multiprocess = True)
    MyGA.fit()

