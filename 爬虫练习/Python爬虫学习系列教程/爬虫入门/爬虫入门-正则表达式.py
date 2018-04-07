import urllib2
import urllib
import re
import thread
import time


page = 1
url = 'http://cl.friu.pw/thread0806.php?fid=7&search=&page=' + str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.4.0'
headers = {'User-Agent': user_agent}

'''headers = {"User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0",
           "Referer": "http://xxx.yyy.com/test0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.5",
           "Accept-Encoding": "gzip, deflate",
           "Connection": "keep-alive",
           # "Cookie":"QSession=",
           "Content-Type": "application/x-www-form-urlencoded",
           }'''
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)

#print response.encoding

#content = response.read().decode('utf-8')
#print content
print response.read()