from numpy import *
import ann

def find(string, substr):
    next_arr = [0] * len(substr)

    j = -1
    next_arr[0] = -1
    for ind, ele in enumerate(substr):
        if ind == 0:
            continue
        while (j >= 0 and ele != substr[j+1]):
            j = next_arr[j]
        if ele == substr[j+1]:
            j += 1
        next_arr[ind] = j

#    print next_arr

    acc = 0
    j = -1
    for ind, ele in enumerate(string):
        while (j >= 0 and ele != substr[j+1]):
            j = next_arr[j]
        if ele == substr[j+1]:
            j += 1
        if j == len(substr)-1:
            acc += 1
            j = next_arr[j]

    return acc    

def separate(l, length):
    x = []
    y = []
    for i in xrange(len(l)- length):
        x.append(l[i: i+length])
        y.append(l[i+length])
    return x, y

def dec2bin(trys):
    if trys == 0:
        return [0]
    l = []
    while trys:
        l.insert(0, trys % 2)
        trys /= 2
    return l

if __name__ == '__main__':
    a = list(random.randint(0, 2, size=(4096)))

    print '''Part 1: counting the substring:'''
    for d in xrange(1, 6+1):
        if d == 1:
            l = [find(a,[0])]
        else:
            l = []        
        for i in xrange(2 ** (d-1), 2 ** d):            
            l.append(find(a, dec2bin(i)))
        print 'd = %d:'%d, l


    print '''Part 2: predict'''
#   failed
    pre = ann.NeuralNetworkClassifier([40, 40, 40])
    dataLen = 500
    x, y = separate(a, dataLen)
    pre.fit(array(x), y)

    test = list(random.randint(0, 2, size=(4096)))
    test_x, test_y = separate(test, dataLen)
    correct = sum(pre.predict(array(test_x))==array(test_y))
    print 'ann predict: ', correct, '/', len(test_y), '=', correct*1.0/len(test_y)

    ranpre = random.randint(0, 2, size=(len(test_y)))
    correct = sum(ranpre == array(test_y))
    print 'ran predict: ', correct, '/', len(test_y), '=', correct*1.0/len(test_y)
