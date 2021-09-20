nb_dec = int(input("Veuillez saisir un entier positif en base 10 : "))
base = int(input("Veuillez saisir la base dans laquelle vous voulez représenter ce nombre : "))
r = nb_dec%base
list_rest = []
while r>0 :
    r = r%base
    print(r)
    list_rest.append(r)
    print (list_rest)
