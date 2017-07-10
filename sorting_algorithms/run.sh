#/bin/bash


SHELL=shell
QUICK=quick
MERGE=merge
INSERTION=insertion
SELECTION=selection
BUBBLE=bubble

ALGORITHMS=( $SHELL $QUICK $MERGE $INSERTION $SELECTION $BUBBLE )

if [ $# -ne 3 ]; then
    echo "Wrong usage"
    echo "usage: ./run [elements on max vector] [progression step] [algorithm]"
    exit 0
fi


if [ "$3" == "all" ]; then
#    parallel python3 main.py ::: $1 ::: $2 ::: ${ALGORITHMS[$i]}
    for i in {0..5}; do
        python3 main.py $1 $2 ${ALGORITHMS[$i]} > "./tests/${ALGORITHMS[$i]}.dat" &
    done
else
    python main.py $1 $2 $3 > "./tests/$3.dat"
fi
