# -*- coding:utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib

def search_by_google(keyword,page):
    browser = webdriver.Chrome()
    word = keyword  # 搜索关键词
    baseUrl = 'http://www.google.com/search'
    for i in range(page):
        data = {'q': word, 'start': i * 10}
        data = urllib.urlencode(data)
        url = baseUrl + '?' + data
        print url
        browser.get(url)
        html = browser.page_source
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



search_by_google("书包",5)