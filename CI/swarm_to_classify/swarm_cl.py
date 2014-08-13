from numpy import *

class swarm_moving_classifier(object):
    
    def __init__(self, x, y,
        maxiter = 100, moving_speed = 1.0, 
        self_factor = 0.7, cul_factor = 0.15, anticul_factor = 0.35):
        '''assuming that the Y is in range(cl_n)'''            
      
#initialization      
        cl_n = len(set(y))
        n = x.shape[1]
        self.n = n
        swarms = map(lambda x: [], [0] * cl_n)
        for ind, ele in enumerate(x):
            swarms[y[ind]].append(biont(zeros(n), ele, y[ind]))
        r = random.rand            
        self.maxiter = maxiter
        
#iteration        
        culture = zeros((cl_n, n))
        anticul = zeros((cl_n, n))
        for iteration in xrange(maxiter):

            for ind, ele in enumerate(swarms):
                #calc the culture
                acc = zeros(n)
                for ele2 in ele:
                    acc += ele2.pos
#                culture = reduce(lambda x, y: x+y, ele) / mean(ele)
                culture[ind] = acc / len(ele) 
                #pre-calc the anti_culture
                anticul += tile(culture[ind], (cl_n, 1))
                anticul[ind] -= culture[ind]

            for cls in swarms:
                for ele in cls:
                    ele.move( moving_speed * 
                        (self_factor * ele.it * r()+ 
                         cul_factor * culture[ele.cl] * r()-
                         anticul_factor * anticul[ele.cl] * r() ))                   
            
#            print culture
        self.culture = culture                    
        self.cl_n = cl_n
    
    def predict(self, x):
        ans = []
        for ele in x:
            p = biont(zeros(self.n), ele, -1)                     
            for iteration in xrange(self.maxiter):
                p.move( p.it * random.rand())
#            print p                
#            print (tile(p.pos, (self.cl_n, 1)) - self.culture)
#            print  (tile(p.pos, (self.cl_n, 1)) - self.culture) ** 2 
#            print  ( (tile(p.pos, (self.cl_n, 1)) - self.culture) ** 2 ).sum(axis=1)
            ans.append ( ( (tile(p.pos, (self.cl_n, 1)) - self.culture) ** 2 ).sum(axis=1).argmin() )
        return array(ans)
                    

class biont(object):
    
    def __init__(self, pos, interest, kind):
        self.pos = pos
        self.cl = kind
        self.it = interest

    def __add__(self, obj):
        try:
#            print 'here'
            return self.pos + obj.pos 
        except:
#            print 'there'
            return self.pos + obj

    def __str__(self): 
        return 'biont:'+str(self.pos)
    
    def __repr__(self):
        return 'biont:'+str(self.pos)

    def move(self, update):
        self.pos += update
        

if __name__ == '__main__':   
    '''x = [[0,  1],
         [.5, 1],
         [1,  0],
         [1,  1],
         [2,  3],
         [3,  2],
         [3,  3],
         [3,  4]]
    y = [1,1,1,1,0,0,0,0]

    cl = swarm_moving_classifier(array(x), y)
    print cl.culture
    print cl.predict(array([[0,0],[3,3]]))'''    


    '''x = []
    y = []
    for line in open('testSet.txt'):
        t = map(float, line.strip().split('\t'))
        x.append(t[0:2])
        y.append(int(t[-1]))
#    print x
#    print y
    x = array(x)
    spInd = int(len(x) * 0.7)
    cl = swarm_moving_classifier(x[:spInd], y[:spInd])
    print cl.culture
    correct = (cl.predict(x[spInd:]) == y[spInd:]).sum()
    print 'correct: %d/%d = %lf' % ( correct, len(y[spInd:]), 1.0 * correct/len(y[spInd:]) )'''


    data = []
    for line in open('horseColicTraining.txt'):
        data.append(array(map(lambda x: float(x), line.strip().split('\t'))))
    test_data = []
    for line in open('horseColicTest.txt'):
        test_data.append(array(map(lambda x: float(x), line.strip().split('\t'))))
        
    data = array(data)
    test_data = array(test_data)

    x = data[:,:-1]
    y = map(int, data[:,-1])
    test_x = test_data[:,:-1]
    test_y = array(map(int, test_data[:,-1]))

    classifier = swarm_moving_classifier(x, y)
#    print test_x[0]
    print '%d/%d' % ((classifier.predict(test_x) == test_y).sum(), test_y.shape[0])

