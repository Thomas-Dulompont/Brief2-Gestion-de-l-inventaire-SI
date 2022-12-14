import functools
from lib2to3.pgen2.token import RPAR
from tabnanny import check
import time
import functions
import crud

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
                # Boucle pour supprimer le root
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
                        functions.clear()
                        print("""
Votre Espace à bien été créé ! 
Veuillez vous reconnecter avec votre nouvel Admin
                        """)
                        time.sleep(2)
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
    ###
    # Boucle pour le panel admin
    ###
    while True:
        functions.clear()
        print("""
    Panel Administrateur
    """)
        print("Les 5 derniers tickets ouverts : ")
        functions.afficher_liste_tickets_admin_open(5)
        print("""
1 - Afficher tous les tickets
2 - Gestion Ordinateurs
3 - Gestion Utilisateurs
4 - Assigner un Ordinateur
        """)
        question_home_admin = input("Entrez votre selection : ")
        
        if question_home_admin == "1" or question_home_admin == "2" or question_home_admin == "3" or question_home_admin == "4":
            if question_home_admin == "1":
                ###
                # Boucle Afficher tous les tickets
                ###
                while True:
                    functions.clear()
                    print("""
    Les Tickets Ouverts
                    """)
                    functions.afficher_liste_tickets_admin_open(0)
                    print("""
1 - Voir un ticket
2 - Retour
                    """)
                    question_ticket_admin = input("Entrez votre selection : ")
                    if question_ticket_admin == "1":
                        choix_ticket = input("\nEntrez l'ID du ticket que vous souhaitez consulter : ")
                        if functions.get_single_ticket_admin(choix_ticket) != None:
                            ticket = functions.get_single_ticket_admin(choix_ticket)
                            functions.clear()
                            ###
                            # Boucle messages tickets
                            ###
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
    1 - Repondre
    2 - Cloturer ticket
    3 - Retour
                                """)
                                question_chat = input("Entrez votre selection : ")
                                if question_chat == "1":
                                    functions.create_message_chat_ticket(ticket[0], user_infos[3], user_infos[1])
                                    print("""
    \033[1;32m Votre message a été envoyé ! \n 
    \033[0m
                                    """)
                                    time.sleep(1)
                                elif question_chat == "2":
                                    question_close = input("Etes-vous sûr de vouloir cloturer ce ticket ? (O = oui / N = non) :")
                                    if question_close.lower() == "o":
                                        functions.clear()
                                        functions.change_status_ticket(ticket[0], functions.global_status_close)
                                        print("""
    Le ticket a été cloturé ! 
                                        """)
                                        time.sleep(1)
                                        break
                                    else:
                                        functions.clear()
                                        print("""
    Le ticket n'a pas été cloturer
                                        """)
                                        time.sleep(1)
                                elif question_chat == "3":
                                    break
                                else:
                                    print("""
    \033[1;31m Merci de selectionner un des 2 choix disponnibles ! \n 
    \033[0m \n
                                    """)
                        else:
                            functions.clear()
                            print("""

    \033[1;31m L'ID du ticket n'existe pas ! \n
    \033[0m \n
                                                        
                            """)
                            time.sleep(2)
                    elif question_ticket_admin == "2":
                        break
                    else:
                        print("""
    \033[1;31m Merci de selectionner un des 2 choix disponnibles ! \n 
    \033[0m \n
                        """)
                        time.sleep(2)
            elif question_home_admin == "2":
                ###
                # Afficher ordinateurs
                ###
                while True:
                    functions.clear()
                    print("""
    Tous les PC
                    """)
                    functions.afficher_liste_ordi()
                    print("""
1 - Ajouter un PC
2 - Retour
                    """)
                    question_ordi_home = input("Entrez votre selection : ")
                    if question_ordi_home == "1":
                        functions.clear()
                        functions.create_ordi()
                        print("""
    \033[1;32m Le PC a bien été créé ! \n 
    \033[0m
                        """)
                        time.sleep(2)
                    elif question_ordi_home == "2":
                        break
                    else:
                        print("""
    \033[1;31m Merci de selectionner un des 2 choix disponnibles ! \n 
    \033[0m \n
                        """)
            elif question_home_admin == "3":
                while True:
                    functions.clear()
                    print("""
    Gestion Utilisateurs
                    """)
                    functions.afficher_liste_user()
                    print("""
1 - Supprimer un utilisateur
2 - Definir un Utilisateur Admin
3 - Retour
                    """)
                    question_user_admin = input("Entrez votre selection : ")
                    if question_user_admin == "1":
                        functions.clear()
                        print("""
    Supprimer Utilisateur
                    """)
                        functions.afficher_liste_user()
                        question_user_admin_delete = input("\nEntrez l'ID de l'utilisateur : ")
                        if int(question_user_admin_delete) == user_infos[0]:
                            functions.clear()
                            print("""
    \033[1;31mVous ne pouvez pas supprimer votre compte !
    \033[0m
                            """)
                            time.sleep(1.5)
                        functions.delete_user(int(question_user_admin_delete))
                        functions.clear()
                        print("""
    \033[1;32m L'utilisateur à bien était supprimé ! \n 
    \033[0m
                        """)
                        time.sleep(1.5)
                    elif question_user_admin == "2":
                        functions.clear()
                        print("""
    Changer rôle Utilisateur
                    """)
                        functions.afficher_liste_user()
                        question_user_admin_change = input("\nEntrez l'ID de l'utilisateur : ")
                        if int(question_user_admin_change) == user_infos[0]:
                            functions.clear()
                            print("""
    \033[1;31mVous ne pouvez pas changer votre role !
    \033[0m
                            """)
                            time.sleep(1.5)
                        question_user_admin_change_role = input("\nEntrez le role de l'utilisateur (Admin / User): ")
                        functions.change_role(question_user_admin_change, question_user_admin_change_role)
                        functions.clear()
                        print("""
    \033[1;32m Le role de l'utilisateur a bien était changé ! \n 
    \033[0m \n
                        """)
                        time.sleep(1.5)
                    elif question_user_admin == "3":
                        break
                    else:
                        print("""
    \033[1;31m Merci de selectionner un des 3 choix disponnibles ! \n 
    \033[0m \n
                            """)
            elif question_home_admin == "4":
                while True:
                    functions.clear()
                    functions.afficher_liste_user()
                    question_assign_user_admin = input("\nEntrez l'ID de l'utilisateur : ")
                    functions.clear()
                    functions.afficher_liste_ordi()
                    question_assign_pc_admin = input("\nEntrez l'ID de l'ordinateur : ")
                    if functions.get_user(int(question_assign_user_admin)):
                        if functions.get_pc(int(question_assign_pc_admin)):
                            id_user = int(question_assign_user_admin)
                            id_pc = int(question_assign_pc_admin)
                            if functions.create_assign(id_user, id_pc):
                                functions.clear()
                                print("""
    \033[1;32m Le PC à bien été assigné à cet utilisateur !\033[0m
                                """)
                                time.sleep(1.5)
                                break
                        else:
                            functions.clear()
                            print("""
    \033[1;31m L'ID du PC n'est pas valable ou n'existe pas !\033[0m
                            """)
                            time.sleep(1.5)
                    else:
                        functions.clear()
                        print("""
    \033[1;31m L'ID de l'utilisateur n'est pas valable ou n'existe pas !\033[0m
                        """)
                        time.sleep(1.5)
            else:
                print("""
    \033[1;31m Merci de selectionner un des 4 choix disponnibles ! \n 
    \033[0m \n
                """)
                time.sleep(2)
        else:
            print("""
    \033[1;31m Merci de selectionner un des 4 choix disponnibles ! \n 
    \033[0m \n
            """)
            time.sleep(2)
else:
    # Boucle pour le panel user
    while True:
        functions.clear()
        print("""
        Panel Utilisateur
    """)
        functions.afficher_liste_tickets_user_open(user_infos, 5)
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
                functions.afficher_liste_tickets_user_open(user_infos, 0)
                print(" ")
                choix_ticket = input("Entrez l'ID du ticket que vous souhaitez consulter : ")
                if isinstance(int(choix_ticket), int):
                    choix_ticket = int(choix_ticket)            
                    if functions.get_single_ticket(choix_ticket, user_infos) != None:
                        ticket = functions.get_single_ticket(choix_ticket, user_infos)
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
                                    functions.create_message_chat_ticket(ticket[0], user_infos[3], user_infos[1])
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
                functions.clear()
                print("""
    Créer un ticket
                
Vos ordinateurs :""")
                functions.afficher_liste_ordi_assign(user_infos[0])
                print(" ")
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
                        if functions.get_single_ticket(choix_ticket_old, user_infos) != None:
                            ticket = functions.get_single_ticket(choix_ticket_old, user_infos)
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