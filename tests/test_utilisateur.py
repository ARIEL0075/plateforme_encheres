from src.models.utilisateur import Utilisateur

def test_crediter():
    # 1. Arrange (Préparation) : On crée un utilisateur avec 0.0 solde
    user = Utilisateur(1, "Ariel", 0.0)
    
    # 2. Act (Action) : On crédite 50.0
    user.crediter(50.0)
    
    # 3. Assert (Vérification) : On vérifie si le solde est bien à 50.0
    assert user.solde == 50.0
    print("Le test créditer a réussi !")
