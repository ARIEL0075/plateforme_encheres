  Plateforme d'Enchères en Ligne (Projet Flask)

Plateforme web de simulation d'enchères en ligne développée avec Python et Flask.



##  Équipe & Répartition
- *HOUETO Ariel :* Logique métier, persistance SQLite, gestion des exceptions.
- *APLOGAN Epiphanio :* Interface Web Flask, tests unitaires Pytest, documentation.

##  Fonctionnalités principales
- Gestion des utilisateurs et crédits virtuels
- Création et gestion d'objets aux enchères
- Prise d'enchères en temps réel avec validation des règles métier
- Détermination automatique du gagnant

##  Stack Technique
- *Backend :* Python 3.x, Flask
- *Base de données :* SQLite
- *Tests :* Pytest

## 🔧 Installation & Lancement en Local

1. *Cloner le dépôt :*
   ```bash
   git clone https://github.com/ARIEL0075/plateforme_encheres.git
   cd plateforme_encheres

2. Créer et activer l'environnement virtuel :
python -m venv venv
# Sur Windows (PowerShell) :
.\venv\Scripts\activate

3. Installer les dépendances :
pip install -r requirements.txt

4. Lancer le serveur Flask :
flask --app src.app run