from src.database.db import connect_db

class Repository:
    @staticmethod
    def save_objet(objet):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO objets (id, nom, description, prix_actuel, etat) VALUES (?, ?, ?, ?, ?)",
            (objet.id, objet.nom, objet.description, objet.prix_actuel, objet.etat.value)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def save_utilisateur(utilisateur):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO utilisateurs (id, nom, solde) VALUES (?, ?, ?)",
            (utilisateur.id, utilisateur.nom, utilisateur.solde)
        )
        conn.commit()
        conn.close()
