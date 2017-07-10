import sys
import time
import utils
import algorithms

if(len(sys.argv) != 4):
    print("Wrong usage")
    print("usage: ./run [elements on max vector] [progression step] [algorithm]")

n = int(sys.argv[1])

step = int(sys.argv[2])

for i in range(0, n+1, step):
    start = time.time()

    if(sys.argv[3] == "insertion"):
        l = algorithms.insertion(utils.genRandVec(i))

    elif(sys.argv[3] == "bubble"):
        l = algorithms.bubble(utils.genRandVec(i))

    elif(sys.argv[3] == "selection"):
        l = algorithms.selection(utils.genRandVec(i))

    elif(sys.argv[3] == "shell"):
        l = algorithms.shell(utils.genRandVec(i))

    elif(sys.argv[3] == "merge"):
        l = algorithms.merge(utils.genRandVec(i))

    elif(sys.argv[3] == "quick"):
        l = algorithms.quick(utils.genRandVec(i))

    else:
        print("not a valid algorithm")
        sys.exit()

#    print(l)

    end = time.time()
    print(str(i) + " " + str(end-start))

