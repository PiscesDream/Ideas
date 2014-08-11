#version 2.0
from numpy.random import shuffle, randint
from numpy import mean
from config import Default_rep_req as rep_req
from config import Growth_g as G
from ga2 import GA

class biont(object):

    def __init__(self):
        self.age = 0
        self.health = 100.

    def __repr__(self):
        return '<Age: %d; Hp: %d>' % (self.age, self.health)

class group(object):

    def __init__(self, gene = [1]*50+[0]*50, num = 3):
        self.gene = gene 
        self.g = map(lambda x: biont(), range(num))
        self.alive = num
        self.num = num

    def reset(self):
        self.g = map(lambda x: biont(), range(self.num))
        self.alive = self.num

    def aday(self, plant):
        shuffle(self.g)

        self.alive = 0
        for ele in self.g:
            if ele.health < 0: continue

            self.alive += 1

            ele.age += 1
            ele.health -= 10

            if self.gene[ele.age] == 1 and plant > 0:
                if plant >= 100-ele.health:
                    plant -=  (100-ele.health)
                    ele.health = 100.
                else:
                    ele.health += plant
                    plant = .0

            if 20 <= ele.age <= 40 and ele.health >= rep_req and randint(0, 100)<ele.health:
                for i in range(int(ele.health/10)):
                    self.g.append(biont())
                ele.health -= rep_req
        if self.alive == 0:
            return -1
        else:
            return plant 

    def __repr__(self):
        return '<Gene: %s; Rate: %lf>' % (''.join(map(lambda x: str(x), self.gene)), mean(self.gene))

def group_fitness(g):
    g.reset()
    plant = 700
    date = 0.
    while g.alive > 0:
        date += 1
        plant = g.aday(plant)
        plant = plant * (1 + G(plant))
#        print 'Day %d; Num: %d; Plant: %d' % (date, g.alive, plant)
#        raw_input(g.g)
    return date + 1 - mean(g.gene)

def group_gen():
    base = [1]*50+[0]*50
    shuffle(base)
    return group(base)

def group_cross(a, b):
    child = range(100)
    for ind, (x, y) in enumerate(zip(a.gene, b.gene)):
        if randint(0, 2) == 0:
            child[ind] = x
        else:
            child[ind] = y
    return group(child)

def group_mutation(base):
    for i in range(randint(0, 5)):
        cur = randint(0, 100)
        base.gene[cur] = 1 - base.gene[cur]
    return base

if __name__ == '__main__':
#    group_fitness(group([1] * 50 + [0] * 50))

    Group_GA = GA(group_fitness, {'iter_maximum':9999999}, 50, group_gen,
                0.95, group_cross, 0.05, group_mutation) 
    Group_GA.fit()
