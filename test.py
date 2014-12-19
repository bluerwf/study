#! /usr/bin/env python
# coding=utf-8

import sys
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
        #raise excep.Msg('error,should be string')
        raise common.TokenError(nm)



if '__main__' == __name__:
    #main()
    import time
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
        _, dic = gettoken('111')
        t2 = time.time()
        print "total: ", t2 - t1
        common.save_dir('/Users/lafengnan/codes/Github/study/1',dic)
    except  common.TokenError as e:
        print e


