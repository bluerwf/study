from functools import wraps

def decoo(type):
    def deco(func, *arg, **karg):
        @wraps(func)
        def wrap(*arg, **karg):
            print "before excute,%s %s" %(type,func.__name__)
            func()
            print 'after escute %s %s'%(type,func.__name__)
        return wrap
    return deco

@decoo('type1')
def funct(*arg, **karg):
    print 'hello'

funct()    
print funct.__name__
