from softmax_reg_2048_self import *
from _2048_self import _2048
from numpy import * 

cl = softmax_reg_for_2048(16, 4, ops = {'maxiter':200, 'disp':False})

def softmax_decide(board, u, d, l, r):
    global cl
    p = cl.p_predict(board.flatten(), get_ans = False).flatten()
    if all(board == u[0]):
        p[0] = 0
    if all(board == d[0]):
        p[1] = 0
    if all(board == l[0]):
        p[2] = 0
    if all(board == r[0]):
        p[3] = 0
#    if p.sum() == 0:
#        p = array([0.25, 0.25, 0.25, 0.25])
#    p = p / p.sum()
#    return random.choice(range(4), p = p) 
    return p.argmax()        

if __name__ == '__main__':
    global cl

#    tr_x, tr_l = load_data()
    tr_x_all = []
    tr_l_all = []

    game = _2048(length = 4, pick_rate = 0.2)
    for i in xrange(200):
        print 'Learning %02d round(s)' % i
        tr_x, tr_l = game.mul_test(10, softmax_decide, addition_arg = True)       
#        tr_x_all.extend(tr_x)
#        tr_l_all.extend(tr_l)
#        cl.fit(array(tr_x_all).T, array(tr_l_all).T)
        cl.fit(tr_x.T, tr_l.T)
       

    '''best:
    -------------------------------------------------------------------------
    max round: 0520     | avr round: 263.60
    max point: 7476     | avr point: 3182.80
    max block: 512
    '''
