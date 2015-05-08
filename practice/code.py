
def qsort(p,l,h):
    def part(p,l,h):
        q = p[l]
        i = l
        j = h
        while i < j:
            while i < j and p[j] > q:
                j -= 1
            p[i], p[j] = p[j], p[i]
            while i < j and p[i] <= q:
                i += 1
            p[i], p[j] = p[j], p[i]
        return i
    if l < h:
        index = part(p,l,h)
        qsort(p,l,index-1)
        qsort(p,index+1, h)
a = [3,2,1,4,1,6,9,8]
b = [3,2,1,4,1,6,9,8]

qsort(a,0,7)
qsort(b,0,7)
print a
print b
