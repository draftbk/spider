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

# get the index of word
def wordTag(word,dic):
    a=0
    for bb in dic:
        if bb[0] == word:
            return a
        a=a+1
    return -1


def add_to_dic(seg_list,myfile):
    print "............"+myfile
    dic = loadCsv("dic_idf.csv")
    a=0
    for word in seg_list:
        tag=wordTag(word.encode('utf-8'),dic)
        if tag==-1:
            dic.append([word.encode('utf-8'),myfile])
            dic.sort()
            print word
        else:
            if myfile not in dic[tag][1]:
                dic[tag][1]=dic[tag][1]+","+myfile
        a=a+1
    print a
    csvfile = file("dic_idf.csv", 'wb')
    writer = csv.writer(csvfile)
    writer.writerows(dic)

# 计算 idf
def get_idf(file_number):
    dic = loadCsv("dic_idf.csv")
    for bb in dic:
        file_list=bb[1].split(',')
        bb.append(math.log(file_number*1.0/len(file_list),10))
        print bb[0]
    csvfile = file("dic_idf.csv", 'wb')
    writer = csv.writer(csvfile)
    writer.writerows(dic)
path = "test" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
for myfile in files: #遍历文件夹
     # 文件命名
     # os.rename(path+'/'+file, path+'/'+str(x)+".txt")
     # 用正则表达式判断是否不是一些奇怪的影藏文件
     if re.match("\d*.txt",myfile):
         data = open(path + '/' + myfile)
         content = data.read()
         seg_list = jieba.cut(content, cut_all=False)
         add_to_dic(seg_list,myfile)
get_idf(len(files))
