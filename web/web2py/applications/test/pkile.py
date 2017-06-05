#!/usr/bin/env python
# from urllib2 import Request
# from urllib2 import urlopen
# req = Request("file:///C:/Users/Administrator/Pictures/Saved%20Pictures/1.PNG")
# response = urlopen(req)
# html = response.read()
# with open('C:/Users/Administrator/Desktop/2.png','wb') as f:
#         f.write(html)
#
#
# print req.get_full_url()
from urllib2 import Request,urlopen
from urllib import urlencode
from json import loads
contents = input()
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=fanyi.logo'
data={}
data['type']='AUTO'
data['i']= contents
data['doctype']='json'
data['xmlVersion']='1.8'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['action']='FY_BY_CLICKBUTTON'
data['typoResult']='true'

data = urlencode(data).encode('utf-8')

response = urlopen(url,data)

html = response.read().decode('utf-8')
print html
targ = loads(html)
print targ.values()[2][0][0]['tgt']

