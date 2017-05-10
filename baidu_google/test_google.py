# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import requests



proxies = {
  #  http://ip.zdaye.com/?adr=%C3%C0%B9%FA <-我去这个网上找免费代理
  "http": "http://192.208.184.210:8080",
  "https": "http://192.208.184.210:8080",
}
url='https://www.google.com/search?q=你好'
req_header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
  'Accept':'text/html;q=0.9,*/*;q=0.8',
  'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding':'utf-8',
  'Connection':'close',
  'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
 }
proxy = urllib2.ProxyHandler(proxies)
# 设置代理
opener = urllib2.build_opener(proxy)
req=urllib2.Request(url,None,req_header)
# 模拟浏览器
opener.addheaders=[('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]
urllib2.install_opener(opener)
response = urllib2.urlopen(req,timeout=3)
html=response.read()
print html


