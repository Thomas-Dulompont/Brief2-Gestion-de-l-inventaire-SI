import functools
from tabnanny import check
import time
import functions
import crud

#functions.creer_admin()
#functions.creer_ordi()
#functions.ticket()
#functions.chat_ticket()
#functions.carnet_pret()
#functions.info_user()
#functions.info_user()


# Boucle tant que l'utilisateur ne se connecte pas

while True:
    functions.clear()
    print("""
    Connexion / Inscription

1 - Connexion
2 - Inscription
    """)
    question_login = input("Entrez votre selection : ")

    if question_login[0].lower() == "1":
        functions.clear()
        user_infos = functions.login()
        
        if user_infos != False:
            if functions.check_root(user_infos):
                functions.clear()
                while True:
                    print("""
                \033[1;31m Première connexion root

Pour des raisons de sécurités nous vous invitons à créer un Admin :
        (L'utilisateur "root" sera supprimé)\033[0m
                """)
                    time.sleep(1)
                    functions.create_admin()
                    if len(functions.list_admin()) > 1:
                        functions.delete_root()
                        print("""
Votre Espace à bien été créé ! 
Veuillez vous reconnecter avec votre nouvel Admin
                        """)
                        break
            else:
                break
    elif question_login[0].lower() == "2":
        functions.clear()
        functions.register()
    else:
        print("""
    \033[1;31m Merci de entre Connexion(1) / Inscription(2) ! \n 
    \033[0m \n
            """)
        time.sleep(2)

if functions.check_admin(user_infos):
    while True:
        functions.clear()

        print("""
    Panel Administrateur
    """)
        functions.afficher_liste_tickets_admin_open()
        print("""
1 - Gestion Tickets
2 - Gestion Ordinateurs
        """)
        question_home_admin = input("Entrez votre selection : ")
        
        if question_home_admin == "1" or question_home_admin == "2":
            if question_home_admin == "1":
                functions.create_ticket(user_infos)
            elif question_home_admin == "2":
                print("2")
        else:
            print("""
    \033[1;31m Merci de selectionner un des 2 choix disponnibles ! \n 
    \033[0m \n
            """)
            time.sleep(2)
else:
    while True:
        functions.clear()
        print("""
        Panel Utilisateur
    """)
        functions.afficher_liste_tickets_user_open(user_infos)
        print("""
1 - Choisir Ticket
2 - Créer Ticket
3 - Historique Tickets
        """)
        question_home_user = input("Entrez votre selection : ")
        
        if question_home_user == "1" or question_home_user == "2" or question_home_user == "3":
            if question_home_user == "1":
                functions.clear()
                print("""
            Vos Tickets
                """)
                functions.afficher_liste_tickets_user_open(user_infos)
                print(" ")
                choix_ticket = input("Entrez l'ID du ticket que vous souhaitez consulter : ")
                if isinstance(int(choix_ticket), int):
                    choix_ticket = int(choix_ticket)            
                    if functions.get_single_ticket(choix_ticket) != None:
                        ticket = crud.get_single_ticket(choix_ticket)
                        if ticket[3] == functions.global_status_open:
                            functions.clear()
                            while True:
                                print("""
Ticket n°{}
Ordinateur n°{}
Description :
\033[1;31m{}\033[0m
            """.format(str(ticket[0]), str(ticket[2]), str(ticket[4])))
                                print("------------------------------------------")
                                functions.afficher_liste_messages_chat(ticket[0])
                                print("""
1 - Répondre
2 - Cloturer le ticket
3 - Retour
                                """)
                                question_chat = input("Entrez votre selection : ")

                                if question_chat[0].lower() == "1":
                                    functions.create_message_chat_ticket(ticket[0], user_infos[3])
                                    print("""
    \033[1;32m Votre message a été envoyé ! \n 
    \033[0m
                                    """)
                                    time.sleep(1)
                                elif question_chat[0].lower() == "2":
                                    question_close = input("Etes-vous sûr de vouloir cloturer ce ticket ? (O = oui / N = non) :")
                                    if question_close.lower() == "o":
                                        functions.clear()
                                        functions.change_status_ticket(ticket[0], functions.global_status_close)
                                        print("""
    Votre ticket a été cloturé ! 
                                        """)
                                        time.sleep(1)
                                        break
                                    else:
                                        functions.clear()
                                        print("""
    Votre ticket n'a pas été cloturer
                                        """)
                                        time.sleep(1)
                                elif question_chat[0].lower() == "3":
                                    break
                                else:
                                    print("""
    \033[1;31m Merci de selectionner un des 2 choix disponnibles ! \n 
    \033[0m \n
                                    """)
                                time.sleep(2)
                        else:
                            print("""

    \033[1;31m Veuillez entrer un ID valable ! \n 
    \033[0m \n
                            """)
                            time.sleep(2)
                    else:
                        functions.clear()
                        print("""

    \033[1;31m L'ID du ticket n'existe pas ! \n
     \033[0m \n
                                                
                            """)
                        time.sleep(2)
                else:
                    functions.clear()
                    print("""

    \033[1;31m Veuillez entrer un ID valable ! \n 
    \033[0m \n
                    """)
                    time.sleep(2)
            elif question_home_user == "2":
                functions.create_ticket(user_infos)
            elif question_home_user == "3":
                while True:
                    functions.clear()
                    print("""
        Historique Tickets
                """)
                    functions.afficher_liste_tickets_user_close(user_infos)
                    print("""
1 - Choisir un Ticket
2 - Retour
                    """)
                    question_home_user = input("Entrez votre selection : ")
                    if question_home_user == "1":
                        functions.clear()
                        print("""
        Choisir un Ticket
                        """)
                        functions.afficher_liste_tickets_user_close(user_infos)
                        print(" ")
                        choix_ticket_old = input("Entrez l'ID du ticket que vous souhaitez consulter : ")
                        if functions.get_single_ticket(choix_ticket_old) != None:
                            ticket = crud.get_single_ticket(choix_ticket_old)
                            if ticket[3] == functions.global_status_close:
                                functions.clear()
                                while True:
                                    print("""
    Ticket n°{}
    Ordinateur n°{}
    Description :
    \033[1;31m{}\033[0m
                """.format(str(ticket[0]), str(ticket[2]), str(ticket[4])))
                                    print("------------------------------------------")
                                    functions.afficher_liste_messages_chat(ticket[0])
                                    print("""
    1 - Retour
                                    """)
                                    question_chat = input("Entrez votre selection : ")
                                    if question_chat == "1":
                                        break
                                    else:
                                        print("""

    \033[1;31m Merci de selectionner un des 3 choix disponnibles ! \n 
    \033[0m \n
                                        """)
                            else:
                                print("""

    \033[1;31m Veuillez entrer un ID valable ! \n 
    \033[0m \n
                                """)
                                time.sleep(2)
                    elif question_home_user == "2":
                        break
                    else:
                        functions.clear()
                        print("""
    \033[1;31m Merci de selectionner un des 2 choix disponnibles ! \n 
    \033[0m \n
                        """)
                        time.sleep(2)


        else:
            functions.clear()
            print("""

    \033[1;31m Merci de selectionner un des 3 choix disponnibles ! \n 
    \033[0m \n
            """)
            time.sleep(2)