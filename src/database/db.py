import sqlite3

DB_NAME = "plateforme_encheres.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    # 1. Table Utilisateurs 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mot_de_passe TEXT NOT NULL,
            solde REAL NOT NULL DEFAULT 0.0
        )
    ''')
    
    # 2. Table Objets 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS objets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            description TEXT,
            prix_actuel REAL NOT NULL,
            etat TEXT NOT NULL,
            vendeur_id INTEGER,
            dernier_encherisseur_id INTEGER,     
            FOREIGN KEY (vendeur_id) REFERENCES utilisateurs(id)
        )
    ''')

    # 3. Table Enchères (Pour l'historique des mises)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS encheres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_utilisateur INTEGER NOT NULL,
            id_objet INTEGER NOT NULL,
            montant REAL NOT NULL,
            date_enchere DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id),
            FOREIGN KEY (id_objet) REFERENCES objets(id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Base de données mise à jour avec succès.")

if __name__ == "__main__":
    init_db()