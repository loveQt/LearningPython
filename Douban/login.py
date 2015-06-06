import urllib
import urllib2
import cookielib
import re


class DB(object):
    def __init__(self, email, passwd):
        self.url = 'http://www.douban.com/login'
        self.post = {
            'form_email':email,
            'form_password':passwd,
            'source':'index_nav'
            }
        cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        self.response = self.opener.open(self.url, urllib.urlencode(self.post))


    def login(self):
        if self.response.geturl() == self.url:
            print 'logining...'
            html = self.response.read()
            reg = r'src="(http://www.douban.com/misc/captcha.*?)"'
            imglist = re.findall(reg, html)
            urllib.urlretrieve(imglist[0], 'captcha.jpg')
            captcha = raw_input('captcha is: ')
            regid = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
            ids = re.findall(regid, html)
            self.post["captcha-solution"] = captcha
            self.post["captcha-id"] = ids[0]
            self.post["user_login"] = "登录"
            self.post["redir"] = 'http://www.douban.com/doumail/'
            self.response = self.opener.open(self.url, urllib.urlencode(self.post))
            if self.response.geturl() == "http://www.douban.com/doumail/":
                print 'login success !'

    def open_url(self):
        testurl = 'http://www.douban.com'
        req = urllib2.Request(testurl)
        #req.add_header()
        page = self.opener.open(req)
        html = page.read().decode('utf-8')
        print (html)
        #return html               

email = raw_input('Your email: ')
passwd = raw_input('Your passwd: ')   
#testurl = 'http://www.douban.com'
my = DB(email, passwd)         
my.login()
my.open_url()
#my.open_url()

