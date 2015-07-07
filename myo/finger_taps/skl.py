import cPickle
import numpy as np
from sklearn import svm
from sklearn.externals import joblib


if __name__ == '__main__':
    x, y = cPickle.load(open('./data/data.npy', 'r')) 
    x = x.reshape(x.shape[0], -1)
    y = np.asarray(y, dtype ='int32') 
    print x.shape

    i = int(y.shape[0] * 0.7)
    train_x = x[:i]
    train_y = y[:i]
    test_x = x[i:]
    test_y = y[i:]

    if 1: # training

        clf = svm.SVC(kernel='rbf')
        print 'training...'
        clf.fit(train_x, train_y)
        joblib.dump(clf, 'clf.pkl')
    
    if 1: # testing
        clf = joblib.load('clf.pkl')
        res = clf.predict(test_x)
        print '%d / %d ' % ( (test_y != res).sum(), test_y.shape[0])
