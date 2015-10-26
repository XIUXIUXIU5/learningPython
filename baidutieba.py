# -*- coding: utf-8 -*-

import string, urllib2
import os

folderName = '/Users/shaolei/Desktop/3rd year/side proj/python/GDTieba/'   

if not os.path.exists(folderName):
    os.makedirs(folderName)

#定义百度函数
def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
    	sName = folderName + '第' + str(i) + '页' + '.html'#自动填充成六位的文件名
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......'
        f = open(sName,'aw+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()
 
bdurl = 'http://tieba.baidu.com/p/4065808261?pn='
begin_page = 1
end_page = 4

baidu_tieba(bdurl,begin_page,end_page)
