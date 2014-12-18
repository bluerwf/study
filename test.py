#! /usr/bin/env python
# coding=utf-8

import sys
from file_class import File

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
#@deco.cache
def gettoken(nm):
    return md5(nm).hexdigest()



if '__main__' == __name__:
    #main()
    import time
    t1 = time.time()
    gettoken('jane')
    gettoken('jack')
    gettoken('jane')
    gettoken('jack')
    gettoken('jack')
    gettoken('jane')
    gettoken('jack')
    gettoken('jack')
    gettoken('jane')
    gettoken('jack')
    gettoken('ann')
    gettoken('jack')
    gettoken('jack')
    t2 = time.time()
    print "total: ", t2 - t1

