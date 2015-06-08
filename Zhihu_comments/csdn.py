import requests
import re
import urllib
import json
s = requests.session()
r = s.get('http://passport.csdn.net/account/login')
print r 
he = r.headers
#print type(he)
#print he
#print he['set-cookie']
#he = json.loads(he)
html = r.content
#print html
datavalue = r'value=".*?"'
valuelist = re.findall(datavalue,html)
#print valuelist
#print valuelist[3]
#print valuelist[4]
lt = valuelist[3]
execution = valuelist[4]
login_data = {'_eventId':'submit','execution':execution,'lt':lt,"password":'DUANxiaochen..!','rememberMe':'true',"username":'shmilydxc@vip.qq.com' }
login_data = urllib.urlencode(login_data)
cookie = he['set-cookie']
print login_data
header = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
    #'Host': "passport.csdn.net",
    #'Referer': "https://passport.csdn.net/account/login",
    #'Connection':'keep-alive',
    #'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    #'cookie':cookie,
    #'Accept-Encoding':'gzip, deflate',
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Length':'149',
    #'Content-Type':'application/x-www-form-urlencoded'
    #'X-Requested-With': "XMLHttpRequest"
        }
#print header
r = s.post('http://passport.csdn.net/account/login', data=login_data, headers=header)
print r
html = r.content
print html

