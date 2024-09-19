CREATE TABLE etudiants (
    student_id SERIAL PRIMARY KEY,              
    prenom VARCHAR(50) NOT NULL,                
    nom VARCHAR(50) NOT NULL,                   
    numero_salle INT,                           
    telephone VARCHAR(15) NOT NULL UNIQUE,      
    email VARCHAR(100) UNIQUE,         
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
	VALUES (1, 'Mark', 'Watney', NULL, '777-555-1234', NULL, 2035, 5)
;

INSERT INTO public.enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES (1, 'Jonas', 'Salk', NULL, 'Biologie', NULL, 'jsalk@school.org', '777-555-4321', 5)
;




-- Insertion de 20 étudiants
INSERT INTO étudiants (student_id, prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
VALUES
    (2, 'Anna', 'Smith', 102, '777-555-1235', 'anna.smith@ecole.org', 2036, 1),
    (3, 'John', 'Doe', 103, '777-555-1236', 'john.doe@ecole.org', 2037, 2),
    (4, 'Emily', 'Jones', 104, '777-555-1237', 'emily.jones@ecole.org', 2035, 3),
    (5, 'Michael', 'Brown', 105, '777-555-1238', 'michael.brown@ecole.org', 2036, 1),
    (6, 'Sarah', 'Davis', 106, '777-555-1239', 'sarah.davis@ecole.org', 2037, 2),
    (7, 'David', 'Wilson', 107, '777-555-1240', 'david.wilson@ecole.org', 2035, 3),
    (8, 'Laura', 'Taylor', 108, '777-555-1241', 'laura.taylor@ecole.org', 2036, 1),
    (9, 'James', 'Anderson', 109, '777-555-1242', 'james.anderson@ecole.org', 2037, 2),
    (10, 'Sophia', 'Thomas', 110, '777-555-1243', 'sophia.thomas@ecole.org', 2035, 3),
    (11, 'Daniel', 'Moore', 111, '777-555-1244', 'daniel.moore@ecole.org', 2036, 1),
    (12, 'Olivia', 'Jackson', 112, '777-555-1245', 'olivia.jackson@ecole.org', 2037, 2),
    (13, 'Matthew', 'Martin', 113, '777-555-1246', 'matthew.martin@ecole.org', 2035, 3),
    (14, 'Emma', 'Lee', 114, '777-555-1247', 'emma.lee@ecole.org', 2036, 1),
    (15, 'Christopher', 'Walker', 115, '777-555-1248', 'christopher.walker@ecole.org', 2037, 2),
    (16, 'Isabella', 'Harris', 116, '777-555-1249', 'isabella.harris@ecole.org', 2035, 3),
    (17, 'Ethan', 'Young', 117, '777-555-1250', 'ethan.young@ecole.org', 2036, 1),
    (18, 'Mia', 'King', 118, '777-555-1251', 'mia.king@ecole.org', 2037, 2),
    (19, 'Alexander', 'Wright', 119, '777-555-1252', 'alexander.wright@ecole.org', 2035, 3),
    (20, 'Ava', 'Lopez', 120, '777-555-1253', 'ava.lopez@ecole.org', 2036, 1);

-- Insertion de 5 enseignants
INSERT INTO enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES
    (1, 'Alice', 'Dupont', 101, 'Mathématiques', 2020, 'alice.dupont@ecole.org', '777-555-0001', 1),
    (2, 'Bob', 'Martin', 102, 'Physique', 2019, 'bob.martin@ecole.org', '777-555-0002', 2),
    (3, 'Carol', 'Durand', 103, 'Biologie', 2021, 'carol.durand@ecole.org', '777-555-0003', 3),
    (4, 'David', 'Lefebvre', 104, 'Chimie', 2022, 'david.lefebvre@ecole.org', '777-555-0004', 4),
    (5, 'Eva', 'Martinez', 105, 'Informatique', 2021, 'eva.martinez@ecole.org', '777-555-0005', 5);
