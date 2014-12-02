#! /usr/bin/env python
# coding=utf-8
import sys
from os import path as pll 

print sys.argv


def main():
    print 'ok?'
    if sys.argv[1] == '-ls':
        path = sys.argv[2]
        getfilelist(path)
    elif sys.argv[1]  == 'lt':
        getname()
    else:
        print 'nothing'

def getfilelist(path):
    if pll.exists(path):
        pass
    else:
        print "invaild path"


    print getfilelist.__name__
    
def getname():
    print getname.__name__

if '__main__' == __name__:
    main()

