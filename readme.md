# Système de gestion de l’inventaire SI

## Projet

Notre groupe a créé un outil de gestion pour les prêts d’ordinateurs en interne, seul les administrateurs peuvent créer et assigner des ordinateurs.
Les utilisateurs peuvent créer des « tickets » en cas de problèmes avec l’ordinateur assigner.


## Fonctionnalités

Utilisateurs :
- Créer des tickets
- Voir les messages d’un ticket
- Clôturer un ticket
- Voir l’historique des anciens tickets

Admin :
- Première connexion en tant que « root » (mail: root, mdp: root)
- Liste de tous les tickets
- Répondre / Clôturer un ticket
- Ajouter / supprimer un ordinateur
- Supprimer un utilisateur
- Changer le rôle d’un utilisateur
- Assigner un ordinateur à un utilisateurs


## Contexte du projet

Le service SI de l'entreprise CFA.co a un soucis avec son outil de gestion de l'inventaire et des tickets. Ils souhaitent que vous en développiez un en interne le temps que le soucis soit réglé.

​
Le commanditaire attend de votre outil les fonctionnalités suivantes :
- Espace de création d’un compte
- Création d’un espace admin qui permet de voir les tickets ouverts et avoir quelques statistiques (Nombre de pc prêtés en ce moment, nombre de panne par modèle)

Création d’un espace utilisateur qui permet :
- d’ajouter/enlever de sa liste un ordinateur
- d’ajouter ses informations (Infos sur le PC)
- de créer un rapport de bug
- Système de messages sous les tickets (Pour échanger entre les admins et les utilisateurs)

​
Pour se faire, vous aurez droit d'utiliser Python, et le module sqlite3.

## Modalités pédagogiques

- Groupe de 3
- Durée : 5 jours

## Critères de performance

- Les fonctionnalités du cahier des charges sont réalisées.
- Utilisation de python de de sqlite 3
- Code clair et documenté.
