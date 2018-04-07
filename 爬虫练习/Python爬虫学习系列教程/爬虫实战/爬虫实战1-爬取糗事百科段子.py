#coding:utf-8
import urllib2
import urllib
import re
import thread
import time


class QSBK:
    #初始化方法定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0(compatibel;MSIE 5.5;Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False
    #拿到网页内容
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url,headers= self.headers)
            response = urllib2.urlopen(request)
            #将网页字符串赋值给pageCode
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败，错误原因",e.reason
                return None
    #对网页字符串做正则匹配
    def getPageItems(self,pageIndex):
        #调用getPage（）函数
        pageCode = self.getPage(pageIndex)
        #获取网页内容失败
        if not pageCode:
            print "页面加载失败"
            return None
        #设置正则表达式模式                                         用户名0                 年龄1              段子内容2                          评论数3
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?manIcon">(.*?)</div>.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>.*?',re.S)
        #与网页内容做比对，返回的是一个列表，里面的元素是每个匹配值的元组即：[（用户名，年龄，段子内容，评论数），（用户名，年龄，段子内容，评论数）】
        items = re.findall(pattern,pageCode)
        #print type(items)  :<type 'list'>
        #创建一个空列表
        pageStories = []
        #这里的item是一个元组
        for item in items:
            #print item
            #print type(item)
            haveImg = re.search("img",item[3])
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,"\n",item[1])
                                            #移除头尾的空格
                #将四个值生成一个列表为一个元素放入pageStories中
                pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip()])
            #返回这个列表
        return pageStories


    #将当前页面的所有故事存到stoties里面去，页面值自加一
    def loadPage(self):

        if self.enable == True:
            if len(self.stories) < 2:
                #把所有故事一个一个的以元组为元素的形式放到pageStories中
                pageStories = self.getPageItems(self.pageIndex)

                if pageStories:  #若为非空，则执行
                    #将列表作为一个元素放在列表stories的最后
                    self.stories.append(pageStories)
                    self.pageIndex += 1


    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人：%s\t发布人年龄：%s\t段子内容：%s\t赞：%s\n" %(page,story[0],story[1],story[2],story[3])

    def start(self):
        print u"正在读取糗事百科，按回车查看新段子，Q退出"
        self.enable = True  #默认是False
        self.loadPage()     #将故事作为元素赋值到stories最后一位
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]  #取出storise的第一位赋值给pageSroties
                nowPage +=1                    #当前页面值自加一
                del self.stories[0]             #删掉stories的第一个元素，即删掉当前页面的所有故事
                self.getOneStory(pageStories, nowPage)
                self.loadPage()


spider = QSBK()
spider.start()









"""page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0(compatibel;MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
    content = response.read().decode('utf-8')
    print ("11111")
   # pattern = re.compile('文章内容 -->(.*?)</div>', re.S)
   # pattern = re.compile('文章内容', re.S)
    #参考
    #pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</', re.S)
    pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>.*?',re.S)
    print ("22222")
    print pattern.findall(content)
    items = re.findall(pattern, content)
    print items
    print ("33333")
    for item in items:
        print item

except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
 """

