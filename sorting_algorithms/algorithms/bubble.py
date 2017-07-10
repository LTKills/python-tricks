from utils import swap

def bubble(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if(l[j] > l[j+1]): swap(l, j, j+1)

    return l

