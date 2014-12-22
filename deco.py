from time import time

def cache(f):
    dic={}
    def wrpper(k, *arg, **karg):
        if k not in dic:
            token =f(k, *arg, **karg)
            dic[k] = token
        else:
            token = dic.get(k)
        print 'ok'
        return token, dic    
        
    return wrpper

def cache2(f):
    """
    cache structure:
    {
       'name1' : ('token', ts),
       'name2' : ('token2', ts2),
       ...
    }
    """
    dic = {}
    def wrapper2 (k, timeout=10):
        now  = time()
        if k in dic:
            if now - dic[k][1] > timeout:
                t = f(k, timeout)
                dic[k] = (t, now)
                return t
            else:
                return dic[k][0]
        else:
            t = f(k, timeout)
            dic[k] = (t, now)
            return t
    return wrapper2


def timeit(f):
    def wrapper(*arg):
        begin  = time()
        s= f(*arg)
        end = time()
        print end-begin
        return s 
    return wrapper    

