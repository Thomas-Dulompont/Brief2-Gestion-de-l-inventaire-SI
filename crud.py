import sqlite3

connexion = sqlite3.connect("./BDD/bdd.db")
curseur = connexion.cursor()