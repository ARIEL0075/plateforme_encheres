from enum import Enum

class Etat(Enum):
    EN_COURS = "EN_COURS"
    TERMINE = "TERMINE"

class Objet:
    def __init__(self, id_objet, nom, description, prix_initial):
        if prix_initial < 0:
            raise ValueError("Le prix initial doit être positif")

        self.id = id_objet
        self.nom = nom
        self.description = description
        self.prix_initial = prix_initial
        self.prix_actuel = prix_initial
        self.etat = Etat.EN_COURS