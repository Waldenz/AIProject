import jieba
import jieba.analyse

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

# 提取关键词
def extract_tags(content,topk):
    content = content.strip()
    tags=jieba.analyse.extract_tags(content, topK=topk)
    return ','.join(tags)
