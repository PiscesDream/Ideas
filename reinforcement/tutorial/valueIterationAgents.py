# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
import numpy as np

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
#       print mdp.getStates() # ['TERMINAL_STATE', (0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
#       s = mdp.getStates()[1]
#       print mdp.getPossibleActions(s) # ('north', 'west', 'south', 'east') 
#       a = mdp.getPossibleActions(s)[0]
#       print mdp.getTransitionStatesAndProbs(s, a) # [((0, 1), 0.8), ((1, 0), 0.1), ((0, 0), 0.1)]
#       ns = mdp.getTransitionStatesAndProbs(s, a)[0][0]
#       print mdp.getReward(s, a, ns)  # 0.0
#       raise Exception

        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        # value iteration
        for i in xrange(iterations):
            newvalues = self.values.copy()
            for state in mdp.getStates():
                if state == 'TERMINAL_STATE': continue
                candidates = []
                for action in mdp.getPossibleActions(state): # noraml state
                    if len( mdp.getTransitionStatesAndProbs(state, action) ) > 1:
                        candidates.append( sum([probability*self.getValue(nextstate) \
                                for nextstate, probability in mdp.getTransitionStatesAndProbs(state, action)]) )

                if len(candidates) == 0: # TERMINAL_STATE
                    for action in mdp.getPossibleActions(state): # terminal 
                        candidates.append( sum([mdp.getReward(state, action, nextstate) \
                            for nextstate, _ in mdp.getTransitionStatesAndProbs(state, action) \
                            if nextstate=='TERMINAL_STATE']) )
                    newvalues[state] = max(candidates)
                else:
                    newvalues[state] = discount * max(candidates)  
            self.values = newvalues
#       raise Exception

        # Q-value
#       lr = 0.1
#       self.Qvalues = util.Counter() # A Counter is a dict with default 0
#       for i in xrange(iterations):
#           newQvalues = self.Qvalues.copy()
#           for state in mdp.getStates():
#               if state == 'TERMINAL_STATE': continue # TERMINAL STATE

#               for action in mdp.getPossibleActions(state):
#                   futureValueSum = 0.0
#                   for nextstate, probability in mdp.getTransitionStatesAndProbs(state, action):
#                       futureValue = [self.getQValue(nextstate, action_) for action_ in mdp.getPossibleActions(nextstate)]
#                       if len(futureValue) == 0: futureValue = [0.0]
#                       futureValueSum += probability * max(futureValue)
#                        
#                   newQvalues[(state, action)] = \
#                       self.getQValue(state, action) + \
#                       lr * (mdp.getReward(state, action, nextstate)\
#                           + discount * futureValueSum\
#                           - self.getQValue(state, action) )
#           self.Qvalues = newQvalues
#       raise Exception


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        return sum([self.mdp.getReward(state, action, nextstate) + self.discount * probability * self.getValue(nextstate)\
                                for nextstate, probability \
                                in self.mdp.getTransitionStatesAndProbs(state, action)])
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if self.mdp.isTerminal(state): return None
        actions = self.mdp.getPossibleActions(state)
        action_values = [ sum([self.getValue(nextstate) * probability \
                                for nextstate, probability \
                                in self.mdp.getTransitionStatesAndProbs(state, action)])\
                          for action in actions]
        return actions[np.argmax(action_values)]
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
