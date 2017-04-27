# -*- coding:utf-8 -*-
import json
import urllib2
import re
import json
from bs4 import BeautifulSoup


# 下载文章内容
def downloadnews(link):
    result1 = re.match('http://www.view.sdu.edu.cn/new/\d{4}/\d{4}/\d*.html', link)
    if result1:
        print "yes"
        try:
            request = urllib2.Request(link)
            response = urllib2.urlopen(request)
            html = response.read()
            soup = BeautifulSoup(html)
            titles = re.findall('<h1>.*</h1>', str(soup))
            title=titles[0][4:-5]
            # print "题目:"+title
            hits= soup.find_all("span", class_="s12",id="hits")[0].string
            # print "点击次数:"+str(hits)
            date = re.findall('\d{4}-\d{2}-\d{2}', str(soup))[0]
            # print "日期:"+date
            contents = soup.find_all(id="content")[0]
            content = str(contents)
            content = re.sub(r'</?\w+[^>]*>', '', content)
            # print "文章:"
            # print content
            date = re.findall('\d{4}-\d{2}-\d{2}', str(soup))[0]
            writers = re.findall(r'<div class="text_c">.*</div>', str(soup))
            writer = str(writers[0])
            writer = re.sub(r'</?\w+[^>]*>', '', writer)
            # print "作者信息:"+writer
            d=dict(date=date,content=content,title=title,hits=hits,writer=writer)
            j_out=json.dumps(d)
            # print j_out
            f = open('articles/'+title+date+'.txt', 'w')
            # f_out2 = codecs.open('json_out2.txt', 'w', 'utf-8')
            # json.dump(j_out, f_out2, ensure_ascii=False, indent=4)
            out=title+"\n"+date+"\n"+str(hits)+"\n"+content+"\n"+writer
            f.write(out)
            f.close()
        except :
            print "download_err"

def news(html,linkset):
    print len(linkset)
    try:
        request = urllib2.Request(html)
        response = urllib2.urlopen(request)
        html = response.read()
        links1 = re.findall('http://www\.view\.sdu\.edu\.cn.*?.html', html)
        links2 = re.findall('\d{4}/\d{4}/\d*.html', html)
        links3 = re.findall('\w{3,6}/\d{1,3}.html', html)
        links4 = re.findall('new/.{3,5}/', html)
        for link in links1:
          if link not in linkset:
              linkset.add(link)
              news(link, linkset)
              print link
              downloadnews(link)
        for link in links2:
          link = "http://www.view.sdu.edu.cn/new/" + link
          if link not in linkset:
              linkset.add(link)
              news(link, linkset)
              print link
              downloadnews(link)
        for link in links4:
            link = "http://www.view.sdu.edu.cn/" + link
            if link not in linkset:
                linkset.add(link)
                news(link, linkset)
                print link
                downloadnews(link)
        for link in links3:
            link = "http://www.view.sdu.edu.cn/new/" + link
            if link not in linkset:
                linkset.add(link)
                news(link, linkset)
                print link
                downloadnews(link)
    except:
        print "err"
    return linkset


# request = urllib2.Request("http://www.view.sdu.edu.cn/")
# response = urllib2.urlopen(request)
# html=response.read()
# aa=re.findall('view\.sdu\.edu\.cn.*?.html',html)
# linkset=set([])
# print aa
# for link in aa:
#     linkset.add(link)
linkset=set([])
print len(news("http://www.view.sdu.edu.cn/",linkset))
# downloadnews("http://www.view.sdu.edu.cn/new/2017/0411/89635.html")