#coding:utf-8
import re


#re.match(pattern,string,flags=0)
"""#在起始位置匹配
print (re.match('www','www.runoob.com').span())
#不在起始位置匹配
print (re.match('com','www.runoob.com')) """

"""matchObj1 = re.match('www','www.runoob.com',re.M|re.I)
matchObj2 = re.match('com','www.runoob.com',re.M|re.I)

print matchObj1.group()
#print matchObj2.group() """


'''line = "Cats hahahah are jjjj smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) (.*)',line,re.M|re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()    #整个句子
    print "matchObj.group(1) : ", matchObj.group(1)  #第一项
    print "matchObj.group(2) : ", matchObj.group(2)
    print "matchObj.group(3) : ", matchObj.group(3)

else:
    print "No match!"  '''


#re.search(pattern, string, flags=0)
"""#在起始位置匹配
print (re.search('www','www.runoob.com').span())
#不在起始位置匹配
print (re.search('ob.c','www.runoob.com').span())"""



"""line = "Cats hahahah are jjjj smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*',line,re.M|re.I)

if searchObj:
    print "searchObj.group() : ", searchObj.group()    #整个句子
    print "searchObj.group(1) : ", searchObj.group(1)  #第一项
    print "searchObj.group(2) : ", searchObj.group(2)
  #  print "searchObj.group(3) : ", searchObj.group(3)

else:
    print "Nothing found!"   """



"""key = r"javapythonhtmlvhdl"
p1 = r"python"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,key)
print matcher1.group(0) """


#星号表示星号之前的字符有或者没有都行，有几次都行
"""key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"#胡编乱造的网址，别在意
p1 = r"https*://"#看那个星号！
pattern1 = re.compile(p1)
print pattern1.findall(key)  """


#正则表达式规避大小写
"""key = r"lalala<hTml>hello</Html>heiheihei"
p1 = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]>"
pattern1 = re.compile(p1)
print pattern1.findall(key)  """

#匹配出@后面的.+\.的结构，匹配完一个后接着匹配下一个，直到下一组不符合的,贪婪模式
"""key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.+\."#我想匹配到@后面一直到“.”之间的，在这里是hit
pattern1 = re.compile(p1)
print pattern1.findall(key)  """


#匹配出@后面的.+\.的结构，匹配完一个后接着匹配下一个，直到下一组不符合的,非贪婪模式，匹配一次就结束
"""key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.+?\."#我想匹配到@后面一直到“.”之间的，在这里是hit,?加载模拟字符后面
pattern1 = re.compile(p1)
print pattern1.findall(key)  """


#准确控制重复字符次数
"""key = r"saas and sas and saaas"
p1 = r"sa{1,2}s"
pattern1 = re.compile(p1)
print pattern1.findall(key) """


key = r"<html><body><h1>hello world</h1></body></html>"#这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=</h1>)"#  ?<=这个前缀    ?=后缀
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print matcher1.group(0)#打印出来










