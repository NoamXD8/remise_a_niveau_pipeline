import colorama
import psycopg2

#Étape 2 : Extraction des données avec Python

try:
    conn = psycopg2.connect(
        dbname="Ecole",  
        user="noam",    
        password="root",  
        host="localhost",   
        port="5432"         
    )
    print("Connexion à la base de données réussie.")
    print()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM etudiants;")
    etudiants = cursor.fetchall()

    def get_etudiants():
        print(colorama.Fore.RED + "Données des étudiants :" + colorama.Style.RESET_ALL)
        for etudiant in etudiants:
            print(etudiant)

        etudiants_dict = {
            etudiant[0]: {
                'prenom': etudiant[1],
                'nom': etudiant[2],
                'numero_salle': etudiant[3],
                'telephone': etudiant[4],
                'email': etudiant[5],
                'annee_obtention': etudiant[6],
                'numero_classe': etudiant[7]
                }
                for etudiant in etudiants
            }
        print()
        print(etudiants_dict)

    cursor.execute("SELECT * FROM enseignants;")
    enseignants = cursor.fetchall()

    def get_enseignants():
        print(colorama.Fore.RED + "Données des enseignants :" + colorama.Style.RESET_ALL)
        for enseignant in enseignants:
            print(enseignant)

        enseignants_dict = {
                        enseignant[0]: { 
                            'id': enseignant[0],
                            'prenom': enseignant[1],
                            'nom': enseignant[2],
                            'numero_salle': enseignant[3],
                            'departement': enseignant[4],
                            'annee_obtention': enseignant[5],
                            'email': enseignant[6],
                            'telephone': enseignant[7],
                            'numero_classe': enseignant[8]
                        }
                        for enseignant in enseignants
                    }
        print()
        print(enseignants_dict)

    print(colorama.Fore.RED+"Etape 2 : Extraction des données avec Python"+colorama.Style.RESET_ALL)
    etudiant = get_etudiants()
    enseignant = get_enseignants()
#ETAPE 3 : Manipulation des données
    print()
    print(colorama.Fore.RED+"Etape 3 : Manipulation des données"+colorama.Style.RESET_ALL)
    print()
    enseignants_par_classe = {}
    for enseignant in enseignants:
        teacher_id = enseignant[0]
        t_prenom = enseignant[1]
        t_nom = enseignant[2]
        t_numero_salle = enseignant[3]
        t_departement = enseignant[4]
        t_annee_obtention = enseignant[5]
        t_email = enseignant[6]
        t_telephone = enseignant[7]
        t_numero_classe = enseignant[8]

        enseignants_par_classe[t_numero_classe] = {
            'id': teacher_id,
            'prenom': t_prenom,
            'nom': t_nom,
            'numero_salle': t_numero_salle,
            'departement': t_departement,
            'annee_obtention': t_annee_obtention,
            'email': t_email,
            'telephone': t_telephone
        }

    associations = []
    
    for etudiant in etudiants:
        student_id = etudiant[0]
        prenom = etudiant[1]
        nom = etudiant[2]
        numero_classe = etudiant[7]   
             
        enseignant = enseignants_par_classe.get(numero_classe, None)
        
        if enseignant:
            association = {
                'etudiant': f"{prenom} {nom}",
                'enseignant': f"{enseignant['prenom']} {enseignant['nom']}",
                'classe': numero_classe,
            }
            associations.append(association)

    for association in associations:
        print(f"Élève: {association['etudiant']}, Prof Pincipal: {association['enseignant']}, "
            f"Classe: {association['classe']}")
        
    

#Étape 4 : Analyse des données
    print()
    print(colorama.Fore.RED+"Etape 4 : Analyse des données"+colorama.Style.RESET_ALL)
    compteur ={}
    for enseignant in enseignants:
        teacher_id = enseignant[0]
        t_prenom = enseignant[1]
        t_nom = enseignant[2]
        t_numero_classe = enseignant[8]

        compteur[teacher_id] = {
            'enseignant': f"{t_prenom} {t_nom}",
            'nb_eleves': 0
        }

    for etudiant in etudiants:
        student_id = etudiant[0]
        prenom = etudiant[1]
        nom = etudiant[2]
        numero_classe = etudiant[7]
        
        enseignant = enseignants_par_classe.get(numero_classe, None)
        
        if enseignant:
            compteur[enseignant['id']]['nb_eleves'] += 1

    print()        
    print("Nombre d'élève par enseignant : ")
    for teacher_id, i in compteur.items():
        numero_classe = 0
        for classe, enseignant in enseignants_par_classe.items():
            if enseignant['id'] == teacher_id:
                numero_classe = classe
        print(f"Classe : {numero_classe} - Enseignant: {i['enseignant']} - Nombre d'élèves: {i['nb_eleves']}")

except Exception as error:
    print(f"Erreur lors de la connexion à la base de données : {error}")




if conn:
    cursor.close()
    conn.close()
