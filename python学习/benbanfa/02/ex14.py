# coding=utf-8
from sys import argv

script, user_name = argv
prompt = '请输入YES或NO>'

print "你好 %s,我是程序%s" % (user_name, script)
print "我想要问你一些小问题哦"
print "你喜欢我吗，%s?" % user_name

def likeorno():
    likes = raw_input(prompt)

    if likes == "YES" :
        print "谢谢,我也喜欢你"
    elif likes == "NO":
        print "好吧，后会有期 "
    else:
        likeorno()

likeorno()
