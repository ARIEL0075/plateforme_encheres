Cahier des Charges
Plateforme d’Enchères en Ligne
Projet : Projet 5 – Plateforme d’Enchères en Ligne
Membres : HOUETO Ariel & APLOGAN Epiphanio
Langage : Python 3.x
Date : 20/04/2026
1. 🎯 Contexte et Objectifs
La vente aux enchères est un mécanisme transactionnel complexe impliquant plusieurs acteurs et des règles strictes de validation.
Ce projet vise à concevoir une plateforme simulée d’enchères en ligne permettant de :
•	Gérer des utilisateurs avec un solde virtuel 
•	Mettre en vente des objets 
•	Permettre des enchères en temps réel simulé 
•	Déterminer automatiquement un gagnant 
🎯 Objectifs pédagogiques
•	Maîtriser la programmation orientée objet (POO) en Python 
•	Structurer un projet logiciel de manière professionnelle 
•	Implémenter des règles métier complexes 
•	Utiliser des tests unitaires pour garantir la qualité du code 

2. Répartition des Responsabilités
🔹 HOUETO Ariel
•	Configuration du dépôt Git 
•	Développement de la logique métier (Business Rules) 
•	Implémentation de la persistance des données (SQLite) 
•	Gestion des exceptions et validation des règles 
🔹 APLOGAN Epiphanio
•	Conception de l’interface utilisateur (CLI ou Web avec Flask) 
•	Rédaction des tests unitaires (Pytest) 
•	Documentation technique 
•	Vérification de la conformité PEP 8 

3. Architecture du Projet
Le projet sera structuré de manière modulaire :
project/
│
├── src/
│   ├── models/
│   │   ├── utilisateur.py
│   │   ├── objet.py
│   │   ├── enchere.py
│   │
│   ├── services/
│   │   ├── logique_metier.py
│   │
│   ├── database/
│   │   ├── db.py
│   │
│   ├── main.py
│
├── tests/
│   ├── test_utilisateur.py
│   ├── test_objet.py
│   ├── test_enchere.py
│
├── requirements.txt
└── README.md

4.  Modélisation Objet (POO)
🔹 Classe Utilisateur
•	id 
•	nom 
•	solde 
Méthodes :
•	créditer() 
•	débiter() 
•	vérifier_solde() 

🔹 Classe Objet
•	id 
•	nom 
•	description 
•	prix_initial 
•	prix_actuel 
•	état (Enum : EN_COURS, TERMINE)
🔹 Classe Enchere
•	id 
•	utilisateur 
•	objet 
•	montant 
•	date 
🔹 Relations
•	Un utilisateur peut faire plusieurs enchères 
•	Un objet peut recevoir plusieurs enchères 
•	Une enchère appartient à un utilisateur et à un objet 
5. ⚙️ Règles Métier
•	Une enchère doit être strictement supérieure au prix actuel 
•	Un utilisateur doit avoir un solde suffisant 
•	Une enchère ne peut être faite que si l’objet est EN_COURS 
•	Une enchère a une durée limitée 
•	Le gagnant est l’utilisateur ayant proposé la plus haute enchère 
•	Le solde est débité uniquement à la fin si l’utilisateur gagne 

6. Persistance des Données
Le système utilisera SQLite via le module sqlite3.
Tables :
•	utilisateurs (id, nom, solde) 
•	objets (id, nom, prix_initial, prix_actuel, état) 
•	encheres (id, utilisateur_id, objet_id, montant, date) 

7. Gestion des Erreurs
Le système devra gérer :
•	Enchère invalide (montant insuffisant) 
•	Solde insuffisant 
•	Objet inexistant 
•	Enchère terminée 
Exceptions personnalisées :
•	EnchereInvalideError 
•	SoldeInsuffisantError 
•	ObjetIndisponibleError 
8. Tests Unitaires
•	Utilisation du framework pytest 
•	Tests pour : 
o	Création d’utilisateur 
o	Ajout d’objet 
o	Validation d’enchère 
o	Détermination du gagnant 
👉 Chaque fonctionnalité doit être testée avant intégration (TDD).

9. Interface Utilisateur
Deux options possibles :
Option 1 : CLI (Terminal)
•	Menu interactif 
•	Saisie utilisateur simple 
Option 2 : Web (Flask) 
•	Page d’accueil 
•	Liste des objets 
•	Formulaire d’enchère 
•	Affichage des résultats 

10. Workflow de Développement
•	Utilisation de Git avec branches : 
o	main (stable) 
o	dev (intégration) 
o	feature/* (développement) 
•	Validation via Pull Requests 

11.  Planning (Bloc 1)
1.	Mise en place de l’environnement (venv + requirements.txt) 
2.	Initialisation du dépôt Git 
3.	Création de la structure du projet 
4.	Définition des classes (modélisation) 
5.	Écriture des premiers tests unitaires 

12. Scénarios d’Utilisation
Scénario 1 :
1.	Un utilisateur s’inscrit 
2.	Il crédite son compte 
3.	Il consulte les objets 
4.	Il enchérit sur un objet 
Scénario 2 :
1.	Plusieurs utilisateurs enchérissent 
2.	L’enchère se termine 
3.	Le système désigne le gagnant 
4.	Le solde du gagnant est débité 
13. Améliorations Futures
•	Système de notifications 
•	Historique des enchères 
•	Gestion du temps réel (timer) 
•	Interface graphique avancée 
•	Authentification sécurisée

