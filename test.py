#! /usr/bin/env python
# coding=utf-8

import sys
from os import path as pll 
import os
print sys.argv

def main():
    print 'ok?'
    if sys.argv[1] == '-ls':
        path = sys.argv[2]
        fl = getfilelist(path, '.py')
        ff = getdir(path)
        print fl
        print ff
        for f in fl:
            with open(f) as fh:
                content = fh.readlines()
                for line in content:
                    print line,
    elif sys.argv[1]  == 'lt':
        getname()
    else:
        print 'nothing'

def getfilelist(path,suffix='*'):
    if pll.exists(path):
        #print os.listdir(path)
        w = os.walk(path)
        flist = list()
        while True:
            try:
                ufo = w.next()
                files = ufo[2] if suffix == '*' else [f for f in ufo[2] if f.endswith(suffix)]
                for i in files:
                     flist.append(os.path.join(ufo[0],i))
            except StopIteration as e:
                break
        return flist
    else:
        print "invaild path"

    #print getfilelist.__name__
def getdir(path):
    if pll.exists(path):
        #print os.listdir(path)
        w = os.walk(path)
        #flistt = list()
        while True:
            try:
                ufo = w.next()
                files = ufo[1] 
                for i in files:
                    p=os.path.join(ufo[0],i)
                    print p
            except StopIteration as e:
                break
        return p
    else:
        print "invaild path"

        
    
def getname():
    print getname.__name__

if '__main__' == __name__:
    main()

