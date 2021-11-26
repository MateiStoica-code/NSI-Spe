from math import *
from random import *

def shuffle_l(list) :
    indexes = [i for i in range(len(list))]
    while len(indexes) != 0 :
        index_1 = indexes.pop(randint(0,len(indexes)-1))
        index_2 = indexes.pop(randint(0,len(indexes)-1))
        val = list[index_1]
        list[index_1] = list[index_2]
        list[index_2] = val
    return list

L = [i**2 for i in range(10)]

print("Original list (first ten integers, squared) = " + str(L))
print("Test of shuffle function on original list = " + str(shuffle_l(L)))
