#!/usr/bin/env python
#-*- coding:utf-8 -*-
# __Arthur__=Timbaland
# Email:422033564@qq.com
# delimiter =','
# mylist  =['brazil','russiA','india','china']
# print delimiter.join(mylist)
# if __name__ == '__main__':
#     n =0
#     p =raw_input('ff')
#     for i in range(len(p)):
#          print ord('0')
#          # print type(ord(p[i]))
#         # n = n*8 + ord(p[i]) -ord('0')
#
#!/usr/bin/python

from Tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环