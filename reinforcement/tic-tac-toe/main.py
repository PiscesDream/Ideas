import numpy as np

class TicTacToe(object):
    def __init__(self):
        pass

    def play(self, p1, p2, ordered=False, verbose=1):
        p1.newgame()
        p2.newgame()

        players = [p1, p2]
        if not ordered: np.random.shuffle(players)
        self.board = np.zeros((9)).astype('int')

        for i in xrange(9):
            num = i%2
            marker = num+1
            try:
                move = players[i%2].play(self.board, marker)
                move = int(move)
                if self.board[move] != 0: raise Exception
                self.board[move] = marker 
            except Exception as e:
#               raise e
                if verbose: print players[num], 'violates the rules.'
                players[1-num].endgame(1, self.board)
                players[num].endgame(-1,self.board)
                return players[1-num] # fail to respond correctly 

            if self.win(marker): break

        if verbose >= 2:
            print 'final'
            show_board(self.board)
        if self.win(1): 
            if verbose: print players[0], 'wins.'
            players[0].endgame(1,self.board)
            players[1].endgame(-1,self.board)
            return players[0]
        elif self.win(2): 
            if verbose: print players[1], 'wins.'
            players[0].endgame(-1,self.board)
            players[1].endgame(1,self.board)
            return players[1]
        else: 
            players[0].endgame(0,self.board)
            players[1].endgame(0,self.board)
            if verbose: print 'Tie.'
            return None

    def win(self, marker):
        a = self.board
        return (a[0]==a[1]==a[2]==marker or a[3]==a[4]==a[5]==marker or \
                a[6]==a[7]==a[8]==marker or a[0]==a[3]==a[6]==marker or \
                a[1]==a[4]==a[7]==marker or a[2]==a[5]==a[8]==marker or \
                a[0]==a[4]==a[8]==marker or a[2]==a[4]==a[6]==marker)

class Player(object):
    def __init__(self, name):
        self.name = name

    def newgame(self):
        pass

    def endgame(self, res, board):
        return 
        if res == -1:
            print ("[{}]: you lose".format(self.name))
        elif res == 1:
            print ("[{}]: you win".format(self.name))
        elif res == 0:
            print ("[{}]: tie".format(self.name))

class HumanPlayer(Player):
    def play(self, board, marker):
        print 'here is theself.board, you are [{}]'.format(marker)
        show_board(board)
        position = raw_input("[{}] Input your move:".format(self.name))
        return position

    def __repr__(self):
        return '<HumanPlayer: {}>'.format(self.name)

def show_board(board):
    board = board.astype('string')
    print '\n------------\n'.join(map(lambda x: ' | '.join(x), [board[x:x+3] for x in [0,3,6]]))


class RandomPlayer(Player):
    def __init__(self, name):
        self.name = name

    def play(self, board, marker):
        return np.random.choice(np.arange(9)[board==0])

    def __repr__(self):
        return '<RandomPlayer: {}>'.format(self.name)

def fctest():
    from fcplayer import FCPlayer
    fc1 = FCPlayer('fc1', shape=[9, 100, 100, 9])

    rewards = [-1, 0, +1]
    lr = 1e-5
    lastloss = np.inf
    i = 0
    while i < np.inf:
        i += 1
        game.play(rp1, fc1, verbose=False)

        if i%10000 == 0:
            print 'iter: {}'.format(i)
            game.play(rp1, fc1, verbose=1)
            loss = fc1.train(fc1.env, fc1.action, np.array(fc1.reward).astype('float32'), lr)
            print '>>> loss:', loss, '\tlr:', lr
            print dict(zip(rewards, map(lambda x: fc1.history.count(x), rewards)) )
            if lastloss >= loss:
                lr *= 0.6
            else:
                lr *= 1.05
            lastloss = loss
            fc1.reward = []
            fc1.env = []
            fc1.action = []
            fc1.history = []

def qtest(game, contestant):
    from qplayer import QPlayer
    qp = QPlayer('qp 1', alpha = 0.1, discount = 0.2, epsilon = 0.9)

    wins, ties, loses = 0, 0, 0 
    i = 0
    while i < np.inf: 
        i += 1
        res = game.play(qp, contestant, verbose=0)
        if res is None:
            ties += 1
        elif res is qp:
            wins += 1
        else:
            loses += 1

        if i % 1000 == 0:
            print 'win: {}\ttie: {}\tloses: {}\tepsilon:{}'.format(wins, ties, loses, qp.epsilon)
            qp.epsilon *= 0.995
            wins, ties, loses = 0,0,0
    return qp

if __name__ == '__main__':
    game = TicTacToe()

    hp1 = HumanPlayer('Alice')
    hp2 = HumanPlayer('Bob')

    rp1 = RandomPlayer('RP1')
    rp2 = RandomPlayer('RP2')

    x = [[1]*9,[3]*9,[2]*9]
    a = [0, 1, 2] 
    r = [-1, 1, -1]

    game.play(rp1, rp2)

#   fctest()
    qtest(game, rp1)

