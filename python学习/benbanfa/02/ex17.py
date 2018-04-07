# coding:utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

indata = open(from_file).read()

print "输入的文件有 %d个字节" % len(indata)

print "输出文件存在吗？ %r" % exists(to_file)
print "准备好了吗？敲回车继续吧"
raw_input()

out_file = open(to_file, 'w').write(indata)

print "好啦，完成"

open(to_file,"w").close()
open(from_file).close()