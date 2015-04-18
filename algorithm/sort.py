#! /usr/bin/env python
# coding=utf-8


count = 0

def bubble(a):
    l=len(a)
    while l:
        for i in range(l-1):
            if a[i] > a[i+1]:
                a[i],a[i+1]= a[i+1], a[i]
        l -= 1

def insert(a):
    global count
    l = len(a)
    for j in range(1,l):
        for i in range(j,0,-1):
            count += 1
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]

def sort(a):
    b = [x for x in a if x%2 == 0]
    c = [x for x in a if x%2 ==1]
    bubble(b)
    bubble(c)
    return b+c

def sort_odd_even(a):
    def _reorg(a):
        i = -1
        j = 0
        while j < len(a):
            if a[j] % 2 == 0:
                x = a[j]
                k = j
                while k > i+1:
                    a[k] = a[k-1]
                    k -= 1
                a[i+1] = x
                i += 1
            j += 1

    bubble(a)
    _reorg(a)

def qsort(a, l, h):
    def _partition(a, l, h):
        global count
        count += 1
        p = a[l]
        i = l
        j = h
        print "l: %d, h: %d" % (l, h)
        while i < j:
            while i<j and a[j] > p:
                j -= 1
            a[j], p = p, a[j]
            while i < j and a[i] <= p:
                i += 1
            a[i] ,p = p, a[i]
        return i

    if l < h:
        idx = _partition(a, l, h)
        qsort(a, l, idx - 1)
        qsort(a, idx + 1, h)


if __name__ == '__main__':
    a = [6,5,4,3,2,1]
    b = [1, 8, 6, 10, 5, 6, 3, 4]
    c = [1, 8, 5, 6, 3, 4]
    print a
    # insert(a)
    #a = sort(a)
    sort_odd_even(a)
    sort_odd_even(b)
    #insert(b)
    #qsort(a, 0, len(a) -1)
    print a
    print b
    #print count
