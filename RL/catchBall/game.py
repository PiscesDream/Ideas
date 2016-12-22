###################
# o               #
#             o   #
#        o        #
#                 #
#                 #
#   ---           #
###################

import numpy as np
import os

class DroppingGame(object):
    def __init__(self, box_size, # box_size: (rows, cols)
                        per_range, # perceptible range: an int
                        cat_len, # catcher length:  an int
                        max_int, # max interval
                        rewards, # rewards: (succeed, fail)
                        robj_gen, # random object generator
                ):
        self.box_size = box_size
        self.per_range = per_range
        self.cat_len = cat_len
        self.max_int = max_int
        self.rewards = rewards
        self.robj_gen = robj_gen

        assert per_range <= box_size[0]
        assert cat_len <= box_size[1]

    def play(self, learner, verbose=1):
        box = np.zeros((self.box_size[0]+1, self.box_size[1]))
        l, r = 0, self.cat_len-1 # left and right of the catcher
        box[-1][l:r+1] = 1

        i = 0
        count = 0.
        totalreward = 0.
        lastavr = 0.
        while i < self.max_int:
            # move: (0, 1, 2) left, stay, right
            move, qval = learner.action(box)
            if move == 0 and l > 0:
                l -= 1; r -= 1
            elif move == 2 and r < box.shape[1]-1:
                l += 1; r += 1

            # update box
            new_box = self.robj_gen(box, i)
            new_box[-1] = 0
            box[-1][l:r+1] = 1

            # calc reward 
            reward = 0.0
            if box[-2].sum() > 0: # there is a dropping object in the last row
                catched = box[-2][l:r+1].sum()
                missed  = box[-2].sum() - catched
                reward += catched*self.rewards[0] + missed*self.rewards[1]

            if reward != 0.:
                count += 1
                totalreward += reward
                if count > 100: 
                    lastavr = totalreward/count
                    count = 0
                    totalreward = 0.
            learner.update(box, new_box, reward, move)
            
            # output
            if verbose > 0:
#               print(chr(27) + "[2J")
                os.system('clear')
                print 'max qval =', qval.max()
                for row in box:
                    for ele in row:
                        print 'o' if ele == 1 else '.',
                    print 
                print 'reward =', reward
                print 'avr reward =', lastavr 
#               raw_input()
            
            i += 1
            box = new_box

class IntervalGenerator(object):
    def __init__(self, interval):
        self.interval = interval

    def __call__(self, cur_state, iteration):
        m = cur_state.shape[1]
        newrow = np.zeros((1, m))
        if iteration % self.interval == 0:
            newrow[0, np.random.randint(0, m)] = 1
        return np.concatenate([newrow, cur_state[:-2], cur_state[-1:]], 0)




import sys
sys.path.insert(0, '/home/shaofan/.local/lib/python2.7/site-packages')
import keras
from keras.models import Sequential, Model
keras.backend.theano_backend._set_device('dev0')
from keras.layers import Dense, Activation

class Learner(object):
    def __init__(self, input_shape, output_dim, gamma = 0.9):
        self.gamma = gamma
        self.xs = []
        self.ys = []

        model = Sequential()
        model.add(Dense(500, input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(Dense(500))
        model.add(Activation('relu'))
        model.add(Dense(500))
        model.add(Activation('relu'))
        model.add(Dense(500))
        model.add(Activation('relu'))
        model.add(Dense(500))
        model.add(Activation('relu'))
        model.add(Dense(output_dim))
        model.add(Activation('softmax'))
#       model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
        model.compile(loss='mse', optimizer='adam')

        self.model = model
        
    def action(self, s):
        qval = self.model.predict(s.flatten().reshape(1,-1), batch_size=1)[0]
        sm = np.exp(qval)
        sm /= sm.sum()
        return np.random.choice(len(sm), p=sm), qval

    def update(self, s, next_s, reward, move):
        qval = self.model.predict(np.array([s.flatten(), next_s.flatten()]), batch_size=2)
        y = qval[:1]
        y[0][move] = reward + self.gamma*qval[1].max()
        self.__update(s.flatten(), y[0])

    def __update(self, x, y):
        self.xs.append(x)
        self.ys.append(y)
        if len(self.xs) >= 1000:
            self.model.fit(np.array(self.xs), 
                np.array(self.ys),
                batch_size=200,
                nb_epoch=5,
                verbose=1)
            self.xs = []
            self.ys = []
            # raise Exception
        
if __name__ == '__main__':
    boxh, boxw = 20, 10

    game = DroppingGame(
            box_size=(boxh, boxw), 
            per_range=5, 
            cat_len=4,
            max_int=np.inf, 
            rewards=(10, -10), 
            robj_gen=IntervalGenerator(2),)

    game.play(Learner((boxw*(boxh+1),), 3)) 




