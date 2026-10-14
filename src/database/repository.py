import sqlite3
import logging
from werkzeug.security import generate_password_hash, check_password_hash
from src.database.db import connect_db
from src.models.objet import Objet, Etat

class Repository:

    # ==========================================
    # GESTION DES UTILISATEURS
    # ==========================================

    @staticmethod
    def create_utilisateur(nom, email, mot_de_passe):
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                hash_pw = generate_password_hash(mot_de_passe)
                cursor.execute("""
                   INSERT INTO utilisateurs(nom, email, mot_de_passe, solde)  VALUES (?,?,?,?)          

                """ , (nom,email,hash_pw,10000.0))
                conn.commit()
                return True
        except sqlite3.Error as e:
            logging.error("Erreur trouvé :", {e})    
            return False
    @staticmethod
    def verify_utilisateur(email, password):
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE email = ?", (email,))
                user = cursor.fetchone()
                if user and check_password_hash(user['mot_de_passe'], password):
                    return user
                return None
        except sqlite3.Error as e:
            logging.error(f"Erreur vérification : {e}")
            return None

    # ==========================================
    # GESTION DES OBJETS
    # ==========================================

    @staticmethod
    def save_objet(objet):
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                etat_val = objet.etat.value if hasattr(objet.etat, 'value') else "EN_COURS"
                if objet.id is None:
                    cursor.execute("INSERT INTO objets (nom, description, prix_actuel, etat) VALUES (?, ?, ?, ?)",
                                 (objet.nom, objet.description, objet.prix_actuel, etat_val))
                else:
                    cursor.execute("""
                        INSERT INTO objets (id, nom, description, prix_actuel, etat)
                        VALUES (?, ?, ?, ?, ?)
                        ON CONFLICT(id) DO UPDATE SET nom=excluded.nom, prix_actuel=excluded.prix_actuel
                    """, (objet.id, objet.nom, objet.description, objet.prix_actuel, etat_val))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Erreur sauvegarde : {e}")

    @staticmethod
    def get_all_objets():
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                query = """
                    SELECT o.*, u.nom as nom_gagnant 
                    FROM objets o
                    LEFT JOIN utilisateurs u ON o.dernier_encherisseur_id = u.id
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                liste = []
                for row in rows:
                    obj = Objet(row['id'], row['nom'], row['description'], row['prix_actuel'])
                    obj.nom_gagnant = row['nom_gagnant'] if row['nom_gagnant'] else "Aucune mise"
                    liste.append(obj)
                return liste
        except sqlite3.Error as e:
            logging.error(f"Erreur listage : {e}")
            return []

    # ==========================================
    # LOGIQUE DES ENCHÈRES (AVEC REMBOURSEMENT)
    # ==========================================

    @staticmethod
    def placer_enchere(id_utilisateur, id_objet, montant):
        """Débite le nouveau, rembourse l'ancien et met à jour l'objet."""
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                
                # 1. Vérifier le solde du nouvel enchérisseur
                cursor.execute("SELECT solde FROM utilisateurs WHERE id = ?", (id_utilisateur,))
                user = cursor.fetchone()
                if not user or user['solde'] < montant:
                    return False, "Solde insuffisant"

                # 2. Récupérer l'ancien enchérisseur et son montant pour le rembourser
                cursor.execute("SELECT dernier_encherisseur_id, prix_actuel FROM objets WHERE id = ?", (id_objet,))
                objet_info = cursor.fetchone()
                
                ancien_id = objet_info['dernier_encherisseur_id']
                ancien_prix = objet_info['prix_actuel']

                # 3. Remboursement de l'ancien (si ce n'est pas la première mise)
                if ancien_id and ancien_id != id_utilisateur:
                    cursor.execute("UPDATE utilisateurs SET solde = solde + ? WHERE id = ?", (ancien_prix, ancien_id))

                # 4. Débiter le nouveau
                cursor.execute("UPDATE utilisateurs SET solde = solde - ? WHERE id = ?", (montant, id_utilisateur))

                # 5. Mettre à jour l'objet
                cursor.execute("""
                    UPDATE objets SET prix_actuel = ?, dernier_encherisseur_id = ? WHERE id = ?
                """, (montant, id_utilisateur, id_objet))

                conn.commit()
                return True, "Succès"
        except sqlite3.Error as e:
            logging.error(f"Erreur SQL : {e}")
            return False, "Erreur technique"

    @staticmethod
    def update_objet(objet):
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                etat_val = objet.etat.value if hasattr(objet.etat, 'value') else "EN_COURS"
                cursor.execute("UPDATE objets SET nom=?, description=?, prix_actuel=?, etat=? WHERE id=?",
                             (objet.nom, objet.description, objet.prix_actuel, etat_val, objet.id))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Erreur update : {e}")

    @staticmethod
    def delete_objet(objet_id):
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM objets WHERE id = ?", (objet_id,))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Erreur suppression : {e}")