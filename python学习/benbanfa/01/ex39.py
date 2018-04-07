#coding: utf-8
#创建一个地图
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'cClifornia': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#创建一些城市
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

print '-'*10
print "Michigan's sdfasfljdsfklj is :", states['Michigan']
print "Florida's asdfjaslkdfjasl is :", states['Florida']

print '-'*10
print "Michigan has :", cities[states['Michigan']]
print "Florida has: ",cities[states['Florida']]

print '-'*10
for state, abbrev in states.items():                 #健值对的for循环
	print "%s is abbreviated %s" % (abbrev, state)

print '-'*10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)


print '-'*10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])


print '-'*10
state = states.get('Texas',None)

if not state:
	print "Sorry, no Texas."
	

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city