def recherche_dichotomique(tableau, valeur) :
    assert (valeur in tableau) and (len(tableau) != 0) ,"Votre tableau soit ne contient pas la valeur, soit est vide"
    début = 0
    fin = len(tableau)
    trouvé = False
    conteur = 0
    while not trouvé and début < fin :
        x = (début+fin)//2
        if tableau[x] == valeur :
            trouvé = True
        else :
            if tableau[x] > valeur:
                fin = x
            else :
                début = x
        conteur += 1
    return x, conteur

def generate_sorted_list(n):
    return [i for i in range(n+1)]

list1=[50,100,500,1000,5000,10000,50000]

for elt in list1:
    print(recherche_dichotomique(generate_sorted_list(elt),49))
    print()
