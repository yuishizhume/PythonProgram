#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '--Yuidea--'

import requests,urllib2,cookielib
from bs4 import BeautifulSoup


url="http://www.baidu.com"

print"第一种方法:"
response1=urllib2.urlopen(url)
print response1.getcode()#返回200表示成功
print len(response1.read())#查看长度

print"第二种方法:"
request=urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")#伪装浏览器访问
response2=urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print"第三种方法:"
cj=cookielib.CookieJar()#创建cookie容器
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))#以容器作为参数创建一个opener
urllib2.install_opener(opener)#给urllib2安装opener
response3=urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())
print cj#打印cookie内容
print response3.read()#打印网页内容


#假装爬取到一个html_doc,作为实例研究
html_doc='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class='title'><b>The Dormouse's story</b></p>
<p class='story'>There were 3 little girl called
<a href="Http://example.com/elsie" class="sister" id="link1">Elise</a>
<a href="Http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="Http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''


#根据HTML网页字符串创建BeautifulSoup对象
soup=BeautifulSoup(
        html_doc,            #HTML文档字符串
        'html.parser',       #HTML解析器
        from_encoding='utf8' #HTML文档的编码
        )
#获取网页中所有链接
links=soup.find_all('a')
for link in links:#提取名称，url，文字
    print link.name,link['href'],link.get_text()
#获取特一对象，如Lacie的链接
link_1=soup.find('a',text='Lacie')
print link_1.name,link_1['href'],link_1.get_text()
#通过正则匹配，使用小段信息，搜到完整信息
import re#调用re正则匹配
link_2=soup.find('a',href=re.compile(r"ill"))
print link_2.name,link_2['href'],link_2.get_text()
#获取p段落文字
link_3=soup.find('p',class_='title')#class是python关键字，所以加_回避
print link_3.name,link_3.get_text()
