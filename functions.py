from concurrent.futures import process
from datetime import date
from email import message
from pickle import FALSE
import crud

def creer_user():
    nom = input ("Entrez votre nom : ")
    prenom = input ("Entrez votre prenom : ")
    mdp = input ("Entrez votre mot de passe  : ")

    crud.create_user (False, nom, prenom, mdp)

def creer_admin():
    nom = input ("Entrez votre nom : ")
    prenom = input ("Entrez votre prenom : ")
    mdp = input ("Entrez votre mot de passe  : ")

    crud.create_user (True, nom, prenom, mdp) 

def creer_ordi():
    marque = input ("Entrez votre marque : ")
    processeur = input ("Entrez votre processeur : ")
    carte_graphique = input ("Entrez votre carte_graphique : ")
    ram = input ("Entrez votre ram : ")
    disque = input ("Entrez votre disque: ")

    crud.type_ordi (marque, processeur, carte_graphique, ram, disque)

def ticket ():
    date = input ("Entrez la date : ")
    id_ref_pret = input ("Entrez la reference du pret : ")
    status = input ("Entrez le status : ")
    message = input ("Entrez le message : ")

    crud.ticket (date, id_ref_pret, status, message)

def chat_ticket ():
    date = input ("Entrez la date : ")
    id_ticket = input ("Entrez la reference du ticket : ")
    auteur = input ("Entrez l'auteur : ")
    message = input ("Entrez le message : ")

    crud.ticket (date, id_ticket, auteur, message)

def carnet_pret ():
    reference_pc = input ("Entrez la reference du pc : ")
    id_user = input ("Entrez l'identite de l'user : ") 
    id_pc = input ("Entrez l'identite du pc : ")

    crud.carnet_pret (reference_pc, id_user, id_pc)


    
