# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import requests



proxies = {
  #  http://ip.zdaye.com/?adr=%C3%C0%B9%FA <-我去这个网上找免费代理
  "http": "http://54.243.10.147:8080",
  "https": "http://54.243.10.147:8080",
}
url='https://www.google.com/search?q=简书'
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
soup = BeautifulSoup(html)
print soup.title.text
for content in soup.find_all('div', class_='g'):
  try:
    print content.find('h3', class_='r').text
    print content.find('cite', class_='_Rm').text
    print content.find('span', class_='st').text
    print '.........................'
  except:
    print '异常网页'
    print '.........................'


# # -*- coding:utf-8 -*-
# import urllib
# import urllib2
# import re
# from bs4 import BeautifulSoup
# import requests
#
#
# def search_by_google(keyword,page):
#   word = keyword  # 搜索关键词
#   baseUrl = 'http://www.google.com/search'
#   proxies = {
#     #  http://ip.zdaye.com/?adr=%C3%C0%B9%FA <-我去这个网上找免费代理
#     "http": "http://45.59.157.55:8080",
#     "https": "http://45.59.157.55:8080",
#   }
#   req_header = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
#     'Accept': 'text/html;q=0.9,*/*;q=0.8',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#     'Accept-Encoding': 'utf-8',
#     'Connection': 'close',
#     'Referer': None  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
#     }
#   # 设置代理
#   proxy = urllib2.ProxyHandler(proxies)
#   opener = urllib2.build_opener(proxy)
#   # 模拟浏览器
#   opener.addheaders = [('User-agent',
#                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]
#   urllib2.install_opener(opener)
#   for i in range(page):
#     data = {'q': word, 'start': i * 10}
#     data = urllib.urlencode(data)
#     url = baseUrl + '?' + data
#     req = urllib2.Request(url, None, req_header)
#     response = urllib2.urlopen(req, timeout=3)
#     html = response.read()
#     print html
#     soup = BeautifulSoup(html)
#     print soup.title.text
#     for content in soup.find_all('div', class_='g'):
#       try:
#         print content.find('h3', class_='r').text
#         print content.find('cite', class_='_Rm').text
#         print content.find('span', class_='st').text
#         print '.........................'
#       except:
#         print '异常网页'
#         print '.........................'
#
# search_by_google("书包",5)
