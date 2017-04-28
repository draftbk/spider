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
            tag_list=bb[1]
            tf_idf_list = bb[2]
            i=0
            for mytag in tag_list:
                if mytag==tag:
                    return tf_idf_list[i]
                i=i+1
    return 0

# 得到 rank
def findranks(search_list):
    dic_idf = loadCsv("dic_idf.csv")
    dic_tf_idfs=loadCsv("dic_tf_idfs.csv")
    articles=[]
    grades=[]
    for word in search_list:
        tag,article_list=wordTag(word.encode('utf-8'),dic_idf)
        print tag
        print article_list
        if tag==-1:
            print word
            print "-----不在词表中"
        else:
            this_articles = article_list.split(",")
            for this_article in this_articles:
                tf_idf = find_tf_idf(this_article, dic_tf_idfs, tag)
                if this_article in articles:
                    articles.append(this_article)
                    grades.append(tf_idf)
                else:
                    for i in range(len(articles)):
                        if articles[i] == this_article:
                            grades[i] = grades[i] + tf_idf
    print articles
    print grades
mysearch="时代"
search_list = jieba.cut(mysearch, cut_all=False)
findranks(search_list)

