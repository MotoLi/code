# coding=utf-8
x = "有 %d 种类型的人" % 10
binary = "二进制"
do_not = "不"
y = "那些知道 %s 和那些 %s 知道的" % (binary, do_not)

print x
print y

print "我说了：%r" % x
print "我也说了 '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "左边有一个"
e = "右边也有一个"

print w + e