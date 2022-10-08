import os
from datetime import date, datetime
import time
from turtle import home
import crud

today = date.today()
now = datetime.now()
global_status_close = "Cloturé"
global_status_open = "En cours"

###                                     ###
###         FONCTIONS GLOBALES          ###
###                                     ###

def clear():
    os.system('clear')

def register():
    """
    Fonction qui permet à l'utilisateur de créer un compte
    """
    nom = input ("Entrez votre nom : ")
    prenom = input ("Entrez votre prenom : ")
    mail = input("Entrez votre email : ")
    mdp = input ("Entrez votre mot de passe : ")

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
        mdp = input ("Entrez votre mot de passe : ")

        user_infos = crud.verify_user(mail, mdp)

        if user_infos != None:
            print("""

\033[1;32m Authentification réussit ! \n

\033[0m Redirection vers votre espace en cours ...\n

""")
            time.sleep(2)
            return crud.get_info_user(mail)
        else:
            print("""

\033[1;31m Adresse email ou mot de passe incorrect ! \n

\033[0m Redirection vers la page d'accueil en cours ... \n

""")
            time.sleep(2)
            return False

###                                     ###
###     FONCTIONS LIEES AUX ADMINS      ###
###                                     ###

def check_root(user_infos):
    """
    Fonction qui vérifie si les informations de l'utilisateur sont égales a celle du root
    : param user_infos (Tuple) : Liste des informations utilisateur
    : return (Bool) : Vrai / Faux si l'user est root
    """
    if user_infos[4] == "root":
        is_admin = crud.check_root(user_infos)
        if is_admin[0] == 1:
            return True
        else:
            return False

def check_admin(user_infos):
    """
    Fonction qui vérifie si l'utilisateur est admin
    : param user_infos (Tuple) : Liste des informations utilisateur
    : return (Bool) : Vrai / Faux si l'user est admin
    """
    is_admin = crud.check_admin(user_infos)
    if is_admin[0] == 1:
        return True
    else:
        return False

def list_admin():
    """
    Fonction qui retourne la liste des admins
    : return (Tuple) : Liste des admins
    """
    return crud.list_admin()

def create_admin():
    """
    Fonction qui créée un Admin
    """
    nom = input ("Entrez votre nom : ")
    prenom = input ("Entrez votre prenom : ")
    mdp = input ("Entrez votre mot de passe  : ")
    mail = input ("Entrez votre email  : ")

    crud.create_user (True, nom, prenom, mail, mdp) 

def delete_root():
    """
    Fonction qui supprime le root
    """
    crud.delete_root()

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

def change_status_ticket(id, status):
    """
    Fonction qui change le status du ticket entré
    : param id (Int) : ID du ticket
    : param status (Str) : Le nouveau Status
    """
    crud.change_status_ticket(id, status)

def afficher_liste_tickets():
    """
    Fonction qui affiche la liste des tickets
    : return grille (Tuple) : Retourne la grille
    """
    grille = []
    for ligne in get_ticket_all():
        ticket = []
        for element in ligne:
            ticket.append(element)

        if global_status_close in ticket:
            pass
        else:
            grille.append(ticket)
    return grille

def afficher_liste_tickets_user_open(user_infos, nb_tickets):
    """
    Fonction qui affiche la liste des tickets de l'utilisateur qui sont encore ouverts
    : param user_infos (Tuple) : Les informations de l'utilisateur
    """
    grille = []
    tickets_user = get_ticket_user(user_infos)
    for ligne in tickets_user:
        ticket = []
        if nb_tickets == 0:
            pass
        elif len(grille) == nb_tickets:
            break
        for element in ligne:
            ticket.append(element)

        if global_status_close in ticket:
            pass
        else:
            grille.append(ticket)
            
    if len(grille) == 0:
        print("Pas de tickets à afficher pour le moment...")
    else:
        print("ID      DATE        PC     STATUS")
        for grid in grille:
            grid.remove(grid[len(grid) -1])
            grid.remove(grid[len(grid) -1])
            print(grid)

def afficher_liste_tickets_user_close(user_infos):
    """
    Fonction qui affiche la liste des tickets de l'utilisateur qui sont cloturés
    : param user_infos (Tuple) : Les informations de l'utilisateur
    """
    grille = []
    for ligne in get_ticket_user(user_infos):
        ticket = []
        for element in ligne:
            ticket.append(element)

        if global_status_open in ticket:
            pass
        else:
            grille.append(ticket)
            
    if len(grille) == 0:
        print("Pas de tickets à afficher pour le moment...")
    else:
        print("ID      DATE        PC     STATUS")
        for grid in grille:
            grid.remove(grid[len(grid) -1])
            grid.remove(grid[len(grid) -1])
            print(grid)

def afficher_liste_tickets_admin_open(nb_tickets):
    """
    Fonction qui affiche la liste de tous les tickets ouverts
    """
    tickets = get_ticket_all()
    grille = []
    for ligne in get_ticket_all():
        if nb_tickets == 0:
            pass
        elif len(grille) == nb_tickets:
            break
        ticket = []
        for element in ligne:
            ticket.append(element)
        if global_status_close in ticket:
            pass
        else:
            grille.append(ticket)
    
    if len(grille) == 0:
        print("Pas de tickets à afficher pour le moment...")
    else:
        print("ID     DATE      PC     STATUS     AUTEUR")
        for grid in grille:
            grid.remove(grid[len(grid) -2])
            print(grid)

def afficher_liste_messages_chat(id):
    messages = crud.get_messages_chat_ticket(id)
    if messages != None:
        for message in messages:
            print("""
\033[1;36m{} - {} :
\033[0m{}
""".format(message[3], message[1], message[4]))
            print("-----")
    else:
        print("Aucun message pour le moment...")

def get_message_chat_ticket(id):
    """
    Fonction qui retourne les messages d'un ticket grace à son ID
    : param id (Int) : ID du ticket
    : return (Tuple) : Les messages du ticket
    """
    messages = crud.get_message_chat_ticket(id)
    return messages

def create_message_chat_ticket (id_ticket, auteur, role):
    """
    Fonction qui ajoute un message à un ticket
    : param id_ticket (Int) : ID du ticket
    : param auteur (Str) : Auteur du message
    """
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    message = input ("Entrez votre message : ")
    if role == 1:
        auteur = "\033[1;31m⭐︎ " + auteur + "\033[0m"

    crud.create_message_chat_tickets(date, id_ticket, auteur, message)

def get_ticket_all():
    """
    Fonction qui retourne tous les tickets existants
    : return (Tuple) : Les tickets    
    """
    return crud.get_ticket_all()
    
def get_ticket_user(user_infos):
    """
    Fonction qui retourne tous les tickets d'un utilisateur
    : param user_infos (Tuple) : Informations de l'utilisateur
    : return (Tuple) : Les tickets de l'utilisateur
    """
    return crud.get_ticket_user(user_infos)

def get_single_ticket(id, user_infos):
    """
    Fonction qui retourne un ticket
    : param id (Int) : ID du ticket
    : return (Tuple) : Ticket
    """
    auteur = auteur = user_infos[2] + "_" + user_infos[3]
    ticket = crud.get_single_ticket(id, auteur)
    return ticket

def get_single_ticket_admin(id):
    """
    Fonction qui retourne un ticket
    : param id (Int) : ID du ticket
    : return (Tuple) : Ticket
    """
    ticket = crud.get_single_ticket_admin(id)
    return ticket

###                                     ###
###       FONCTIONS LIEES AUX PC        ###
###                                     ###

def creer_ordi():
    marque = input ("Entrez votre marque : ")
    processeur = input ("Entrez votre processeur : ")
    carte_graphique = input ("Entrez votre carte_graphique : ")
    ram = input ("Entrez votre ram : ")
    disque = input ("Entrez votre disque: ")

    crud.create_type_ordi (marque, processeur, carte_graphique, ram, disque)