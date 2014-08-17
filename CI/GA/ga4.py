'''
    Update in Aug. 15rd, 2014
    add multiprocess
        solve queue limited new-defined class
'''

import multiprocessing as mp 
from numpy import *
import time

class extended_Queue(object):
    
    def __init__(self, max = 100, threshold = 300):
        self.qs = [mp.Queue() for i in range(max)]
        self.ind = 0
        self.max = max
        self.threshold = threshold

    def put(self, ele):
        if self.qs[self.ind].qsize() > self.threshold:
            self.ind += 1
            if self.ind >= self.max:
                pass
#                raw_input('leaking')
        self.qs[self.ind].put(ele)

    def get(self):
        if self.qs[self.ind].empty():
            self.ind -= 1
#        print self.ind
#        print self.__repr__()
        return self.qs[self.ind].get()
    
    def refresh(self):
        while self.qs[self.ind].qsize() > self.threshold:
            self.ind += 1

    def __repr__(self):
        return '<Extended Queue; Qsizes: '+str(map(lambda x: x.qsize(), self.qs)) + '>'

def choice(eles, num, p):
    ans = []
    for i in xrange(num):
        acc = .0
        thr = random.rand()
        for ind, ele in enumerate(p):
            acc += ele
            if acc > thr:
                ans.append(eles[ind])
                break
    return ans                


class GA(object):
    
    def __init__(self, fitness_f, terminator, generation_size, generation_init, 
        crossover_vs_survival, crossover_f, mutation_rate, mutation_f, 
        plot = False, plot_f = None, plot_interval = 100,
        cmp_f = None,
        multiprocess = False):

        self.fitness_f = fitness_f
        if 'fitness_thresold' in terminator:
            self.fitness_thresold = terminator['fitness_thresold']
            self.iter_maximum = None
        else:
            self.iter_maximum = terminator['iter_maximum']
            self.fitness_thresold = None

        self.generation_size = generation_size
        self.generation_init = generation_init
        self.crossover_vs_survival = crossover_vs_survival
        self.crossover_f = crossover_f
        self.mutation_rate = mutation_rate
        self.mutation_f = mutation_f
        self.plot = plot
        self.plot_f = plot_f
        self.best_fitness = None
        self.plot_interval = plot_interval
        self.multiprocess = multiprocess

        if cmp_f == None:
            self.cmp_f = lambda a,b: a>b
        else:
            self.cmp_f = cmp_f

    def result(self):
        self.best_fitness = None
        self.fit()
        return self.best_biont
    
    def fit(self):            
        #multiprocessing queue
        res = extended_Queue()

        generation = [None] * self.generation_size
        fitness = [None] * self.generation_size

        fitness_max = None        
        for i in xrange(self.generation_size):
            generation[i] = self.generation_init()
            fitness[i] = self.fitness_f(generation[i])
            if fitness_max == None or self.cmp_f(fitness[i], fitness_max):
                fitness_max = fitness[i]
                best_child = generation[i]
        fitness_sum = sum(fitness)
        
        iteration = 0
        while (self.fitness_thresold == None and iteration < self.iter_maximum) or \
            (self.iter_maximum == None and not self.cmp_f(fitness_max,self.fitness_thresold)):

            if self.best_fitness == None or self.cmp_f(fitness_max, self.best_fitness):
                self.best_fitness = fitness_max
                self.best_biont = best_child

            print '%03dth  generation|\tbest fitness:\t%lf|\tbest child fitness:\t%lf' % (iteration, self.best_fitness,fitness_max)

            if self.plot and iteration % self.plot_interval == 0:
                self.plot_f(best_child, 'red', False)            
                self.plot_f(self.best_biont, 'blue', True)

            iteration += 1
            
            #generation probability
            gen_pr = map(lambda x: x / fitness_sum, fitness)
           
            next_generation = []
#            next_gen_fitness = []

            while len(next_generation) < self.generation_size:
                if random.rand() > self.crossover_vs_survival:
                    #survival
                    next_generation.extend(choice(generation, num = 1, p = gen_pr))
                else:                  
                    tmp_child = self.crossover_f( *choice(generation, num = 2, p = gen_pr) ) 
                    if type(tmp_child).__name__ == 'tuple':
                        next_generation.extend(list(tmp_child))
                    else:
                        next_generation.append(tmp_child)

            #mutation
            l = len(next_generation)
            for i in xrange( int(l * self.mutation_rate) ):
                mutation_gen = random.randint(0, l)
                next_generation[mutation_gen] = self.mutation_f(next_generation[mutation_gen])

            #inherit
            generation = copy(next_generation)          
            fitness = [None] * l
            fitness_max = None
           


            start_time = time.time()
            if self.multiprocess:
                #fitness[i] = self.fitness_f(generation[i])
                #mp that line
                core_num = 4
                batch_size = l/core_num
 
                #print 'creating missions'
                missions = zip(range(l), generation)
                def f(mission):
                    for ind, ele in mission:
                        res.put((ind, self.fitness_f(ele)))

                #print 'processing'
                tasks = []
                for ind in range(core_num):
                    if ind+1 == core_num:
                        p = mp.Process(target = f, name = 'MP:'+str(ind), args=(missions[ind * batch_size:],))
                    else:
                        p = mp.Process(target = f, name = 'MP:'+str(ind),
                                       args=(missions[ind * batch_size:(ind+1) * batch_size], ))
                    tasks.append(p)
                    p.start()

                for task in tasks:
                    task.join()

                #the context is copied by other processing
                #restore the context
                res.refresh()
                for ind in range(l):
                    index, value = res.get()
                    fitness[index] = value                    
                    if fitness_max == None or self.cmp_f(value, fitness_max):
                        fitness_max = value 
                        best_child = generation[index]

            else:
                for i in xrange(l):
                    fitness[i] = self.fitness_f(generation[i])
                    if fitness_max == None or self.cmp_f(fitness[i], fitness_max):
                        fitness_max = fitness[i]
                        best_child = generation[i]
                fitness[i] = self.fitness_f(generation[i])
            print 'takes', time.time()-start_time

            fitness_sum = sum(fitness)
            
        self.plot_f(best_child, 'red', False)            
        self.plot_f(self.best_biont, 'blue', True)
        raw_input('Done.')

