import os
from datetime import date
import time
from turtle import home
import crud

today = date.today()

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

###                                     ###
###     FONCTIONS LIEES AUX TICKETS     ###
###                                     ###

def create_ticket(user_infos):
    """
    Fonction qui demande à l'utilisateur de rentrer un ID de PC et un message, et qui fait appel a crud pour créer une nouvelle Ligne dans la DB
    : return (Str) : Retourne un print
    """
    clear()
    date = today.strftime("%d/%m/%Y")
    id_ref_pc = input ("Entrez l'ID de l'ordinateur : ")
    message = input ("Décrivez votre problème : ")
    auteur = user_infos[2] + "_" + user_infos[3]

    crud.create_ticket(date, id_ref_pc, message, auteur)
    print("""

Le Ticket a été créé !

    """)
    time.sleep(2)

def delete_ticket(id):
    """
    Fonction qui supprime le ticket en fonction de l'ID demandé, vérifie si le ticket existe
    : param : id (Int) : ID du ticket
    : return (Str) : Retourne un print
    """
    if crud.get_ticket(id) == None:
        print("L'ID du ticket entré est inéxistant ! ")
        return
    else:
        crud.delete_ticket(id)

    print("Le ticket a été supprimé ! ")

def afficher_liste_tickets():
    """
    Fonction qui affiche la liste des tickets
    """
    grille = []
    for ligne in get_ticket_all():
        ticket = []
        for element in ligne:
            ticket.append(element)

        if "Clos" in ticket:
            pass
        else:
            grille.append(ticket)
            
    
    for grid in grille:
        grid.remove(grid[len(grid) -1])
        print(grid)


def afficher_liste_tickets_user_open(user_infos):
    """
    Fonction qui affiche la liste des tickets de l'utilisateur qui sont encore ouverts
    """
    grille = []
    for ligne in get_ticket_user(user_infos):
        ticket = []
        for element in ligne:
            ticket.append(element)

        if "Clos" in ticket:
            pass
        else:
            grille.append(ticket)
            
    
    for grid in grille:
        grid.remove(grid[len(grid) -1])
        print(grid)




def chat_ticket ():
    date = input ("Entrez la date : ")
    id_ticket = input ("Entrez la reference du ticket : ")
    auteur = input ("Entrez l'auteur : ")
    message = input ("Entrez le message : ")

    crud.create_chat_tickets (date, id_ticket, auteur, message)

def get_ticket_all():
    return crud.get_ticket_all()
    
def get_ticket_user(user_infos):
    return crud.get_ticket_user(user_infos)

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
            return crud.get_info_user()
        else:
            print("""

\033[1;31m Adresse email ou mot de passe incorrect ! \n

\033[0m Redirection vers la page d'accueil en cours ... \n

""")
            time.sleep(2)
            return False
