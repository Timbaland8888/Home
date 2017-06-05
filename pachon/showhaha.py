#!/usr/bin/env python
#-*- coding:utf-8 -*-
# __Arthur__=Timbaland
# Email:422033564@qq.com
def add_count(func):
    def wrapper():
        print 'call func....'
        func()
    return wrapper

@add_count
def show_haha():
    print 'haha'

o = add_count(show_haha)
o()