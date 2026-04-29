from src.database.db import connect_db
class Repository:
    
    @staticmethod
    def save_objet(objet):
        conn = None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR REPLACE INTO objets (id, nom, description, prix_actuel, etat) VALUES (?, ?, ?, ?, ?)",
                (objet.id, objet.nom, objet.description, objet.prix_actuel, objet.etat)
            )
            conn.commit()
            print(f"Objet '{objet.nom}' mis à jour ou créé en base.")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erreur lors de la sauvegarde de l'objet : {e}")
        finally:
            if conn:
                conn.close()

    @staticmethod
    def save_utilisateur(utilisateur):
        conn = None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR REPLACE INTO utilisateurs (id, nom, solde) VALUES (?, ?, ?)",
                (utilisateur.id, utilisateur.nom, utilisateur.solde)
            )
            conn.commit()
            print(f"Utilisateur '{utilisateur.nom}' mis à jour ou créé en base.")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erreur lors de la sauvegarde de l'utilisateur : {e}")
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update_objet(objet):
        conn = None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE objets SET prix_actuel = ?, etat = ? WHERE id = ?",
                (objet.prix_actuel, objet.etat, objet.id)
            )
            conn.commit()
            print(f"Objet '{objet.nom}' mis à jour en base.")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erreur lors de la mise à jour de l'objet : {e}")
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete_objet(objet_id):
        conn = None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM objets WHERE id = ?", (objet_id,))
            conn.commit()
            print(f"Objet avec ID {objet_id} supprimé.")
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Erreur lors de la suppression de l'objet : {e}")
        finally:
            if conn:
                conn.close()
