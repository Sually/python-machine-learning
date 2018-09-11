# -*- coding: utf-8 -*-
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

a = fib(4)
next(a)
next(a)
for i in a:
    print i