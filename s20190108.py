#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'test threading'

__auther__='liangtiaoyu'

import time,threading
'''
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n<5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)
	
print('thread %s is running ...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''

local_school = threading.local()

def process_student():
    std = local_school.s
    print('Hello, %s (in %s)' %(std, threading.current_thread().name))
	
def process_thread(name):
    local_school.s = name 
    process_student()
	
t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


