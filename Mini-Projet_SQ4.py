personnel = {'prenom': ['Julien', 'Stefano', 'Claire', 'Damien', 'Yuki', 'Sarah', 'Alex', 'Fayna', 'Anaïs', 'John' ] , 'age': ['56','46','36','38','26','24','29','35','30','21'] , 'departement': ['Direction', 'Design', 'Marketing', 'Web', 'Design', 'Design', 'Marketing', 'Marketing', 'Web', 'Web'] }

def noms() :
    l_prenoms = personnel['prenom']
    return(l_prenoms)

def equipe(table, departement) :
    l_dep = []
    for i in range(len(table['prenom'])) :
        if table['departement'][i] == departement :
            l_dep.append(table['prenom'][i])
    return("Equipe " + departement + " : "+ str(l_dep))

def age(table, age_min) :
    l_ages = []
    for i in range(len(table['age'])) :
        if int(table['age'][i]) >= age_min :
            l_ages.append((table['prenom'][i], str(table['age'][i]) + ' ans'))
    return(l_ages)