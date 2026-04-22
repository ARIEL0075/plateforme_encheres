from datetime import datetime

class Enchere:
    def __init__(self, id_enchere, utilisateur, objet, montant):
        if montant <= 0:
            raise ValueError("Montant invalide")

        if objet.etat.value == "TERMINE":
            raise ValueError("L'enchère est terminée")

        if montant <= objet.prix_actuel:
            raise ValueError("Le montant doit être supérieur au prix actuel")

        if utilisateur.solde < montant:
            raise ValueError("Solde insuffisant")

        self.id = id_enchere
        self.utilisateur = utilisateur
        self.objet = objet
        self.montant = montant
        self.date = datetime.now()

        # Mise à jour du prix de l'objet
        objet.prix_actuel = montant