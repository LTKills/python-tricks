from utils import swap


def insertion(l):
    for i in range(1, len(l)):
        j = i
        while(j > 0 and l[j] < l[j-1]):
            swap(l, j, j-1)
            j -= 1
    return l
