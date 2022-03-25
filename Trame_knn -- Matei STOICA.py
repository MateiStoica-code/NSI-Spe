import csv
from math import sqrt

with open('bd_iris.csv', newline='') as iris:
    bd_iris = list(csv.reader(iris, delimiter=','))

# calcul de la distance entre l'élément de coordonnées (x,y) et l'élément de coordonnées (z,t)
# x et z représentent les largeurs des sépales
# y et t les largeurs des pétales
def distance_euclidienne(x,y,z,t):
    return round(sqrt(((x-z)**2)+((y-t)**2)), 3)


# fonction qui retourne la catégorie de l'iris donnée par ses coordonnées (x,y)
# à partir de l'algorithme des k plus proches voisins
def kNN(liste,x_individu,y_individu,k):
    distances_variétés = []
    for i in range(len(liste)):
        distances_variétés.append((distance_euclidienne(x_individu, y_individu, liste[i][0], liste[i][1]), liste[i][2]))
        #On crée une liste à laquelle on ajoute, pour chaque élément de la liste des k voisins (liste_knn, voir plus bas),
        #Un tuple avec la distance entre l'élément de la liste_knn ainsi que la variété de celui-ci et l'élément choisi
    distances_variétés.sort(key = lambda x: x[0])
    distances_variétés = distances_variétés[0:k]
    #On sorte la liste de tuples en fonction de la distance, puis on la slice pour ne garder que les k éléments les plus proches de l'élément choisi

    occurences = {}
    for elt in distances_variétés:
        if elt[1] in occurences :
            occurences[elt[1]] += 1
        elif elt[1] not in occurences:
            occurences[elt[1]] = 1
    return max(occurences)
    #Simple algorithme pour compter le nombre d'occurences de chaque variété qui apparait dans la liste d'au-dessus et renvoyer la variété qui apparait le plus souvent
           


# liste_knn est la liste formée d'éléménts [x,y,'variété'] à partir de bd_iris
# elle est simplement initialisée, vous devez la remplir vous-même.
liste_knn = []
for elt in bd_iris:    
    liste_knn.append([float(elt[2]), float(elt[4]), str(elt[5])]) #Pour chaque entrée dans la base de données, entrée qui est 
                                                                  #sous la forme [Index, longueur sépale, largeur sépale, longueur pétale, largeur pétale, variété],
                                                                  #on ne sélectionne que les informations dont on a besoin, soit les éléments aux indexes 2, 4 et 5


#Ma propre fonction de test:
liste_test = [[3.5, 0.2],[3.0, 1.4],[3.0 , 1.8]]
for largeur_sepales, largeur_petales in liste_test:
    print("Cette iris a des sépales larges de " + str(largeur_sepales) + "cm " + "et des pétales larges de " + str(largeur_petales) + "cm. En utilisant la méthode des k plus proches voisins (k-NN), on obtient que l'iris est de la variété " + kNN(liste_knn, largeur_sepales, largeur_petales, 12))
    print()









# Tests de la fonction kNN pour retrouver les catégories de la question 7 de l'activité 3 de la séquence 10
#def main():
    #test = True
    #while test:
   #     print("Test de votre fleur")
  #      largeur_sepales = float(input("Entrer la largeur des sépales : "))
 #       largeur_petales = float(input("Entrer la largeur des pétales : "))
#        print("La variété de votre fleur semble être",kNN(liste_knn,largeur_sepales,largeur_petales,12))
#        reponse = input("Voulez-vous tester une autre fleur ? (O:N)")
#        if reponse.upper() == "N":
#            test = False
    # Execution de la procédure main qui permet de tester autant de fleurs que l'on veut
#main()

