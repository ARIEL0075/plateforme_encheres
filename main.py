from src.models.utilisateur import Utilisateur
from src.models.objet import Objet
from src.models.enchere import Enchere

def demarrer_simulation():
    print("--- Démarrage de la Plateforme d'Enchères ---")
    
    # 1. Création des acteurs
    ariel = Utilisateur(1, "Ariel", 200.0)
    print(f"Utilisateur créé : {ariel.nom} avec un solde de {ariel.solde}€")
    
    # 2. Création de l'objet
    montre = Objet(1, "Montre Vintage", "Une belle montre", 50.0)
    print(f"Objet en vente : {montre.nom} (Prix actuel : {montre.prix_actuel}€)")
    
    # 3. Simulation d'une enchère
    try:
        nouvelle_enchere = Enchere(1, ariel, montre, 75.0)
        montre.mettre_a_jour_prix(nouvelle_enchere.montant)
        print(f"Enchère réussie ! Nouveau prix : {montre.prix_actuel}€")
    except ValueError as e:
        print(f"Erreur lors de l'enchère : {e}")

if __name__ == "__main__":
    demarrer_simulation()
