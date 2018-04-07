print "1."
def f(a,b,c):
    return a+b+c

print(f(3,1,5))
print(f(3,2,1))

print "2."
def func(*name):
    print type(name)
    print name

func(1,4,6)
func(5,6,7,1,2,3)


print "3."
def func(**dict):
    print type(dict)
    print dict

func(a=1,b=9)
func(m=2,n=1,c=11)

print "4."
def func(a,b,c):
    print a,b,c

args = (1,3,4)
func(*args)


print "5."
for a in [3,4.4,'life']:
    print a
    
    
print "6."
idx = range(5)
print idx

for a in range(10):
    print a**2