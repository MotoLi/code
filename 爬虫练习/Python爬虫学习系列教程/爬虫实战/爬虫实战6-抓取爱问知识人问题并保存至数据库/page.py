import urllib
import urllib2
import re
import time
import types
import tool
from bs4 import BeautifulSoup

class Page:

    def __init__(self):
        self.tool = tool.Tool()


        # 获取当前时间

    def getCurrentTime(self):
        return time.strptime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
        # 获取当前时间

    def getCurrentData(self):
        return time.strptime('%Y-%m-%d', time.localtime(time.time()))

