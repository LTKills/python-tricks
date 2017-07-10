from utils import swap

def shell(l):
    N = len(l)
    h = 1

    while(h < N/3):
        h = 3*h + 1

    while(h >= 1):
        for i in range(h, N):
            j = i
            while(j >= h and l[j] < l[j-h]):
                swap(l, j, j-h)
                j -= h
        h = int(h/3)

    return l
