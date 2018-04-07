#! /usr/bin/env python2.7
#coding:utf-8
import sys
import zlib
import chardet
import urllib
import urllib2
import cookielib

def main():
    reload( sys )
    page = 1
    url = 'http://cl.friu.pw/thread0806.php?fid=7&search=&page=' + str(page)

    values = {
            "form_field1":"value1",
            "form_field2":"TRUE",
             }

    post_data = urllib.urlencode(values)
    cj=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    headers ={"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:36.0) Gecko/20100101 Firefox/36.0",
              "Referer":"http://xxx.yyy.com/test0",
              "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "Accept-Language":"en-US,en;q=0.5",
              "Accept-Encoding":"gzip, deflate",
              "Connection":"keep-alive",
              # "Cookie":"QSession=",
              "Content-Type":"application/x-www-form-urlencoded",
              }
    req = urllib2.Request(url,post_data,headers)
    response = opener.open(req)
    content = response.read()
    gzipped = response.headers.get('Content-Encoding')
    if gzipped:
        html = zlib.decompress(content, 16+zlib.MAX_WBITS)
    else:
        html = content
    result = chardet.detect(html)
    print(result)
    print html.decode("utf8")

if __name__ == '__main__':
    main()