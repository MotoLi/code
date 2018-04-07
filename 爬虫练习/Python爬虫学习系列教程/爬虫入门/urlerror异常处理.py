import urllib2
import urllib


#URLError
'''requset = urllib2.Request('http://www.xx1xxx.com')
try:
    print "0000"
    urllib2.urlopen(requset)
    print "111"
except urllib2.URLError,e:
    print e.reason
    print "2222"
    print e'''


#HTTPError
'''req = urllib2.Request('http://blog.csdn.net/cqrerercre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError,e:
    print e.code
    print e.reason'''


