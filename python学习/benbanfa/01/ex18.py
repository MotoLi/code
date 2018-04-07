# -*- coding: utf-8 -*-
#这个就像argv一样
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#做一次精简
def print_two_again(arg1, arg2):
	print "arg1: %r,arg2: %r" % (arg1, arg2)
	
#用放一个参数
def print_one(arg1):
	print "arg1: %r" % arg1
	
#空的
def print_none():
	print "I got nothin'."
	
	
print_two("Moto","Li")
print_two_again("moto","Li")
print_one("First!")
print_none()