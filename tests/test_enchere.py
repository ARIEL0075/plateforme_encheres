import pytest
from src.models.utilisateur import Utilisateur
from src.models.objet import Objet, Etat
from src.models.enchere import Enchere

# Fixture pour simplifier la création des objets de test
@pytest.fixture
def data_test():
    user = Utilisateur(1, "Ariel", 100.0)
    objet = Objet(1, "Montre", "Belle montre", 50.0)
    return user, objet

def test_creation_enchere_valide(data_test):
    user, objet = data_test
    enchere = Enchere(1, user, objet, 60.0)
    assert enchere.montant == 60.0
    assert enchere.utilisateur == user
    assert enchere.objet == objet

def test_enchere_montant_invalide(data_test):
    user, objet = data_test
    with pytest.raises(ValueError, match="Montant invalide"):
        Enchere(1, user, objet, 0) # Montant à 0

def test_enchere_objet_termine(data_test):
    user, objet = data_test
    objet.etat = Etat.TERMINE # On force l'objet en état terminé
    with pytest.raises(ValueError, match="L'enchère est terminée"):
        Enchere(1, user, objet, 60.0)

def test_enchere_montant_trop_bas(data_test):
    user, objet = data_test
    # Le prix actuel est 50.0, on tente d'enchérir à 40.0
    with pytest.raises(ValueError, match="Le montant doit être supérieur au prix actuel"):
        Enchere(1, user, objet, 40.0)

def test_enchere_solde_insuffisant(data_test):
    user, objet = data_test
    user.solde = 10.0 # Solde insuffisant pour enchérir à 60.0
    with pytest.raises(ValueError, match="Solde insuffisant"):
        Enchere(1, user, objet, 60.0)
