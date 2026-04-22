class Utilisateur:
    def __init__(self, id_utilisateur, nom, solde=0.0):
        self.id = id_utilisateur
        self.nom = nom
        self.solde = solde

    def crediter(self, montant):
     if montant > 0:
      self.solde += montant

    
