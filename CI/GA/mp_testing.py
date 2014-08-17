import multiprocessing as mp 
import time

def execute(qin, qout):
    inlock.acquire()
    while qin.empty():
        inlock.wait()
    t = qin.get()
    inlock.release()

    t = t+1

    outlock.acquire()
    while qout.full():
        outlock.wait()
    qout.put(t)
    outlock.release()

def put_mission(qin, q):
    l = len(q)
    ind = 0
    while ind < l:
        inlock.acquire()
        while qin.full():
            qin.wait()
        while ind < l and not qin.full():
            qin.put(q[ind])
            ind += 1
        inlock.notify_all()
        inlock.release()

def get_result(qout):
    count = 0
    while count < 1000:
        outlock.acquire()
        while qout.empty():
            outlock.wait()
        while not qout.empty():
            print qout.get()
        outlock.notify_all()
        outlock.release()

inlock = mp.Condition()
outlock = mp.Condition()
qin = mp.Queue()
qout = mp.Queue()

tasks = [mp.Process(target = execute, args=(qin, qout)) for i in range(2)]
tasks = tasks + [mp.Process(target = put_mission, args=(qin, range(1000))),
                 mp.Process(target = get_result, args=(qout,))]
for task in tasks:
    task.start()
for task in tasks:
    task.join()

