# 自动摘要
# MMR的全称为Maximal Marginal Relevance ，中文名字为最大边界相关法或者最大边缘相关。

# -*- coding: utf-8 -*-
import sys
import os
import re
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import operator
import jiebahelper


print(sys.path)
f = open(r'./stopwordshit.txt',encoding="utf-8")  # 停止词
stopwords = f.readlines()
stopwords = [i.replace("\n", "") for i in stopwords]


def cleanData(name):
    setlast = jieba.cut(name)
    seg_list = [i.lower() for i in setlast if i not in stopwords]
    return " ".join(seg_list)

demotext="米家行车记录仪正式发布，告别驾驶孤单。继上周70迈智能"
print(cleanData(demotext))
print(jiebahelper.seg_sentence(demotext))

def calculateSimilarity(sentence, doc):  # 根据句子和句子，句子和文档的余弦相似度
    if doc == []:
        return 0
    vocab = {}
    for word in sentence.split():
        vocab[word] = 0  # 生成所在句子的单词字典，值为0

    docInOneSentence = '';
    for t in doc:
        docInOneSentence += (t + ' ')  # 所有剩余句子合并
        for word in t.split():
            vocab[word] = 0  # 所有剩余句子的单词字典，值为0

    cv = CountVectorizer(vocabulary=vocab.keys())

    docVector = cv.fit_transform([docInOneSentence])
    sentenceVector = cv.fit_transform([sentence])
    return cosine_similarity(docVector, sentenceVector)[0][0]


data = open(r"d:\temp.txt",encoding="utf-8")  # 测试文件
texts = data.readlines()  # 读行
texts = [i[:-1] if i[-1] == '\n' else i for i in texts]

sentences = []
clean = []
originalSentenceOf = {}

import time

start = time.time()

# Data cleansing
for line in texts:
    parts = line.split('。')[:-1]  # 句子拆分
    #   print (parts)
    for part in parts:
        cl = cleanData(part)  # 句子切分以及去掉停止词
        #       print (cl)
        sentences.append(part)  # 原本的句子
        clean.append(cl)  # 干净有重复的句子
        originalSentenceOf[cl] = part  # 字典格式
setClean = set(clean)  # 干净无重复的句子

# calculate Similarity score each sentence with whole documents
scores = {}
for data in clean:
    temp_doc = setClean - set([data])  # 在除了当前句子的剩余所有句子
    score = calculateSimilarity(data, list(temp_doc))  # 计算当前句子与剩余所有句子的相似度
    scores[data] = score  # 得到相似度的列表
    # print score

# calculate MMR
n = 25 * len(sentences) / 100  # 摘要的比例大小
alpha = 0.7
summarySet = []
while n > 0:
    mmr = {}
    # kurangkan dengan set summary
    for sentence in scores.keys():
        if not sentence in summarySet:
            mmr[sentence] = alpha * scores[sentence] - (1 - alpha) * calculateSimilarity(sentence,
                                                                                         summarySet)  # 公式
    selected = max(mmr.items(), key=operator.itemgetter(1))[0]
    summarySet.append(selected)
    #   print (summarySet)
    n -= 1

# rint str(time.time() - start)

print('\nSummary:\n')
for sentence in summarySet:
    print(originalSentenceOf[sentence].lstrip(' '))
print('=============================================================')
print('\nOriginal Passages:\n')