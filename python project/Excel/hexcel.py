#!/usr/bin/env python
#-*- coding:utf-8 -*-
# __Arthur__=Timbaland
# Email:422033564@qq.com

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)
def add(a, b):
   return Coordinate(a.x + b.x, a.y + b.y)
def sub(a, b):
   return Coordinate(a.x - b.x, a.y - b.y)
one = Coordinate(100, 200)
print(one)
two = Coordinate(300, 200)
add(one, two)
# Coord: {'y': 400, 'x': 400}