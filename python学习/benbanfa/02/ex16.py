# coding=utf-8
from sys import argv
script, filename = argv

print "我们马上要清除文件 %r" % filename

raw_input("确认吗？")

print "正在打开文件......"
target = open(filename, 'w')

print "文档已经清空了"
target.truncate()

print"现在我要你输入三行代码："

line1 = raw_input("第一行：")
line2 = raw_input("第二行：")
line3 = raw_input("第三行：")

print "现在我要将这些文件写进文档里面"


"""target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)"""

target.write(line1+"\n"+line2+"\n"+line3)

target = open(filename)

print target.read()

target.close()