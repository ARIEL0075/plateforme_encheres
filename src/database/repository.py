import sqlite3
import logging
from src.database.db import connect_db
from src.models.objet import Objet, Etat

class Repository:

    @staticmethod
    def save_objet(objet):
        try:
            with connect_db() as conn:
                cursor = conn.cursor()

                etat_value = objet.etat.value if objet.etat else None

                cursor.execute("""
                    INSERT INTO objets (id, nom, description, prix_actuel, etat)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        nom=excluded.nom,
                        description=excluded.description,
                        prix_actuel=excluded.prix_actuel,
                        etat=excluded.etat
                """, (objet.id, objet.nom, objet.description, objet.prix_actuel, etat_value))

        except sqlite3.Error as e:
            logging.error(f"Erreur sauvegarde objet : {e}")
    @staticmethod
    def update_objet(objet):
        try:
         with connect_db() as conn:
            cursor = conn.cursor()

            etat_value = objet.etat.value if objet.etat else None

            cursor.execute("""
                UPDATE objets
                SET nom = ?,
                    description = ?,
                    prix_actuel = ?,
                    etat = ?
                WHERE id = ?
            """, (
                objet.nom,
                objet.description,
                objet.prix_actuel,
                etat_value,
                objet.id
            ))

        except sqlite3.Error as e:
            logging.error(f"Erreur modification objet : {e}")       

    @staticmethod
    def delete_objet(objet_id):
        try:
         with connect_db() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM objets
                WHERE id = ?
            """, (objet_id,))

        except sqlite3.Error as e:
            logging.error(f"Erreur suppression objet : {e}")       


    @staticmethod
    def get_all_objets():
        try:
            with connect_db() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM objets")

                rows = cursor.fetchall()

                return [
                    Objet(
                        id_objet=row['id'],
                        nom=row['nom'],
                        description=row['description'],
                        prix_depart=row['prix_actuel'],  # à améliorer plus tard
                        prix_actuel=row['prix_actuel'],
                        etat=Etat(row['etat']) if row['etat'] else None
                    )
                    for row in rows
                ]

        except sqlite3.Error as e:
            logging.error(f"Erreur récupération : {e}")
            return []