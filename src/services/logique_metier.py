from src.models.objet import Objet
from src.database.repository import Repository

class EnchereService:
    @staticmethod
    def creer_annonce(nom, description, prix):
        """Logique pour valider et créer une annonce."""
        if not nom or float(prix) <= 0:
            return False, "Données invalides"
        
        nouvel_objet = Objet(
            id_objet=None, # Laissé à la DB
            nom=nom,
            description=description,
            prix_depart=float(prix)
        )
        
        Repository.save_objet(nouvel_objet)
        return True, "Annonce créée avec succès"

    @staticmethod
    def verifier_eligibilite_enchere(utilisateur, objet, montant):
        """Centralise les vérifications avant de créer une Enchere."""
        if montant <= objet.prix_actuel:
            return False, "Montant trop bas."
        if utilisateur.solde < montant:
            return False, "Solde insuffisant."
        return True, "Ok"