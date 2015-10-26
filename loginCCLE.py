#-*- coding:UTF-8 -*-

import urllib,urllib2,cookielib
import os
import xml.etree.ElementTree as etree #xml解析类
import time

#伪装browser, for ccle, this need to be a modern brower
header =[('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'), ('Referer', 'https://shb.ais.ucla.edu/shibboleth-idp/profile/SAML2/Redirect/SSO'),('Host','ccle.ucla.edu'),('Origin','https://shb.ais.ucla.edu'),('Connection','keep-alive')]
header2 =[('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'), ('Referer', 'https://ccle.ucla.edu/'),('Host','ccle.ucla.edu'),('Connection','keep-alive')]
username = ''
passwd = ''
cookie = None #cookie对象
cookiefile = './cookies.dat' #cookie临时存放地
postdata = {}

class LoginCCLE:

    
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
        #cookie设置
        self.cookie = cookielib.MozillaCookieJar(cookiefile)
        if os.access(cookiefile, os.F_OK):
            self.cookie.load(ignore_discard=True)
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=1),
            urllib2.HTTPSHandler(debuglevel=1),
            urllib2.HTTPCookieProcessor(self.cookie)
        )
        self.opener2 = self.opener

        self.opener.addheaders = header
        self.login()
        self.cookie.save()
        self.download()

   #登陆    
    def login(self):       

        #请求参数设置
        postdata = {
            'username':self.username,
            'password':self.passwd,
            'type':1
            }
        postdata = urllib.urlencode(postdata)

        response = self.opener.open("https://ccle.ucla.edu/login/index.php", postdata)
        f = open('/Users/shaolei/Desktop/3rd year/side proj/python/ResponseFromCCLE.html','aw+')
        f.write(str(response.read()))
        f.close()
        print "this is the response.geturl/n" 
        print response.geturl()

    def download(self):

        self.opener2.addheaders = header2
        result = self.opener2.open("https://ccle.ucla.edu/my/")
        print "this is the result.geturl/n" 
        print result.geturl()
        result = str(result)
        f = open('/Users/shaolei/Desktop/3rd year/side proj/python/ccleResult.html','aw+')
        f.write(result)
        f.close()

#Demo
customUsername = raw_input('username:	')
customPasswd = raw_input('password:	')
print("Requesting......\n\n")
login = LoginCCLE(customUsername,customPasswd)

