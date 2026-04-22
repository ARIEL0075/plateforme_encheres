import pytest
from src.models.objet import Objet, Etat

def test_creation_objet_valide():
    """
    Vérifi qu'un objet est correctement initialisé avec les bonne valeurs.
    """
    # On crée une instance pour tester l'initialisation
    montre = Objet(1, "Montre", "une belle montre vintage", 150.0)
    
    assert montre.id == 1
    assert montre.nom == "Montre"
    assert montre.prix_depart == 150.0
    # On vérifie que l'état par défaut est bien EN_COURS
    assert montre.etat == Etat.EN_COURS

def test_mise_a_jour_prix():
    """
    Vérifie que le prix actuel augmente bien quand une nouvelle offre est faite.
    """
    table = Objet(2, "Table", "Table en bois", 50.0)

    # Simulation d'une nouvelle enchère
    table.mettre_a_jour_prix(75.0)
    
    assert table.prix_actuel == 75.0

def test_creation_objet_prix_negatif():
    """
    Vérifie que le programme bloque bien la création d'un objet avec un prix invalide.
    C'est un test de 'robustesse'.
    """
    # On s'attend à ce que le code lève une ValueError, car on ne peut pas 
    # enchérir sur un prix négatif.
    with pytest.raises(ValueError):
        Objet(3, "Objet erroné", "Description", -10.0)
