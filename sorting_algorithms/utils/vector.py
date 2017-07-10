import random

def genRandVec(n):
    l = [int(random.random()*n*n) for i in range(n)]
    return l
