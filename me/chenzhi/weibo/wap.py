# -*- coding: utf-8 -*-
__author__ = 'chenzhi'

import urllib2
import urllib
import cookielib
import sys
import lxml.html as HTML


class Fetcher(object):
    def __init__(self, username=None, pwd=None, cookie_filename=None):
        self.cj = cookielib.LWPCookieJar()
        if cookie_filename is not None:
            self.cj.load(cookie_filename)
        self.cookie_processor = urllib2.HTTPCookieProcessor(self.cj)
        self.opener = urllib2.build_opener(self.cookie_processor, urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)
        self.username = username
        self.pwd = pwd
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
                        'Referer': '', 'Content-Type': 'application/x-www-form-urlencoded'}

    def get_rand(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0',
                   'Referer': ''}
        req = urllib2.Request(url, urllib.urlencode({}), headers)
        resp = urllib2.urlopen(req)
        login_page = resp.read()
        rand = HTML.fromstring(login_page).xpath("//form/@action")[0]
        print "rand", rand
        passwd = HTML.fromstring(login_page).xpath("//input[@type='password']/@name")[0]
        print "passwd", passwd
        vk = HTML.fromstring(login_page).xpath("//input[@name='vk']/@value")[0]
        print "vk", vk
        return rand, passwd, vk

    def login(self, username=None, pwd=None, cookie_filename=None):
        if self.username is None or self.pwd is None:
            self.username = username
            self.pwd = pwd
        assert self.username is not None and self.pwd is not None
        url = 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt='
        rand, passwd, vk = self.get_rand(url)
        data = urllib.urlencode({'mobile': self.username, passwd: self.pwd, 'remember': 'on', 'backURL': 'http://weibo.cn/', 'backTitle': '微博', 'vk': vk, 'submit': '登录', 'encoding': 'utf-8'})
        url = 'http://login.weibo.cn/login/' + rand
        req = urllib2.Request(url, data, self.headers)
        resp = urllib2.urlopen(req)
        page = resp.read()
        f = open("response.html", "w")
        f.write(page)
        if cookie_filename is not None:
            self.cj.save(filename=cookie_filename)
        elif self.cj.filename is not None:
            self.cj.save(filename=cookie_filename)
        else:
            print "cookie is null"
        print 'login success!'

    def fetch(self, url, data, timeout):
        req = urllib2.Request(url, data, headers=self.headers)
        return urllib2.urlopen(req, None, timeout).read()

if __name__ == '__main__':
    username = "xx@xx.com"
    password = "xx"
    fetcher = Fetcher(username, password)
    fetcher.login(cookie_filename="cookie.txt")
    home_url = 'http://weibo.cn/?vt=4'
    msg_url = 'http://weibo.cn/msg/?tf=5_010&vt=4'
    try:
        htmlContent = fetcher.fetch(msg_url, None, 5)
        f = open("final.html", "w")
        f.write(htmlContent)
    except Exception, e:
        print 'time out'
