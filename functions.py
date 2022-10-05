import os
from datetime import date
import time
from turtle import home
import crud

def clear():
    os.system('clear')

def creer_admin():
    nom = input ("Entrez votre nom admin : ")
    prenom = input ("Entrez votre prenom : ")
    mdp = input ("Entrez votre mot de passe  : ")

    crud.create_user (True, nom, prenom, mdp) 

def creer_ordi():
    marque = input ("Entrez votre marque : ")
    processeur = input ("Entrez votre processeur : ")
    carte_graphique = input ("Entrez votre carte_graphique : ")
    ram = input ("Entrez votre ram : ")
    disque = input ("Entrez votre disque: ")

    crud.create_type_ordi (marque, processeur, carte_graphique, ram, disque)

def ticket ():
    date = input ("Entrez la date : ")
    id_ref_pret = input ("Entrez la reference du pret : ")
    status = input ("Entrez le status : ")
    message = input ("Entrez le message : ")

    crud.create_ticket (date, id_ref_pret, status, message)

def chat_ticket ():
    date = input ("Entrez la date : ")
    id_ticket = input ("Entrez la reference du ticket : ")
    auteur = input ("Entrez l'auteur : ")
    message = input ("Entrez le message : ")

    crud.create_chat_tickets (date, id_ticket, auteur, message)

def carnet_pret ():
    reference_pc = input ("Entrez la reference du pc : ")
    id_user = input ("Entrez l'identite de l'user : ") 
    id_pc = input ("Entrez l'identite du pc : ")

    crud.create_carnet_pret (reference_pc, id_user, id_pc)

def info_user(id):
    return crud.get_info_user(id)
    

def register():
    """
    Fonction qui permet à l'utilisateur de créer un compte
    """
    nom = input ("Entrez votre nom : ")
    prenom = input ("Entrez votre prenom : ")
    mail = input("Entrez votre email : ")
    mdp = input ("Entrez votre mot de passe  : ")

    crud.create_user(False, nom, prenom, mail, mdp)
    clear()
    print("""

\033[1;32m Inscription validée ! \n

\033[0m Redirection vers la page d'accueil en cours ... \n

""")
    time.sleep(2)
    home_page()

def login():
    """
    Fonction qui demande à l'utilisateur son email & mot de passe et qui vérifie si la base contient l'email indiqué avec le mot de passe, elle compte également le nombre d'essais avant de renvoyer à l'accueil
    """

    essais = 0
    while True:
        mail = input("Entrez votre email : ")
        mdp = input ("Entrez votre mot de passe  : ")

        user_infos = crud.verify_user(mail, mdp)

        if user_infos != None:
            print("""

\033[1;32m Authentification réussit ! \n

\033[0m Redirection vers votre espace en cours ...\n

""")
            time.sleep(2)
            return user_infos
        else:
            print("""

\033[1;31m Adresse email ou mot de passe incorrect ! \n

\033[0m Redirection vers la page d'accueil en cours ... \n

""")
            time.sleep(2)
            home_page()
            

def home_page():
    """
    Fonction qui demande à l'utilisateur si il souhaite se connecter / s'inscrire
    """
    clear()
    print("""
    Connexion / Inscription

1 - Connexion
2 - Inscription

    """)
    question_login = input("Entrez votre selection : ")

    if question_login[0].lower() == "1":
        clear()
        login()
    elif question_login[0].lower() == "2":
        clear()
        register()
    else:
        print(" Merci de selectionner entre Connexion & Inscription ! ")
