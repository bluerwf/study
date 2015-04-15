#! /usr/bin/env python
# coding=utf-8

from sort import bubble
import time

a = [i for i in xrange(10000)]

bubble(a)

def timing(f, *args, **kwargs):
    def deco(*args, **kwargs):
        b = time.time()
        r = f(*args, **kwargs)
        e = time.time()
        print "{} seconds".format(e - b)
        return r
    return deco

@timing
def bi_search(a, key, low, high):
    if low < high and low >= 0:
        mid = (high - low + 1)/2
        print "low = %d, high = %d, mid = %d" % (low, high, mid)
        d = key - a[mid]
        if d == 0:
            return True
        elif d < 0:
            return bi_search(a, key, low, mid)
        else:
            return bi_search(a, key, mid, high)
        return False

print bi_search(a, 50001, 0, len(a) - 1)
