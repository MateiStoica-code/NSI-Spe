def suite(n):
    assert n>=1, "Nombre doit être supérieur ou égal à 1"
    sequence = [] #On crée la liste qui va être renvoyée
    sequence.append(n) #On rajoute le nombre initial à la liste
    while n != 1: #On établit la condition d'arrêt et une boucle
        if n%2 == 0 : #On teste la parité du nombre passé en argument
            n = n//2    # si n est pair, on le divise par 2
        else :
            n = 3*n + 1 # si n est impair, on fait 3n + 1
        sequence.append(n)
    return(sequence)