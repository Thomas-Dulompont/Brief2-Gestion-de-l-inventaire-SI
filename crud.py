import sqlite3
import hashlib

# fonction qui ajoute un utilisateur
def create_user(is_admin, nom, prenom, mail, mdp):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    mdp = hashlib.sha256(mdp.encode()).hexdigest()

    if is_admin:
        curseur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?)", (None, 1, nom, prenom, mail, mdp,))
    else:
        curseur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?)", (None, 0, nom, prenom, mail, mdp,))
    connexion.commit()
    connexion.close()

# fonction qui supprime un utilisateur
def delete_user(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("DELETE FROM user WHERE id = ?", (id,))
    connexion.commit()
    connexion.close()

# fonction qui cree un ticket
def create_ticket(date, id_ref_pc, message, auteur):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    status = "En cours"
    
    curseur.execute("INSERT INTO ticket VALUES(?, ?, ?, ?, ?, ?)", (None, date, id_ref_pc, status, message, auteur,))
    connexion.commit()
    connexion.close()

# fonction qui supprime un ticket
def delete_ticket(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM ticket WHERE id = ?", (id,))
    connexion.commit()
    connexion.close()

def get_ticket(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT id FROM ticket WHERE id = ?", (id,))
    ticket = curseur.fetchone()
    connexion.commit()
    connexion.close()
    return ticket

def get_ticket_all():
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM ticket")
    tickets = curseur.fetchall()
    connexion.commit()
    connexion.close()
    return tickets

def get_ticket_user(infos_user):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    auteur = infos_user[2] + "_" + infos_user[3]

    curseur.execute("SELECT * FROM ticket WHERE auteur = ?", (auteur,))
    tickets = curseur.fetchall()
    connexion.commit()
    connexion.close()
    return tickets

# fonction qui ajoute un ordinateur
def create_type_ordi(marque, processeur, carte_graphique, ram, disque):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("INSERT INTO type_ordi VALUES(?, ?, ?, ?, ?, ?)", (None, marque, processeur, carte_graphique, ram, disque,))
    connexion.commit()
    connexion.close()

# fonction qui supprime un ordinateur
def delete_type_ordi(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("DELETE FROM type_ordi WHERE id = ?", (id,))
    connexion.commit()
    connexion.close()

# fonction qui ajoute un chat_tickets
def create_chat_tickets(date, id_ticket, auteur, message):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("INSERT INTO chat_tickets VALUES(?, ?, ?, ?, ?)", (None, date, id_ticket, auteur, message,))
    connexion.commit()
    connexion.close()

def get_info_user():
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM user")
    reponse = curseur.fetchone()
    connexion.commit()
    connexion.close()
    return reponse

def verify_user(mail, mdp):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    # Hachage du mdp entré par l'utilisateur
    mdp = hashlib.sha256(mdp.encode()).hexdigest()

    curseur.execute("SELECT mot_de_passe FROM user WHERE mail = ? and mot_de_passe = ?", (mail, mdp,))
    reponse = curseur.fetchone()
    connexion.close()
    return reponse
