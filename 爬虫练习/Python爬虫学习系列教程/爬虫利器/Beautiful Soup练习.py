#coding:utf-8
from bs4 import BeautifulSoup
import lxml

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,"lxml")
#print soup.prettify()  #打印整个html的内容


'''打印各种标签'''
#print soup.title
#print soup.head
#print soup.a
#print soup.p


'''Tag:HTML里面的一个个标签'''
#print soup.name
#print soup.head.name
#print soup.p.attrs  #打印出所有属性
#soup.p['class']= "newClass"    #修改字典内容
#print soup.p['class']
#print soup.p.get('class')


'''NavigableString'''
#print soup.p.string  #得到标签里面的内容

'''BeautifulSoup'''
#print type(soup.name)
#print soup.name
#print soup.attrs


'''Comment'''
#print soup.a
#print soup.a.string
#print type(soup.a.string)


'''遍历文档树'''
'''直接子节点'''
'''.contents'''
#print soup.head.contents   #一个列表，只有一个元素
#print soup.head.contents[0]
#print type(soup.head.contents)


'''.children'''
#print soup.head.children #是一个list生成器对象
#for child in soup.body.children:
#    print child

'''所有子孙节点'''
'''.descendants'''
#for child in soup.descendants:
#    print child

'''节点内容'''
#print soup.head.string
#print soup.title.string

'''多个内容'''
#for string in soup.strings:  #获取所有内容
#    print (repr(string))

#for string in soup.stripped_strings:  #获取所有内容并去掉空格或空行
#    print (repr(string))

'''父节点  .parent属性'''
#p = soup.p
#print p.parent.name
#content = soup.head.title.string
#print content.parent.name
'''全部父节点'''
#content = soup.head.title.string
#for parent in content.parents:
#    print parent.name

'''兄弟节点 .next_sibling .previous_sibling'''


'''搜索文档树'''
'''find_all(name,sttrs,recursive,text,**kwatgs)
搜索当前Tag的所有子节点，并判断是否符合过滤器的条件'''
'''1)name  可以查找所有名字为name的tag，字符串对象会被自动忽略掉'''
#A传字符串 在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签
#print soup.find_all('a')
#B传正则表达式 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到
#import re
#for tag in soup.find_all(re.compile("^b")):
#    print (tag.name)
#C传列表  如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签
#print soup.find_all(["a","b"])
#D传True  True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
#for tag in soup.find_all(True):
#    print(tag.name)
#E传方法  如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
#def has_class_but_no_id(tag):
#    return tag.has_attr('class') and not tag.has_attr('id')
#print soup.find_all(has_class_but_no_id)

'''2)keyword参数  如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性'''
import re
#print soup.find_all(id='link2')
#print soup.find_all(href=re.compile("elsie"))
#print soup.find_all("a",class_="sister")

'''3）text参数 通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True'''
#print soup.find_all(text="Elsie")
#print soup.find_all(text=["Tillie","Elsie","Lacie"])
#print soup.find_all(text=re.compile("Dormouse"))

'''4)limit参数  find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.'''
#print soup.find_all("a", limit=2)

'''5)recursive参数 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False'''


'''find(name,attrs,recursive,text,**kwargs) 与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果'''

'''find_parents()  find_parent()  find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容'''

'''CSS选择器  我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list'''
'''1）通过标签名查找'''
#print soup.select('title')
#print soup.select('a')
#print soup.select('b')

'''2)通过类名查找'''
#print soup.select('.sister')

'''3)通过id名查找'''
#print soup.select('#link1')

'''4)组合查找  组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开'''
#print soup.select('p #link1')
'''直接子标签查找'''
#print soup.select("head > title")

'''5)属性查找  查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到'''
#print soup.select('a[class="sister"]')
#print soup.select('a[href="http://example.com/elsie"]')
#遍历输出，使用get_text() 获取内容
print type(soup.select('title'))
print soup.select('title')[0].get_text()
for title in soup.select('title'):
    print title.get_text()




















