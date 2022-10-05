import sqlite3

connexion = sqlite3.connect("./BDD/bdd.db")
curseur = connexion.cursor()

curseur.execute('''CREATE TABLE user
                (
                    id INTEGER PRIMARY KEY,
                    role INTERGER,
                    nom TEXT,
                    prenom TEXT,
                    mail TEXT UNIQUE,
                    mot_de_passe TEXT
                )
''')

curseur.execute('''CREATE TABLE type_ordi
                (
                    id INTEGER PRIMARY KEY,
                    marque TEXT,
                    processeur TEXT,
                    carte_graphique TEXT,
                    ram INTEGER,
                    disque INTEGER
                )
''')

curseur.execute('''CREATE TABLE carnet_pret
                (
                    reference_pc INTEGER PRIMARY KEY,
                    id_user INTEGER,
                    id_pc INTEGER,
                    FOREIGN KEY (id_user)
                        REFERENCES user(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (id_pc)
                        REFERENCES type_ordi(id)
                        ON DELETE CASCADE
                )
''')

curseur.execute('''CREATE TABLE ticket
                (
                    id INTEGER PRIMARY KEY,
                    date INTEGER,
                    id_ref_pret TEXT,
                    status INTEGER,
                    message TEXT,
                    FOREIGN KEY (id_ref_pret)
                        REFERENCES carnet_pret(reference_pc)
                        ON DELETE CASCADE
                )
''')

curseur.execute('''CREATE TABLE chat_tickets
                (
                    id_message INTEGER PRIMARY KEY,
                    date INTEGER,
                    id_ticket INTEGER,
                    auteur TEXT,
                    message TEXT,
                    FOREIGN KEY (id_ticket)
                        REFERENCES ticket(id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (auteur)
                        REFERENCES user(id)
                        ON DELETE CASCADE
                )
''')

connexion.commit()
connexion.close()