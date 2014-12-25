import os
import sys

from os import path as pll

class File(object):
    """docstring for ClassName"""
    def __init__(self, path, suffix):
        super(File, self).__init__()
        self.path = path
        self.suffix = suffix

    #@property
    def filelist(self):
        #path = path if path else self.path
        path = self.path
        suffix = self.suffix
        if pll.exists(path):
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

    def getdirlist(self, path):
        path = path if path else self.path
        if pll.exists(path):
            w = os.walk(path)
            dirlist = list()
            while True:
                try:
                    ufo = w.next()
                    dirs = ufo[1] 
                    for i in dirs:
                        dirlist.append(os.path.join(ufo[0],i))
                except StopIteration as e:
                    break
            return dirlist 
        else:
            print "invaild path"


def main():
    print sys.argv
    thefile = File(sys.argv[2], 'py')
    if sys.argv[1] == 'ls':
        #path = sys.argv[2]
        #fl = thefile.getfilelist(path, '.py')
        fl = thefile.filelist()
        print fl
        for f in fl:
            with open(f) as fh:
                content = fh.readlines()
                for line in content:
                    print line,
    elif sys.argv[1]  == 'ld':
        dirlist = thefile.getfilelist(sys.argv[2])
        print dirlist
    else:
        print 'nothing'

if __name__=='__main__':
	main()
