class static_game(object):
    def __init__(self, S, U):
        self.S = S
        self.U = U

    def benefit(self, u):
        return reduce(lambda a, b: a[b], u, self.U)

    def playing(self, players, times = 200):
        point_p = [0] * len(players)
        rec = []
        for iteration in xrange(times):
            choice = []
            for p in players:
                choice.append( p(self.S, self.U, rec) )
            rec.append(choice)
            benefit = self.benefit(choice)

            for ind, ele in enumerate(benefit):
                point_p[ind] += ele
        self.rec = rec
        return point_p
