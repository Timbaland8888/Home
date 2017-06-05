# #!/usr/bin/env python
# #-*- coding:utf-8 -*-
# # __Arthur__=Timbaland
# # Email:422033564@qq.com
#
# import time as t
# class Mytime():
#     '''开始计时'''
#     def __init__(self):
#         self.unit=['年','月','日','时','分','秒']
#         self.prompt="未开始"
#         self.lasted=[]
#         self.begin=0
#         self.end=0
#     def __str__(self):
#         return self.prompt
#     __repr__=__str__
#     def start(self):
#         self.begin=t.localtime()
#         self.prompt = '提示:请先调用stop()停止计时'
#         print "计时开始"
#     '''停止计时'''
#     def stop(self):
#         if not self.begin:
#             print '请开始计时'
#         else:
#             self.end=t.localtime()
#             self._calc()
#             print '计时结束'
#     '''内部方法'''
#     def _calc(self):
#         self.lasted=[]
#         self.prompt='总共运行了'
#         for index in range(6):
#             self.lasted.append(self.end[index]-self.begin[index])
#             self.prompt+=(str(self.lasted[index])+self.unit[index])
#         print self.prompt
#
#
# p=Mytime()
# p.start()
# p.stop()
# a = [1,'222','rdfrse',('fggf',222)]\
import json
a ={'d':11,'5':5}
a.

# a.sort()
# print a ,'===================================='
# a.reverse()
# print a

















