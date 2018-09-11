# -*- coding: utf-8 -*-
import time


def deco1(func):
    def wrapper(*args, **kargs):
        print 'deco start'
        start = time.time()
        func(*args, **kargs)
        end = time.time()
        print 'deco end'
        print 'the func execute time:', end-start
    return wrapper


def deco2(func):
    def wrapper(*args, **kargs):
        print 'deco2 start'
        func(*args, **kargs)
        print 'deco2 end'
    return wrapper


# deco2 means contains deco1
@deco2
@deco1
def printHello(name):
    time.sleep(1)
    print 'hello,', name

printHello('you')
