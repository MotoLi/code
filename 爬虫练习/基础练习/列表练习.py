'''list = [0,1,2,3,4,5,6]
print list[2:-1]'''

a=10
b=0
try:
    c=a/b
    print c
except ZeroDivisionError,e:
    print e.message

    print e
print "done"