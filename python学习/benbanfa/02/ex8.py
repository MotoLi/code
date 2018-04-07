# coding=utf-8
fomatter = " %s  %r %r %r"  #r在引用字符串的时候会保留字符串的单引号

hehe = "one"
print fomatter % (1, 2, 3, 4)
print fomatter % (hehe, "two", "three", "four")
print fomatter % (True, False, False, True)
print fomatter % (fomatter, fomatter,fomatter, fomatter)