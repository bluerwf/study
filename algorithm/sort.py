#! /usr/bin/env python
# coding=utf-8

def bubble(a):
    l=len(a)
    while l:
        for i in range(l-1):
            if a[i] > a[i+1]:
                a[i],a[i+1]= a[i+1], a[i]
        l -= 1

def insert(a):
    l = len(a)
    for j in range(1,l):
        for i in range(j,0,-1):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]

if __name__ == '__main__':
    a = [6,5,4,3,2,1]
    print a
    insert(a)
    print a
