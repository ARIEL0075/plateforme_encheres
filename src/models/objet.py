from enum import Enum

class Etat(Enum):
    EN_COURS = "EN_COURS"
    TERMINE = "TERMINE"

class Objet:
    def __init__(self, id_objet, nom, description, prix_depart):
        if prix_depart < 0:
            raise ValueError("Le prix initial doit être positif")

        self.id = id_objet
        self.nom = nom
        self.description = description
        self.prix_depart = prix_depart
        self.prix_actuel = prix_depart
        self.etat = Etat.EN_COURS


    def mettre_a_jour_prix(self, nouveau_prix):
        """
        Met à jour le prix actuel de l'objet si la nouvelle offre est supérieure au prix actuel.
        """
        if nouveau_prix > self.prix_actuel:
            self.prix_actuel = nouveau_prix

