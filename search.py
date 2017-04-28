# -*- coding:utf-8 -*-
import json
import urllib2
import re
import json

import math
from bs4 import BeautifulSoup
import jieba
import sys
import os
import csv

# used to load csv-type data
def loadCsv(filename):
  lines = csv.reader(open(filename, "rb"))
  dataset = list(lines)
  for i in range(len(dataset)):
    dataset[i] = [x for x in dataset[i]]
  return dataset

# get the index of word and the list of articles
def wordTag(word,dic):
    a=0
    for bb in dic:
        if bb[0] == word:
            return a,bb[1]
        a=a+1
    return -1,[]

# get the tf_idf of word
def find_tf_idf(this_article,dic_tf_idfs,tag):
    for bb in dic_tf_idfs:
        if bb[0] == this_article:
            tag_list_str=bb[1].replace('[','').replace(' ','')
            tf_idf_list_str = bb[2].replace('[', '').replace(' ', '')
            tag_list=tag_list_str.split(",")
            tf_idf_list = tf_idf_list_str.split(",")
            # print this_article
            # print tag_list
            # print tf_idf_list
            for i in range(len(tag_list)):
                # 要加 str,不然 str 和 int 不能比较
                if tag_list[i]==str(tag):
                    return tf_idf_list[i]
    return 0

# 得到 rank
def find_ranks(search_list):
    dic_idf = loadCsv("dic_idf.csv")
    dic_tf_idfs=loadCsv("dic_tf_idfs.csv")
    articles=[]
    grades=[]
    for word in search_list:
        tag,article_list=wordTag(word.encode('utf-8'),dic_idf)
        # print tag
        # print word
        if tag==-1:
            print word
            print "-----不在词表中"
        else:
            this_articles = article_list.split(",")
            for this_article in this_articles:
                tf_idf = find_tf_idf(this_article, dic_tf_idfs, tag)
                if this_article not in articles:
                    articles.append(this_article)
                    grades.append(float(tf_idf))
                else:
                    for i in range(len(articles)):
                        if articles[i] == this_article:
                            grades[i] = grades[i] + float(tf_idf)
    articles_and_grades=[]
    for index in range(len(articles)):
        articles_and_grades.append((grades[index],articles[index]))
    articles_and_grades.sort(reverse = True)
    print articles_and_grades
    if len(articles)>10:
        print "前十个文章"
        for j in range(10):
            print articles_and_grades[j][1]
    else:
        print "全部文章"
        for j in range(len(articles)):
            print articles_and_grades[j][1]



mysearch="审美"
search_list = jieba.cut(mysearch, cut_all=False)
# print search_list
find_ranks(search_list)

