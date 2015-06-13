import urllib
import urllib.request
import re


url = 'http://www.zhihu.com/answer/15024185/voters_profile?total=138&offset=30&follows=9fnQNBOLLln6knzZv17KzONKTRYjrQI10z62gAE='
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
page = urllib.request.urlopen(req)
html = page.read().decode('utf-8')
print (html)
#print(html.decode('unicode-escape'))

'''
#获取人名 ×
#待用name = r'title=\\".+?"'
#错误name = r'\\">\\.+?</a>\\n<span class=\\"bio hidden-phone\\">'
namelist = re.findall(name,html)
l2 = []
[l2.append(i) for i in namelist if not i in l2]
for each in l2:
    print (each)
'''
'''
#获取点赞数√
votes = r'[_a-zA-Z0-9_]{0,10} \\u8d5e\\u540c'
voteslist = re.findall(votes,html)

for each in voteslist:
    print (each)
'''
'''
#获取感谢数√
thank = r'[_a-zA-Z0-9_]{0,10} \\u611f\\u8c22'
thanklist = re.findall(thank,html)

for each in thanklist:
    print (each)
'''
'''
#获取提问数√
ques = r'[_a-zA-Z0-9_]{0,10} \\u63d0\\u95ee'
queslist = re.findall(ques,html)

for each in queslist:
    print (each)
'''
'''
#获取回答数√
ans = r'[_a-zA-Z0-9_]{0,10} \\u56de\\u7b54'
anslist = re.findall(ans,html)

for each in anslist:
    print (each)
'''

#获取个人主页地址
vpage = r'http://www.zhihu.com/people/..{0,40}\\" target'
vpagelist = re.findall(vpage,html)

for each in vpagelist:
    print (each)

#<a title=\"\u7530\u4f2f\u5149\"
#\"\u7530\u4f2f\u5149

