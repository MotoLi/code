# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(f):   #函数调用方法
	print f.read() #函数执行内容,打印出读到的所有内容

def rewind(f):
	f.seek(0)     #这个是做什么的

def print_a_line(line_count,f):
	print line_count, f.readline() #打印某一行

current_file = open(input_file)

print "Frist let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

