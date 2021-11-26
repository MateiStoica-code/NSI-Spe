from math import *
from random import *


def ran_list(n) :
    l = []
    for i in range(n) :
        l.append(randint(0,100))
    return l

def min(list) :
    min=0
    for i in range(len(list)) :
        if list[i] < list[min] :
            min = i
    return(min)

def sort_l(list) :
    print(list)
    list1 = []
    for i in range(len(list)) :
        minim = min(list)
        popped = list.pop(minim)
        list1.append(popped)
    return(list1)
