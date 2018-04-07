# -*- coding: utf-8 -*-
print "How old are you?",
age = raw_input()   # 等待输入函数
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
     age, height, weight)