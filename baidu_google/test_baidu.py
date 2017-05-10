#coding=utf-8
#python version：2.7
#author:sharpdeep

import urllib
import urllib2
import re
from bs4 import BeautifulSoup
from pyquery import PyQuery

def search_by_baidu(keyword,page):
    word = keyword  # 搜索关键词
    for i in range(page):
        baseUrl = 'http://www.baidu.com/s'
        data = {'wd': word, 'pn': i * 10}
        data = urllib.urlencode(data)
        url = baseUrl + '?' + data
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        html = response.read()
        soup = BeautifulSoup(html)
        print len(soup.find_all('div', class_='result c-container '))
        # 通过这个排除了百度图片,百度糯米,百度贴吧,百度百科等奇怪的东西
        for content in soup.find_all('div', class_='result c-container '):
            soup_part = BeautifulSoup(str(content))
            content1 = soup_part.find('h3', class_='t')
            title = re.findall(r'_blank">.*</a>', str(content1))
            link = re.findall(r'http://.*"', str(content1))
            if len(title) > 0:
                print title[0][8:-4]
                print link[0][0:-17]
            content2 = soup_part.find('div', class_='c-abstract')
            content2 = content2.text
            print content2
            print '............'



search_by_baidu("书包",5)

