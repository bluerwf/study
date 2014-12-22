
class TokenError(Exception):
    def __init__(self, nm):
        self.nm = nm
    def __str__(self):
        return "Error: nm: {0} is illegale".format(self.nm)

def save_dic(path,dic):
   with open(path,'w') as fh:
       for k in dic:
           fh.write(k+':'+dic[k]+'\n')
from deco import cache

@cache

def fun(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n >= 2 :
        return fun(n-1)+fun(n-2)

