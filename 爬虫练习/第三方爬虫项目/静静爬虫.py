# -*- coding: utf-8 -*-
#静静爬虫
from selenium import webdriver
import codecs

url = 'http://www.ddc.net.cn/offerlist/1066646/517932.html'
#url = 'http://www.ddc.net.cn/qiye/______24_1.html'
browser = webdriver.Chrome()      #chrome浏览器的定位
#browser = webdriver.PhantomJS(executable_path="/Users/moto/phantomjs")
browser.get(url)


def pagelist():
    list = browser.find_elements_by_class_name('P37')

    l = 1
    for i in list:
        print l
        print i.text
        i.click()
        print i.get_attribute('href')
        l +=1
    print "完成"





#获取当前页面公司信息
def getcpinfoma():
   # cpname = browser.find_element_by_class_name('twoLtitle')
    cpname = browser.find_element_by_xpath("//p[@class='twoLtitle']")

    cpmana = browser.find_element_by_class_name('twoLtable')
    cpinfo = browser.find_element_by_class_name('pcont')

    print cpname.text
    print cpname.get_attribute("href")
    print cpmana.text
    print cpinfo.text
    #list = browser.find_element_by_class_name("twoLtable")  #获取元素焦点


    #for x in list :
    #    print "d%"  % x

    print "输出成功"




getcpinfoma()
browser.quit()
#list = browser.find_element_by_xpath("//p[@class='P37']")
