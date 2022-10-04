import sqlite3

# fonction qui ajoute un utilisateur
def create_user(is_admin, nom, prenom, mdp):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    if is_admin:
        curseur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?)", (None, 1, nom, prenom, mdp))
    else:
        curseur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?)", (None, 0, nom, prenom, mdp))
    connexion.commit()

# fonction qui supprime un utilisateur
def delete_user(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("DELETE FROM user WHERE id = ?", (id,))
    connexion.commit()

# fonction qui cree un ticket
def create_ticket(date, id_ref_pret, status, message):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("INSERT INTO ticket VALUES(?, ?, ?, ?, ?)", (None, date, id_ref_pret, status, message))
    connexion.commit()

# fonction qui ajoute un ordinateur
def create_type_ordi(marque, processeur, carte_graphique, ram, disque):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("INSERT INTO type_ordi VALUES(?, ?, ?, ?, ?, ?)", (None, marque, processeur, carte_graphique, ram, disque))
    connexion.commit()

# fonction qui supprime un ordinateur
def delete_type_ordi(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("DELETE FROM type_ordi WHERE id = ?", (id,))
    connexion.commit()

# fonction qui ajoute un chat_tickets
def create_chat_tickets(date, id_ticket, auteur, message):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("INSERT INTO chat_tickets VALUES(?, ?, ?, ?, ?)", (None, date, id_ticket, auteur, message))
    connexion.commit()

# fonction qui ajoute un pret d ordinateur
def create_carnet_pret(reference_pc, id_user, id_pc):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("INSERT INTO carnet_pret VALUES(?, ?, ?)", (reference_pc, id_user, id_pc))
    connexion.commit()

# fonction qui supprime un pret d ordinateur
def delete_carnet_pret(reference_pc):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("DELETE FROM carnet_pret WHERE reference_pc = ?", (reference_pc,))
    connexion.commit()