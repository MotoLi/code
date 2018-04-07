# coding=utf-8
from sys import argv

script, filename = argv

txt = open(filename)

print "这里有一个文件叫%s" % script
print txt.read()

filename_again = raw_input("再输入一次文件名>")

txt_again = open(filename_again)
txt_again.close()
print txt_again.read()