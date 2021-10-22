from random import *

L= [randint(1,100) for i in range(20)]
print(L)
def sum_list(list) :
    somme=0
    for i in range(len(list)) :
        somme += list[i]
    return(somme)
