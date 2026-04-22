import sqlite3

# Nom du fichier base de données
DB_NAME = "plateforme_encheres.db"

def connect_db():
    """Crée une connexion à la base de données."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    """Initialise les tables de la base de données."""
    conn = connect_db()
    cursor = conn.cursor()
    
    # Création de la table Utilisateurs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            solde REAL NOT NULL
        )
    ''')
    
    # Création de la table Objets
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS objets (
            id INTEGER PRIMARY KEY,
            nom TEXT NOT NULL,
            description TEXT,
            prix_actuel REAL NOT NULL,
            etat TEXT NOT NULl
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Base de données initialisée avec succès.")

if __name__ == "__main__":
    init_db()
