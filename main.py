import functools
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
            break
    elif question_login[0].lower() == "2":
        functions.clear()
        functions.register()
    else:
        print(" Merci de selectionner entre Connexion & Inscription ! ")
        time.sleep(2)

while True:
    functions.clear()
    print("""
    Panel Utilisateur

""")
    functions.afficher_liste_tickets_user_open(user_infos)
    print("""

 1 - Créer un Ticket
 2 - Gestion Ticket

    """)
    question_home_user = input("Entrez votre selection : ")
    
    if question_home_user == "1" or question_home_user == "2":
        if question_home_user == "1":
            functions.create_ticket(user_infos)
        elif question_home_user == "2":
            print("2")
    else:
        print("Merci de selectionner un des 2 choix disponnibles ! ")
        time.sleep(2)
