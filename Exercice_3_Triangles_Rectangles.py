from math import *
from random import *
def dist_pts(pA,pB) :
    dist = sqrt(((pB[0] - pA[0])**2)+((pB[1] - pA[1])**2))
    return(dist)

def compare(a, b) :
    if a<b :
        return(b)
    else :
        return(a)

def est_rectangle(p1,p2,p3):
    len_1_2 = dist_pts(p1, p2)
    len_2_3 = dist_pts(p2, p3)
    len_3_1 = dist_pts(p3, p1)
    #longueurs de tous les côtés du triangle

    a =[len_1_2, len_2_3, len_3_1]

    hypo = compare(compare(len_1_2, len_2_3), compare(len_2_3, len_3_1))

    dico = {len_1_2 : 0, len_2_3 : 1, len_3_1 :2}

    a.pop(dico[hypo])
    #on définit l'hypothénuse et les deux côtés adjacents, puis on les sépare


    if sqrt((a[0])**2+(a[1]**2))==hypo :
        return(True)
    else :
        return(False)

def random_points() :
    x=[]
    y=[]
    for i in range(3) :
        y.append(randint(0,10))
        x.append(randint(0,10))
    p1=(x[0],y[0])
    p2=(x[1],y[1])
    p3=(x[2],y[2])
    return(p1, p2, p3)

def test_rectangles(n):
    compte_rectangles = 0
    for i in range(n) :
        points=random_points()
        if est_rectangle(points[0], points[1], points[2]) == True :
            compte_rectangles+=1
    return(str(compte_rectangles/n) +'%')





























