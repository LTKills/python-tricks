from utils import swap

aux = []

def merge_aux(l, lo, mid, hi):
    global aux
    i = int(lo)
    j = int(mid+1)

    for k in range(lo, hi+1):
        aux[k] = l[k]

    for k in range(lo, hi+1):
        if(i > mid):
            l[k] = aux[j]
            j += 1

        elif(j > hi):
            l[k] = aux[i]
            i += 1

        elif(aux[j] < aux[i]):
            l[k] = aux[j]
            j += 1

        else:
            l[k] = aux[i]
            i += 1


def sort(l, lo, hi):
    if(hi <= lo):
        return

    mid = int(lo) + int((hi - lo)/2)
    sort(l, lo, mid)
    sort(l, mid+1, hi)
    merge_aux(l, lo, mid, hi)


def merge(l):
    global aux
    aux = list(l)
    sort(l, 0, len(l)-1)
    return l



