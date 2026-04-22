from src.models.utilisateur import Utilisateur

def test_crediter():
    
    user = Utilisateur(1, "Ariel", 100.0)
    user.crediter(50.0)
    assert user.solde == 150.0
    print("Le test créditer a réussi !")

def test_debiter():
    user = Utilisateur(1, "Ariel", 100.0)
    succes = user.debiter(30.0)
    assert succes == True
    assert user.solde == 70.0

    echec = user.debiter(200.0)
    assert echec == False 
    assert user.solde == 70.0