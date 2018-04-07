# -*- coding: utf-8 -*-
from selenium import webdriver

import codecs

'''url = 'http://cl.friu.pw/thread0806.php?fid=7&search=&page='  '''
url = 'http://cl.friu.pw/thread0806.php?fid=7&search=&page='
'''chromedriver = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"  '''
browser = webdriver.Chrome()
file_output = codecs.open('22thefile.csv','w', 'utf_8_sig')

for i in xrange(1,100):
    browser.get(url+str(i))
    print i
    l = 1
    List = browser.find_elements_by_xpath("//h3/a[@target='_blank']")
    for x in List:
        print "%d ----- %d" % (i,l)
        l += 1
        file_output.write(x.text+','+x.get_attribute('href'))
file_output.close()

