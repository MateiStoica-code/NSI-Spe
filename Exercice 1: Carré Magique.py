carre4=[[4,5,11,14],[15,10,8,1],[6,3,13,12],[9,16,2,7]]

def somme_ligne(carre,n):
    somme=0
    for i in carre[n]:
        somme+=i
    return somme

def verification_somme(carre):
    a=[]
    for b in range(len(carre)):
        a.append(somme_ligne(carre,b))

    for y in range(len(carre)-1):
        if a[y]==a[y+1]:
            None
        else:
            return False
    return True

def somme_col(carre,col):
    a=[]
    for i in range(len(carre)):
        a.append(carre[i][col])
    b=sum(a)
    return b
