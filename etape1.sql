CREATE TABLE etudiants (
    student_id SERIAL PRIMARY KEY,              
    prenom VARCHAR(50) NOT NULL,                
    nom VARCHAR(50) NOT NULL,                   
    numero_salle INT,                           
    telephone VARCHAR(15) NOT NULL UNIQUE,      
    email VARCHAR(100) NOT NULL UNIQUE,         
    annee_obtention INT,                        
    numero_classe INT                          
);

CREATE TABLE enseignants (
    teacher_id SERIAL PRIMARY KEY,              
    prenom VARCHAR(50) NOT NULL,                
    nom VARCHAR(50) NOT NULL,                   
    numero_salle INT,                           
    departement VARCHAR(100),                   
    annee_obtention INT,                        
    email VARCHAR(100) NOT NULL UNIQUE,         
    telephone VARCHAR(15) NOT NULL UNIQUE,     
    numero_classe INT                         
);

INSERT INTO public.etudiants(student_id, prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
	VALUES (1, 'Mark', 'Watney', NULL, '777-555-1234', 'mark.watney@noemail.com', 2035, 5)
;

INSERT INTO public.enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES (1, 'Jonas', 'Salk', NULL, 'Biologie', NULL, 'jsalk@school.org', '777-555-4321', 5)
;




