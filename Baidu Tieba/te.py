# -*- coding: utf-8 -*-
import urllib2
import codecs
from bs4 import BeautifulSoup
url = 'http://finance.sina.com.cn/stock/t/20150413/010021937376.shtml'
response = urllib2.urlopen(url).read().decode('gbk','ignore')
print response
# = urllib2.urlopen(url).read().decode('gbk', 'ignore').encode('utf-8')
