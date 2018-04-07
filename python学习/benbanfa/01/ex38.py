#coding: utf-8
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')       #详见split方法，遇到空格就分割
print stuff


more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()    #移除列表中最后一位，且返回该值
	print "Adding: ", next_one
	stuff.append(next_one)         #添加到列表末尾
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff[3:5]              #拿到列表四和五的元素
print stuff.pop()
print stuff.count('Apples')
print ' '.join(stuff) #what? cool!     以前面的str将列表里面的元素相连并输出字符串
print ' '.join(stuff[3:5]) # super stellar!