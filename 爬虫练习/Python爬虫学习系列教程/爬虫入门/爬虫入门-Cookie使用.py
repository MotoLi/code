#coding:utf-8
import urllib2
import urllib
import cookielib

#获取Cookie保存到变量
#利用CookieJar对象实现获取cookie的功能，存储到变量中。
'''cookie = cookielib.CookieJar()   #申明一个cookiejar实例
handler = urllib2.HTTPCookieProcessor(cookie)  #创建cookie处理器
opener = urllib2.build_opener(handler) #通过handler构建opener
response = opener.open('http://www.baidu.com')，此时网站cookie会存到cookie这个变量中
for item in cookie:
    print 'Name=' + item.name
    print 'Value='+ item.value
    print type(item)
    print item
print type(cookie)
print cookie'''


#保存Cookie到文件
'''filename = 'cookie.txt'      #设置保存cookie的文件
cookie = cookielib.MozillaCookieJar(filename) #申明一个对象实例保存cookies
handler = urllib2.HTTPCookieProcessor(cookie) #创建cookie处理器
opener = urllib2.build_opener(handler)        #构建opener
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True) #保存到文件'''

#从文件中获取Cookie并访问
'''cookie = cookielib.MozillaCookieJar()  #创建实例对象
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True) #从文件中读取cookie内容到变量 这一步已经把cookie拿下来了
req = urllib2.Request("http://www.baidu.com")  #创建请求的request
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))#利用build_opener创建一个opener
response = opener.open(req)
print response'''


#利用cookie模拟网站登录
#创建一个带有cookie的opener，在访问登录的url时，将登录后的cookie保存下来，
# 然后利用这个cookie来访问其他网址
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)       #创建cookie实例
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'stuid':'201200131012','pwd':'23342321'})
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
result = opener.open(gradeUrl)
print result.read()










