import random
from utils import swap


def partition(l, lo, hi):
    i = lo+1
    j = hi
    v = l[lo]

    while(True):
        while(l[i] < v):
            if(i == hi):
                break
            i += 1

        while(v < l[j]):
            if(j == lo):
                break
            j -= 1

        if(i >= j):
            break
        swap(l, i, j)

    swap(l, lo, j)
    return j


def sort(l, lo, hi):
    if(hi <= lo):
        return

    j = partition(l, lo, hi)
    sort(l, lo, j-1)
    sort(l, j+1, hi)


def quick(l):
    random.shuffle(l)
    sort(l, 0, len(l)-1)
    return l

