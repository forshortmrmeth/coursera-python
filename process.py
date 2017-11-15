import os
import time

if __name__ == '__main__':
    pid = os.fork()
    '''
    Если pid == 0, 
    то это дочерний процесс, полученный из os.fork()
    '''
    if pid == 0:
        while True:
            print('Child process', os.getpid())
            time.sleep(2)
    else:
        print('This is main (parent) process: ', os.getpid())
        tup = os.wait()
        print(tup)
