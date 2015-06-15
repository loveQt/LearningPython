# -*- coding: utf-8 -*-
import urllib
import urllib2

def login(self, username, password, questionid=0, answer=''):
    postdata = {
        #'loginfield': config.LOGINFIELD,
        'username': '虚心若愚',
        'password': 'DUANxiaochen0',
        'questionid': questionid,
        'answer': answer,
        'referer' : 'http://rs.xidian.edu.cn/'
        #'cookietime': config.COOKIETIME,
    }

    # 取得登录成功/失败的提示信息
    self.operate = self._get_response(config.LOGINURL, postdata)
    '''
     print self.operate.read()
    reqmovie = urllib2.Request(
        url="http://rs.xidian.edu.cn/bt.php?mod=browse&c=10"
     )
     MOVIE = self.opener.open(reqmovie).read()
     print  MOVIE
     '''
    login_tip_page = self.operate.read()

     # 显示登录成功/失败信息
    if 'succeedhandle_login' in login_tip_page:
        self.formhash = self._get_formhash(self._get_response(config.HOMEURL).read())
        print '登录成功'
        return True
    else:
        print '无法获取登录状态'
        return False
