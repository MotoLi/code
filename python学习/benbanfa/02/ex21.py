# coding: utf-8

def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "将 %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "将 %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "将 %d / %d" %(a, b)
    return a / b

print "使用这些函数做些事情！"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "年龄：%d， 身高：%d， 体重：%d，IQ：%d" % (age, height, weight, iq)

print "这里有一个谜题"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "这就变成了", what,"你能手算出来吗?"