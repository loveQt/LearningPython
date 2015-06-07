# -*- coding: utf-8 -*-
import requests
import ConfigParser
import re
from bs4 import BeautifulSoup
import xlwt
def login():
    Zhihu = 'http://www.zhihu.com/'
    Login_url = Zhihu + 'login'
    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")
    cookies = cf._sections['cookies']

    email = cf.get("info", "email")
    password = cf.get("info", "password")
    cookies = dict(cookies)
    global s
    s = requests.session()
    login_data = {"email": email, "password": password}
    header = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
    'Host': "www.zhihu.com",
    'Referer': "http://www.zhihu.com/",
    'X-Requested-With': "XMLHttpRequest"
        }
    r = s.post(Login_url, data=login_data, headers=header)
login()
ans_id = raw_input('input ans_id：')
comment_num = raw_input('input comment_num：')
url = 'http://www.zhihu.com/node/AnswerCommentListV2?params={"answer_id":"'+ans_id+'"}'
#print url
h = s.get(url)
html = h.content.encode('utf-8')
book = xlwt.Workbook(encoding = 'utf-8',style_compression=0)
sheet = book.add_sheet('data',cell_overwrite_ok = True)
soup = BeautifulSoup(html)
#print soup
for i in range(0,int(comment_num)*2-1,2):
    j = i/2
    try:
        b = soup.contents[i].contents[5]
        #print b
        c1 = b.contents[1]
        c1 = str(c1.text).split('\n')
        c2 = b.contents[3]
        #print c1[1]
        sheet.write(j,0,c1[1])
        #print c1[2]
        sheet.write(j,1,c1[2])
        #print c2.text
        sheet.write(j,3,c2.text)
    except:
        print 'error'
book.save(r'.\\'+str(ans_id)+'comment.xls')
