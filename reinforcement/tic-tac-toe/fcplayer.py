import theano
import theano.tensor as T
import sys
sys.path.append('/home/shaofan/Projects/NN')
from NN.common.layers import FullConnectLayer, SoftmaxLayer, InputLayer
from NN.common.nets import NetModel 

from main import Player

class FCPlayer(Player, NetModel):
    def __init__(self, name, **kwarg):
        self.name = name

        self.env = []
        self.action = []
        self.reward = []
        self.history = []

        self.buildmodel(**kwarg)

    def buildmodel(self, shape=[9, 10, 9], activation=T.nnet.sigmoid):
        x = T.fmatrix('x')
        a = T.ivector('a')
        r = T.fvector('r')
        lr = T.fscalar('lr')

        layers = [InputLayer(x)]
        for ind, (Idim, Odim) in enumerate(zip(shape[:-1], shape[1:])):
            fc = FullConnectLayer(layers[-1].output, Idim, Odim, activation=activation,\
                                        name='FC[{}]'.format(ind))
            layers.append(fc)
        sm = SoftmaxLayer(layers[-1].output)
        layers.append(sm)

        output = sm.output 
        loss = T.sum(  T.log(sm.output[T.arange(a.shape[0]), a]) * r )
        prediction = output.argmax(1)

        params = reduce(lambda x, y: x+y.params, layers, [])
        updates = map(lambda x: (x, x+lr*T.grad(loss, x)), params)

        self.debug = theano.function([x, a, r], loss)
        self.train = theano.function([x, a, r, lr], loss, updates=updates)
        self.react = theano.function([x], prediction)
        
    def newgame(self):
        self.count = 0

    def play(self, board, marker):
        if marker == 2: # swap 1,2
            board = 3-board
            board[board==3] = 0

        a = self.react([board])[0]

        self.count += 1
        self.env.append(board)
        self.action.append(a)

        return a

    def endgame(self, res, board):
        super(FCPlayer, self).endgame(res)
        self.history.append(res)
        if res == 0: res = 0.05
        res = np.linspace(0, res, self.count)
        self.reward.extend(res)


    def __repr__(self):
        return '<FCPlayer: {}>'.format(self.name)


