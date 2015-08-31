__author__ = 'chenzhi'

import re
import json
import urllib
import base64
import rsa
import binascii
import urllib2
import cookielib

def sServerData(serverData):
    # Search the server time & nonce from server data
    p = re.compile('\((.*)\)')
    jsonData = p.search(serverData).group(1)
    data = json.loads(jsonData)
    serverTime = str(data['servertime'])
    nonce = data['nonce']
    pubkey = data['pubkey']#
    rsakv = data['rsakv']#
    print "Server time is:", serverTime
    print "Nonce is:", nonce
    return serverTime, nonce, pubkey, rsakv

def sRedirectData(text):
    p = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
    loginUrl = p.search(text).group(1)
    print 'loginUrl:', loginUrl
    return loginUrl

def PostEncode(userName, passWord, serverTime, nonce, pubkey, rsakv):
    # Used to generate POST data
    encodedUserName = GetUserName(userName)
    encodedPassWord = get_pwd(passWord, serverTime, nonce, pubkey)
    postPara = { 'entry': 'weibo', 'gateway': '1', 'from': '', 'savestate': '7', 'userticket': '1',
                 'ssosimplelogin': '1', 'vsnf': '1', 'vsnval': '', 'su': encodedUserName, 'service': 'miniblog',
                 'servertime': serverTime, 'nonce': nonce, 'pwencode': 'rsa2', 'sp': encodedPassWord,
                 'encoding': 'UTF-8', 'prelt': '115', 'rsakv': rsakv,
                 'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                 'returntype': 'META' }
    postData = urllib.urlencode(postPara)
    return postData

def GetUserName(userName):
    # Used to encode user name
    userNameTemp = urllib.quote(userName)
    userNameEncoded = base64.encodestring(userNameTemp)[:-1]
    return userNameEncoded

def get_pwd(password, servertime, nonce, pubkey):
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537)
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    passwd = rsa.encrypt(message, key)
    passwd = binascii.b2a_hex(passwd)
    return passwd

class Fetcher:
    def __init__(self, user, pwd, enableProxy = False):
        print "Initializing WeiboLogin..."
        self.userName = user
        self.passWord = pwd
        self.enableProxy = enableProxy
        self.serverUrl = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683"
        self.loginUrl = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)"
        self.postHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}

def Login(self):
    self.EnableCookie(self.enableProxy)
    serverTime, nonce, pubkey, rsakv = self.GetServerTime()
    postData = PostEncode(self.userName, self.passWord, serverTime, nonce, pubkey, rsakv)#
    print "Post data length:\n", len(postData)
    req = urllib2.Request(self.loginUrl, postData, self.postHeader)
    print "Posting request..."
    result = urllib2.urlopen(req)
    text = result.read()
    try:
        loginUrl = sRedirectData(text)
        urllib2.urlopen(loginUrl)
    except:
        print 'Login error!'
        return False
    print 'Login sucess!'
    return True

def EnableCookie(self, enableProxy):
    # Enable cookie & proxy (if needed).
    cookiejar = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cookiejar)
    if enableProxy:
        proxy_support = urllib2.ProxyHandler({'http':'http://xxxxx.pac'})
        opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)
        print "Proxy enabled"
    else:
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

def GetServerTime(self):
    # Get server time and nonce, which are used to encode the password
    print "Getting server time and nonce..."
    serverData = urllib2.urlopen(self.serverUrl).read()
    print serverData
    try:
        serverTime, nonce, pubkey, rsakv = sServerData(serverData)
        return serverTime, nonce, pubkey, rsakv
    except:
        print 'Get server time & nonce error!'
        return None

def fetch(self, url, timeout) :
    req = urllib2.Request(url, headers=self.postHeader)
    return urllib2.urlopen(req, None, timeout).read()

if __name__ == '__main__':
    username = 'xx@xx.com'
    passwd = 'xxxx'
    fetcher = Fetcher(username, passwd)
    if fetcher.Login():
        print "Login success!"
    seed_url='http://weibo.com/p/1006061771925961/weibo'
    try:
        htmlContent = fetcher.fetch(seed_url, 3)
    except Exception, e:
        print 'time out'
