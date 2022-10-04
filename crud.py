import sqlite3

def create_user(is_admin, nom, prenom, mdp):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    if is_admin:
        curseur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?)", (None, 1, nom, prenom, mdp))
    else:
        curseur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?)", (None, 0, nom, prenom, mdp))
    connexion.commit()

def delete_user(id):
    connexion = sqlite3.connect("./BDD/bdd.db")
    curseur = connexion.cursor()
    
    curseur.execute("DELETE FROM user WHERE id = ?", (id,))
    connexion.commit()