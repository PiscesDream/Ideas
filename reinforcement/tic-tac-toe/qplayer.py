# qlearning

from main import Player
import numpy as np

class QPlayer(Player):
    def __init__(self, name, alpha, discount, epsilon):
        super(QPlayer, self).__init__(name)
        self.name = name

        self.played = 0 
        
        self.QValues = {}
        self.alpha = alpha
        self.discount = discount
        self.epsilon = epsilon
    def hash(self, x):
        return tuple(x)
    def setQValue(self, state, action, value):
        self.QValues[(self.hash(state), action)] = value
    def getQValue(self, state, action):
        return self.QValues.get((self.hash(state), action), 0.0)
    def getLegalActions(self, state):
        #return (state==0).nonzero()[0]
        return np.arange(9)
    def computeActionFromQValues(self, state):
        actions = self.getLegalActions(state)
        action_values = [self.getQValue(state, action) for action in actions]
        return actions[np.argmax(action_values)]
    def getAction(self, state):
        legalActions = self.getLegalActions(state)
        action = None
        if np.random.rand() < self.epsilon: 
            action = np.random.choice(legalActions)
        else:
            prob = np.array([self.getQValue(state, a) for a in legalActions])
            action = legalActions[np.argmax(prob)]
        return action
    def update(self, state, action, nextState, reward):
        try:
            nextStateMaxQ = max([self.getQValue(nextState, nextAction)  \
                                for nextAction in self.getLegalActions(nextState)])
        except:
            nextStateMaxQ = 0
        self.setQValue(state, action, \
            self.getQValue(state, action) \
            + self.alpha * (reward \
                          + self.discount * nextStateMaxQ \
                          - self.getQValue(state, action))
            )
#   def getPolicy(self, state):
#       return self.computeActionFromQValues(state)
#   def getValue(self, state):
#       return self.computeValueFromQValues(state)
#   def computeValueFromQValues(self, state):
#       return max([self.getQValue(state, action) for action in self.getLegalActions(state)])

    def save(self, filename):
        pass
#       self.name = name
#       self.played = 0 
#       self.QValues = {}
#       self.alpha = alpha
#       self.discount = discount
#       self.epsilon = epsilon
    def load(self):
        pass

    def newgame(self):
        self.memory = []

    def play(self, board, marker):
        if marker == 2: # swap 1,2
            board = 3-board
            board[board==3] = 0
        a = self.getAction(board)
        self.memory.append( (board, a) )
        return a

    def endgame(self, res, board):
        if res == 0: 
            res = -0.1
#       elif res == -1:
#           res = -10
#       else:
#           res = 10
        self.memory.append( (board, None) )
        for thispair, nextpair in zip(self.memory[:-1], self.memory[1:]):
            self.update(thispair[0], thispair[1], nextpair[0], res)
        self.memory = []
        self.played += 1

    def __repr__(self):
        return '<QPlayer: {}>'.format(self.name)



