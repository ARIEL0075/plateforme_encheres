from enum import Enum

class Etat(Enum):
    EN_COURS = "EN_COURS"
    TERMINE = "TERMINE"


class Objet:
    def __init__(self, id_objet, nom, description, prix_depart, prix_actuel=None, etat=None):
        if prix_depart < 0:
            raise ValueError("Le prix initial doit être positif")

        self.id_objet = id_objet
        self.nom = nom
        self.description = description
        self.prix_depart = prix_depart
        self.prix_actuel = prix_actuel if prix_actuel is not None else prix_depart
        self.etat = etat if etat else Etat.EN_COURS