#!/usr/bin/env python
#-*- coding:UTF-8 -*-
# __Arthur__=Timbaland
# Email:422033564@qq.com
# import  re
# line = 'cats are smarter than dogs'
# matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
# if matchObj:
#     print matchObj.group(0)
#     print matchObj.group(1)
#     print matchObj.group(2)
#
# else:
#     print 'no match !!'
#
# import  re
# print (re.search('www','www.m.runoob.com').span())
# print (re.search('com','www.m.runoob.com').span())
# import  re
# line = 'cats are smarter than dogs'
# searchObj = re.search(r'(.*) are (.*?) (.*)',line,re.M|re.I)
# if searchObj:
#     print searchObj.group()
#     print searchObj.group(1)
#     print searchObj.group(2)
#     print searchObj.group(3)
# else:
#     print 'no match'
#
#
# import re
# line = 'cats are smarter than dogs'
# matchObj = re.match('dogs',line,re.M|re.I)
# if matchObj:
#     print matchObj.group()
#
#
# else:
#     print 'no match'
#
# '''使用searhmatch'''
# searchObj = re.search('dogs',line,re.M|re.I)
# if searchObj:
#     print searchObj.group()
#
# else:
#     print 'no match'
#
# #
# import re
# phone = '2004-959-666 #这是一个电话号码'
# num = re.sub(r'#.*$','',phone)
# print '电话号码是:%s', num
# num = re.sub(r'\D','',phone)
# print  num
import  re
def double(matched):
    value = int (matched.group('value'))
    return str(value*2)
s = 'A234GHFD567'
print (re.sub('',double,s))








































