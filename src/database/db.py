import sqlite3
import os

def initialiser_db():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'encheres.db')
    
    connexion = sqlite3.connect(db_path)
    curseur = connexion.cursor()

    curseur.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            solde REAL
        )
    ''')

  
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS objets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prix_initial REAL,
            prix_actuel REAL,
            etat TEXT
        )
    ''')

  
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS encheres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            utilisateur_id INTEGER,
            objet_id INTEGER,
            montant REAL,
            date TIMESTAMP,
            FOREIGN KEY(utilisateur_id) REFERENCES utilisateurs(id),
            FOREIGN KEY(objet_id) REFERENCES objets(id)
        )
    ''')
    
    connexion.commit()
    connexion.close()
print(f"Base de données créée à cet emplacement : {os.path.abspath(db_path)}")


if __name__ == "__main__":
    initialiser_db()
