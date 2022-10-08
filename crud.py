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

def change_status_ticket(id, status):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("UPDATE ticket SET status = ? WHERE id = ?", (status,id,))
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

def get_single_ticket(id, auteur):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM ticket WHERE id = ? AND auteur = ?", (id, auteur,))
    ticket = curseur.fetchone()
    connexion.commit()
    connexion.close()
    return ticket

def get_single_ticket_admin(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM ticket WHERE id = ?", (id,))
    ticket = curseur.fetchone()
    connexion.commit()
    connexion.close()
    return ticket

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
def create_message_chat_tickets(date, id_ticket, auteur, message):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("INSERT INTO chat_tickets VALUES(?, ?, ?, ?, ?)", (None, date, id_ticket, auteur, message,))
    connexion.commit()
    connexion.close()

def get_messages_chat_ticket(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM chat_tickets WHERE id_ticket = ?", (id,))
    messages = curseur.fetchall()
    connexion.commit()
    connexion.close()
    return messages

def get_info_user(mail):
    """
    Fonction qui va chercher dans la DB les informations de l'utilisateur grace à son mail
    : param mail (Str) : Mail entré par l'utilisateur
    """
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM user WHERE mail = ?", (mail,))
    reponse = curseur.fetchone()
    connexion.commit()
    connexion.close()
    return reponse

def verify_user(mail, mdp):
    """
    Fonction qui hash et va chercher dans la base de donnée le mot de passe ainsi que le mail
    : param mail (Str) : Mail entré par l'utilisateur
    : param mdp (Str) : Mot de passe entré par l'utilisateur
    """
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    # Hachage du mdp entré par l'utilisateur
    mdp = hashlib.sha256(mdp.encode()).hexdigest()

    curseur.execute("SELECT mot_de_passe FROM user WHERE mail = ? and mot_de_passe = ?", (mail, mdp,))
    reponse = curseur.fetchone()
    connexion.close()
    return reponse

def check_admin(user_infos):
    """
    Fonction qui va chercher dans la base de donnée le role de l'utilisateur
    : param user_infos (Tuple) : Les informations de l'utilisateur
    : return (Int) : Role de l'utilisateur 
    """
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT role FROM user WHERE mail = ?", (user_infos[4],))
    reponse = curseur.fetchone()
    connexion.close()
    return reponse

def check_root(user_infos):
    """
    Fonction qui regarde si l'administrateur connecter est l'utilisateur supreme (root)
    : param user_infos (Tuple) : Les informations de l'admin
    : return (Tuple) : Retourne le rôle
    """
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT role FROM user WHERE mail = ?", (user_infos[4],))
    reponse = curseur.fetchone()
    connexion.close()
    return reponse

def delete_root():
    """
    Fonction qui supprime le root
    """
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM user WHERE mail = ? AND role = ?", ("root", 1,))
    connexion.commit()
    connexion.close()

def list_admin():
    """
    Fonction qui liste tous les administrateurs
    : return (Tuple) : Liste des admins
    """
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM user WHERE role = ?", (1,))
    reponse = curseur.fetchall()
    connexion.close()
    return reponse