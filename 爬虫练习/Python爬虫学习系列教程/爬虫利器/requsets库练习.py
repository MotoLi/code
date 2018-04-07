#-*- coding:utf-8 -*-
import requests
import json

"""url = 'http://www.baidu.com'
r = requests.get(url)
print("11111")
print r.text
print("22222")  """


'''r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
print(r.status_code)  # 获取返回状态

print "11111111"
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
print(r.url)
print "22222222"

print(r.text)
print "33333333"  '''

'''r = requests.get("http://www.baidu.com")
print type(r)
print r.status_code
print r.encoding
print r.cookies
print r.content '''

'''payload = {'key2': 'value2','key1':'value1','key3':'value3'}
headers = {'content-type': 'application/json'}
r = requests.get("http://httpbin.org/get",params=payload,headers = headers)
print r.url  '''

'''payload = {'key1':'value1','key2':'value2'}
r = requests.post("http://httpbin.org/post",data = payload) 李浩
print r.text '''

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url,cookies=cookies)
print r.text

#print r.cookies
#print r.cookies['example_cookie_name']