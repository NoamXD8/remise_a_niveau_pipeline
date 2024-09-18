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

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM etudiants;")
    etudiants = cursor.fetchall()
    # print(colorama.Fore.RED + "Données des étudiants :" + colorama.Style.RESET_ALL)
    # for etudiant in etudiants:
    #     print(etudiant)
    etudiants_dict = {
        e[0]: {
            'prenom': e[1],
            'nom': e[2],
            'numero_salle': e[3],
            'telephone': e[4],
            'email': e[5],
            'annee_obtention': e[6],
            'numero_classe': e[7]
            }
            for e in etudiants
        }
        
    cursor.execute("SELECT * FROM enseignants;")
    enseignants = cursor.fetchall()
    #print(colorama.Fore.RED + "Données des enseignants :" + colorama.Style.RESET_ALL)
    # for enseignant in enseignants:
    #     print(enseignant)

#ETAPE 3 : Manipulation des données

    enseignants_dict = {
            e[0]: {
                'prenom': e[1],
                'nom': e[2],
                'numero_salle': e[3],
                'departement': e[4],
                'annee_obtention': e[5],
                'email': e[6],
                'telephone': e[7],
                'numero_classe': e[8]
            }
            for e in enseignants
        }
    enseignants_par_classe = {}
    for enseignant in enseignants:
        teacher_id, t_prenom, t_nom, t_numero_salle, t_departement, t_annee_obtention, t_email, t_telephone, t_numero_classe = enseignant
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
        student_id, prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe = etudiant
        enseignant = enseignants_par_classe.get(numero_classe, None)
        
        if enseignant:
            association = {
                'etudiant': f"{prenom} {nom}",
                'enseignant': f"{enseignant['prenom']} {enseignant['nom']}",
                'classe': numero_classe,
            }
            associations.append(association)

    # Affichage des associations
    print("Associations Élèves - Enseignants:")
    for association in associations:
        print(f"Élève: {association['etudiant']}, Prof Pincipal: {association['enseignant']}, "
            f"Classe: {association['classe']}")
    


except Exception as error:
    print(f"Erreur lors de la connexion à la base de données : {error}")



    
    


if conn:

    cursor.close()
    conn.close()
    #print("La connexion à la base de données a été fermée.")
