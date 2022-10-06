import time
import functions

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
        if functions.login() != False:
            user_infos = functions.login()
            break
    elif question_login[0].lower() == "2":
        functions.clear()
        functions.register()
    else:
        print(" Merci de selectionner entre Connexion & Inscription ! ")
        time.sleep(2)
    
functions.clear()

while True:
    print("""
    Panel Utilisateur

1 - Mes Tickets
2 - Mes Ordinateurs

    """)
    break