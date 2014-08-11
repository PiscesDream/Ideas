from static_game import *
def random(S, U, rec):
    from random import choice
    return choice(S)

def kind(S, U, rec):
    return S[0]

def betray(S, U, rec):
    return S[0]

def revenge(S, U, rec):
    if len(rec) == 0:
        return S[0]
    else:
        return rec[-1][0]

if __name__ == '__main__':
    sg = static_game(['k', 'b'],\
    {'k':{'k':(7, 7), 'b':(-2, 10)},\
            'b':{'k':(10, -2), 'b':(-5, -5)}})

    l = [random, kind, betray, revenge]
    for ele in l:
        print '-' * 80
        print ele.__name__,'vs:'
        point = 0
        for ele2 in l:            
            t = sg.playing([ele, ele2])
            print '\t',ele2.__name__,'\t:', t
            point += t[0]
        print 'total loss:', point
