#coding:utf-8
import urllib2
import urllib
import re
#贴吧网址完成版1：http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1
#贴吧网址完整版2：https://tieba.baidu.com/p/5135834448?see_lz=1&pn=1

class BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '？see_lz=' + str(seeLZ)

        #提取页面内容
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print "11111"
            print response.read()
            print "22222"
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接失败，错误原因",e.reason
                return None
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.gtoup(1).strip()
        else:
            return None
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1)
        else:
            return None
    def getContent(self,page):
        page = self.getPage(1)
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.finall(pattern,page)
        for item in items:
            print item




baseURL = "https://tieba.baidu.com/p/5135834448"
bdtb = BDTB(baseURL,1)
bdtb.getPage(1)
