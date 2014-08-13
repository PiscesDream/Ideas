from numpy import *

def separate(l, length):
    x = []
    y = []
    for i in xrange(len(l)- length):
        x.append(l[i: i+length])
        y.append(l[i+length])
    return array(x), array(y)

class test_sys(object):

    def __init__(self, fun, data_size, sample_len, bits, args = None):
        if args == None:
            self.x, self.y = separate(fun(bits, data_size), sample_len)        
            self.test_x, self.test_y = separate(fun(bits, data_size), sample_len)
        else:
            self.x, self.y = separate(fun(bits, data_size, args), sample_len)        
            self.test_x, self.test_y = separate(fun(bits, data_size, args), sample_len)
#        print self.x
#        print self.y
#        print self.test_x
#        print self.test_y

    def check(self, name, pre_fun, fit_fun = None):
        print 'predict with', name, ':'
        if fit_fun != None:
            fit_fun(self.x, self.y)
        pre = pre_fun(self.test_x)
#        print pre            
        correct = sum(pre == self.test_y)
        print '%d/%d = %lf' % (correct, len(self.test_y), correct * 1.0 / len(self.test_y))
