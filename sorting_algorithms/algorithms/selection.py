from utils import swap


def selection(l):
    for i in range(len(l)):
        mini = i
        for j in range(i+1, len(l)):
            if(l[j] < l[mini]):
                mini = j
        swap(l, mini, i)
    return l
