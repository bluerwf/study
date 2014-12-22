#! /usr/bin/env python
# coding=utf-8

import sys
import time
from file_class import File
import common 
def main():
    path = sys.argv[2]
    fh = File(path, '.py')
    if sys.argv[1] == 'ls':
        fl = fh.filelist
        print fl
        for f in fl:
            with open(f) as fh:
                content = fh.readlines()
                for line in content:
                    print line,
    elif sys.argv[1]  == 'ld':
        dirlist = fh.getfilelist(path)
        print dirlist
    else:
        print 'nothing'


from hashlib import md5
import deco
@deco.timeit
@deco.cache
def gettoken(nm):
    if isinstance(nm, str) and nm is not "":
        return md5(nm).hexdigest()
    else:
        raise common.TokenError(nm)

@deco.cache2
def get_token(nm, to=10):
    if isinstance(nm, str) and len(nm) > 0:
        return md5(nm + str(time.time())).hexdigest()
    else:
        return common.TokenError(nm)

if '__main__' == __name__:
    #main()
    t1 = time.time()
    try:
        gettoken('jane')
        gettoken('jack')

        gettoken('jack')
        gettoken('wang')
        gettoken('li')
        gettoken('jack')
        gettoken('zhang')
        gettoken('jane')
        gettoken('jack')
        gettoken('ann')
        gettoken('jack')
        #gettoken('')
#        _, dic = gettoken('111')
        t2 = time.time()
        print "total: ", t2 - t1
#        common.save_dic('/Users/lafengnan/codes/Github/study/1',dic)
    except  common.TokenError as e:
        print e

#print common.fun(0)
#print common.fun(1)
#print common.fun(2)
#print common.fun(200)
print "abcd", get_token("abcd", 3)
print "abce", get_token("abce", 3)
print "abcd", get_token("abcd", 3)
time.sleep(4)
print "abcd", get_token('abcd', 3)
