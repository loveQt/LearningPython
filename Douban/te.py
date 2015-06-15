# -*- coding: utf-8 -*-
import urllib2
import codecs
import re
from bs4 import BeautifulSoup
url = 'http://weixin.sogou.com/gzh?openid=oIWsFt_gMcFjyaIvSAq9GCBa2M4U'
response = urllib2.urlopen(url)
html = response.read()
print html
# = urllib2.urlopen(url).read().decode('gbk', 'ignore').encode('utf-8')
thank = r' href="(http://mp.weixin.qq.com.*?) target="_blank"'
thanklist = re.findall(thank,html)

for each in thanklist:
    print (each)
