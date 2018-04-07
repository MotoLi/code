#coding:utf-8
import urllib2
import urllib

'''response = urllib2.urlopen("http://www.baidu.com")
print response.read()'''   #获取网站源码

#urlopen(url, data, timeout)
'''第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面'''


'''request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()'''


#POST方式传送
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values)
print data
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()


#GET方式传送
'''values={}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
print data

url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()'''



#设置Headers  Headers参考网页的代码的headers
'''url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
values = {'username':'cqc','password':'XXXX'}
headers = {'User-Agent':user_agent,'Referer':'http://www.zhihu.com/articles'}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()'''



#Proxy代理设置
#urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。
# 假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。
# 所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个
# 代理，网站君都不知道是谁在捣鬼了，这酸爽！
'''enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)'''


#Timeout设置
'''上一节已经说过urlopen方法了，第三个参数就是timeout的设置，可以设置等待
多久超时，为了解决一些网站实在响应过慢而造成的影响。
例如下面的代码,如果第二个参数data为空那么要特别指定是timeout是多少，写明形
参，如果data已经传入，则不必声明。
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
response = urllib2.urlopen('http://www.baidu.com',data,10)'''


#使用HTTP的PUT和DELETE方法


#使用Debuglog
'''可以通过下面的方法把 Debug Log 打开，这样收发包的内容就会在屏幕上打
印出来，方便调试，这个也不太常用，仅提一下
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')'''























