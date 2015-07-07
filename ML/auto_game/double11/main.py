#http://ubuntuforums.org/showthread.php?t=448160
#http://huawei.tmall.com/campaign.htm?spm=a2156.1384043.1998202575.1.EyinwC

from numpy import *
import gtk.gdk
import cPickle
from time import sleep
import matplotlib.pyplot as plt
from subprocess import Popen, PIPE

def get_blocks():
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    arr = pb.get_pixels_array()
    left = arr[425:535, 679:759]
    right = arr[425:535, 840:920]

    return left, right

def label():
    ban = []
    good = []
    while 1:
        left, right = get_blocks()

        plt.imshow(left)
        plt.show()
        ans = raw_input('ban or good? ')
        if ans == 'ban':
            ban.append(left)
        if ans == 'exit':
            break;

        plt.imshow(right)
        plt.show()
        ans = raw_input('ban or good? ')
        if ans == 'ban':
            ban.append(right)
        if ans == 'exit':
            break;

    cPickle.dump((ban, good), open('list.dat', 'wb'))


def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

def key_left():
    keypress('''key Left
''')

def key_right():
    keypress('''key Right
''')


if __name__ == '__main__':
    ban, good = cPickle.load(open('list.dat', 'rb'))
    ban = [ban[0], ban[2], ban[-1], ban[-2]]

    while 1:
        left, right = get_blocks()

        lmin = min(map(lambda x: ((left-x)**2).sum(), ban))
        rmin = min(map(lambda x: ((right-x)**2).sum(), ban))

        if lmin > rmin:
            key_left() 
        else:
            key_right() 
        sleep(0.219)
