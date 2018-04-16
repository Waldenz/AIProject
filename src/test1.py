
import random

#print('Python', python_version())
print('Hello, World!')
'''
#dfdfdfd
sdfsdf

'''
"""
sdfsdfdf
sfsdfd
"""
print("some text,", end="")
print(' print more text on the same line')

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list);  # 输出完整列表
print (list[0]);  # 输出列表的第一个元素
print (list[1:3]);  # 输出第二个至第三个元素
print (list[2:]);  # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2);  # 输出列表两次
print (list + tinylist);  # 打印组合的列表

flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print ('welcome boss')    # 并输出欢迎信息
else:
    print (name)              # 条件不成立时输出变量名称

if (name =="luren"):
    print("luren");
else:
    print("else")

'''
#循环while
s = int(random.uniform(1,10))
#print(s)
m = int(input('输入整数:'))
while m != s:
    if m > s:
        print('大了')
        m = int(input('输入整数:'))
    if m < s:
        print('小了')
        m = int(input('输入整数:'))
    if m == s:
        print('OK')
        break;
'''
a="Python"
print(a[1:4])

from urllib.request import urlopen
url = 'https://www.baidu.com/'
html = urlopen(url).read()

print(html)