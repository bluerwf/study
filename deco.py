


def cache(f):
    dic={}
    def wrpper(name):
        if name not in dic:
            token =f(name)
            dic[name] = token
        else:
            token = dic.get(name)
        print 'ok'
        return token   
        
    return wrpper


from time import time

def timeit(f):
    def wrapper(*arg):
        begin  = time()
        s= f(*arg)
        end = time()
        print end-begin
        return s 
    return wrapper    

