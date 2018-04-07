#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains




'''调用浏览器打开网页'''
url = 'http://www.baidu.com'
##chromedriver = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"
driver = webdriver.Chrome()
driver.get(url)

'''模拟提交提交搜索功能'''
#url = 'http://www.baidu.com'
#driver = webdriver.Chrome()
#driver.get("http://www.python.org")      # WebDriver 会等待页面完全加载完成之后才会返回，即程序会等待页面的所有内容加载完成，JS渲染完毕之后才继续往下执行
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")      #输入字符串
#elem.send_keys(Keys.RETURN)  #输入回车
#print driver.page_source    #打印出网页源代码


'''把搜索、输入封装成类'''
#class PythonOrgSearch(unittest.TestCase):
#    def setUp(self):
#        self.driver = webdriver.Chrome()

#    def test_search_in_python_org(self):
#        driver = self.driver
#        driver.get("http://www.python.org")
#        self.assertIn("Python", driver.title)
#        elem = driver.find_element_by_name("q") #实例name为q的元素
#        elem.send_keys("pycon")     #向q输入pycon
#        elem.send_keys(Keys.RETURN)  #向q输入回车
#        assert "No results found." not in driver.page_source

#    def tearDown(self):
#        self.driver.close()  #关闭当前选项卡
#        #self.driver.quit()   #关闭浏览器


#if __name__ == "__main__":
#    unittest.main()





'''获取输入框'''
#<input type="text" name="passwd" id="passwd-id" />
#url = 'http://www.baidu.com'
#driver = webdriver.Chrome()
#driver.get(url)

#有如下几种方式去获取它：
#elem = driver.find_element_by_id("passwd-id")
#elem1 = driver.find_element_by_name("passwd")
#elem2 = driver.find_element_by_tag_name("input")
#elem3 = driver.find_element_by_xpath("//input[@id='passwd-id']") #如果有多个元素匹配了 xpath，它只会返回第一个匹配的元素。如果没有找到，那么会抛出 NoSuchElementException 的异常

#elem.send_keys(u'的蓝')  #输入内容
#elem.send_keys("and some",Keys.RETURN) #点击按键
#elem.clear()  #清理输入的内容


'''填充表单'''
url = 'http://www.python.org'
driver = webdriver.Chrome()
driver.get(url)

#下拉选项框的处理：通过循环将所有选项框都点击一下
#elem = driver.find_element_by_xpath("//select[@name='name']")
#all_options = elem.find_element_by_tag_name("option")
#for option in all_options:  #每一个选项框都点一下
#    print ("Value is: %s" % option.get_atrribute("value"))
#    option.click()


'''元素拖拽'''
#elem = driver.find_element_by_name("source")
#target = driver.find_element_by_name("target")


#action_chains = ActionChains(driver)
#action_chains.drag_and_drop(elem, target).perform()


'''页面切换'''
#切换窗口
#driver.switch_to_window("windowName")

#for handle in driver.window_handles:
#    driver.switch_to_window(handle)

#切换frame
#driver.switch_to_frame("frameName.0.child")



'''弹窗处理'''
#alert = driver.switch_to_alert()


'''历史记录'''
#driver.forward()
#driver.back()

'''Cookies处理'''
#为页面添加Cookies
#driver.get("http://www.example.com")
#cookie = {'name':'foo',"value":'bar'}
#driver.add_cookie(cookie)
#获取页面Cookies
#driver.get("http://www.example.com")
#driver.get_cookie()
































