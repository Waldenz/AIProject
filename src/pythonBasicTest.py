
# python3 中map返回迭代器
a=map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(a))

path='./stopwordshit.txt'
with open(path,encoding="utf-8") as f:
    # temp=f.readlines()
    # print(temp[:5])
    stopwords=list(map(lambda x: x.strip(), f.readlines()))
    # stopwords = filter(lambda x: x, temp)
    stopwords.extend([' ', '\t', '\n'])
    ret=frozenset(stopwords)
#  print(ret)
print("End")