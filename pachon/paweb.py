#!/usr/bin/env python
#-*- coding:utf-8 -*-
# __Arthur__=Timbaland
# Email:422033564@qq.com
from Tkinter import *
from ScrolledText import ScrolledText
import urllib,requests
import  sys ,re,threading
reload(sys)
sys.setdefaultencoding('utf-8')
url_name = []
a = 1
def get():
    global a
    hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    url = 'http://www.budejie.com/video/' +str(a)
    # var1.set('已经获取到第%s也视频'%(a))
    a +=1
    html = requests.get(url,headers=hd).text

    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)

    url_contents = re.findall(url_content,html)
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">'
        url_items = re.findall(url_reg,i)
        print url_items
        if url_items:
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</\w',re.S)
            name_items = re.findall(name_reg,i)
            for i,k in zip(name_items,url_items):
                url_name.append([i,k])

    return  url_name
b= get()
id =1
def wirte():
    global id
    while id <10:
        url_name = get()
        for i in url_name:
            urllib.urlretrieve(i[1],'video\\%s.mp4' %i[0])
            text.insert(END,str(id)+'.'+i[1]+'\n'+i[0] +'\n')
            url_name.pop(0)
            id +=1
        var1.set('视频链接和视频抓取完毕')
def start():
    th = threading.Thread(target=wirte)
    th.start()

root = Tk()
root.title('storeFront')
text = ScrolledText(root,font=('微软雅黑',10))
text.grid()
button = Button(root,text='开始爬取',font=('微软雅黑',10),command=start)
button.grid()
var1 =StringVar()
lable = Label(root,font=('微软雅黑',10),fg='red',textvariable=var1)
lable.grid()
var1.set('已准备......')
root.mainloop()


