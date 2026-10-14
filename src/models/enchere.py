from datetime import datetime

class Enchere:
    def __init__(self, id_enchere, utilisateur, objet, montant):
        # 1. Vérification des règles métier
        if montant <= 0:
            raise ValueError("Le montant doit être strictement positif.")

        # Utilisation de .value si c'est un Enum, ou comparaison directe
        if hasattr(objet.etat, 'value'):
            etat_actuel = objet.etat.value
        else:
            etat_actuel = objet.etat

        if etat_actuel == "TERMINE":
            raise ValueError("L'enchère sur cet objet est déjà clôturée.")

        if montant <= objet.prix_actuel:
            raise ValueError(f"Enchère trop basse : {montant}€ (actuel : {objet.prix_actuel}€)")

        if utilisateur.solde < montant:
            raise ValueError(f"Solde insuffisant : {utilisateur.solde}€ disponibles.")

        # 2. Assignation si tout est valide
        self.id = id_enchere
        self.utilisateur = utilisateur
        self.objet = objet
        self.montant = montant
        self.date = datetime.now()

        # 3. Mise à jour de l'objet (effet de bord)
        objet.prix_actuel = montant