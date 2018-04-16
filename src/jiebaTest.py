import jieba
import jieba.analyse

# 清华大学分词
# http://thulac.thunlp.org/
# THULAC：一个高效的中文词法分析工具包

#加载自定义词典
jieba.load_userdict('userdict.txt')

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('./stopwordshit.txt')  # 这里加载停用词的路径
    emptyList=["\t","\r\n","\r","\n"]
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords and word not in emptyList:
            outstr += word+" "
    return outstr


s = '''在已经过去的七天里，互联网行业内的资本风起云涌。在对饿了么进行了长达数年的投资之后，
阿里巴巴终于还是不满足于仅仅身为第一大股东的身份，在4月初整个收购了饿了么，
从此每一份饿了么快递都带上了真正的“马氏血统”，只是不知道这样的外卖吃起来味道如何，'''
# cut = jieba.cut(s)
# print ('【Output】')
# print (','.join(cut))

# print (','.join(jieba.cut(s)))
print(seg_sentence(s))

# 提取关键词
def extract_tags(content,topk):
    content = content.strip()
    tags=jieba.analyse.extract_tags(content, topK=topk)
    return ','.join(tags)


f=open(r"D:\temp.txt",encoding="utf-8")
print("FileName:"+f.name)
alltext=f.read()
f.close()
# print ("AllText:"+alltext)
print ('【Tag Output】')
print(extract_tags(alltext,20))
# print ("【segment result:】")
# print(seg_sentence(alltext))
# print(",".join(jieba.cut(alltext.strip())))

# 提取关键词+权重值
# tags = jieba.analyse.extract_tags(alltext,20, withWeight=True)
# print ('【Tag with weight】')
# for tag in tags:
#     print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))

# TextRank 不过滤词性
rankResult=jieba.analyse.textrank(alltext, topK=20)
print ("【rankResult Output:】")
print(",".join(rankResult))
# 过滤词性
rankResult=jieba.analyse.textrank(alltext, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
# rankResult=jieba.analyse.textrank(alltext, topK=20, withWeight=False, allowPOS=('ns','vn', 'v'))
print ("【rankResult AllowPos Output:】")
print(",".join(rankResult))

def cuttest(test_sent):
    result = jieba.cut(test_sent)
    print("  ".join(result))


def testcase():
    cuttest("这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。")
    cuttest("我不喜欢日本和服。")
    cuttest("雷猴回归人间。")
    cuttest("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
    cuttest("我需要廉租房")
    cuttest("永和服装饰品有限公司")
    cuttest("我爱北京天安门")
    cuttest("abc")
    cuttest("隐马尔可夫")
    cuttest("雷猴是个好网站")

# testcase()
# jieba.set_dictionary("foobar.txt")
# print("================================")
# testcase()