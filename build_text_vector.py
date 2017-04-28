# -*- coding:utf-8 -*-
import re

import math
import jieba
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
            return a,bb[2]
        a=a+1
    return -1

def build_tf(seg_list,myfile,dic):
    print "............"+myfile
    # 这两个保存词语编号以及数量
    word_tags=[]
    word_numbers = []
    word_idf=[]
    word_tf_idfs=[]
    length=0
    for word in seg_list:
        tag,idf=wordTag(word.encode('utf-8'),dic)
        length=length+1
        if tag not in word_tags:
            word_tags.append(tag)
            word_numbers.append(1)
            word_idf.append(idf)
        else:
            for i in range(len(word_tags)):
                if word_tags[i]==tag:
                    word_numbers[i]=word_numbers[i]+1
    for i1 in word_numbers:
        word_tf_idfs.append(i1*1.0*float(word_idf[i1])/length)
    dic_tf_part=[myfile,word_tags,word_tf_idfs]
    return dic_tf_part

path = "test" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
dic_tf=[]
for myfile in files: #遍历文件夹
     # 文件命名
     # os.rename(path+'/'+file, path+'/'+str(x)+".txt")
     # 用正则表达式判断是否不是一些奇怪的影藏文件
     if re.match("\d*.txt",myfile):
         data = open(path + '/' + myfile)
         content = data.read()
         seg_list = jieba.cut(content, cut_all=False)
         dic = loadCsv("dic_idf.csv")
         dic_tf.append(build_tf(seg_list, myfile,dic))
csvfile = file("dic_tf_idfs.csv", 'wb')
writer = csv.writer(csvfile)
writer.writerows(dic_tf)
