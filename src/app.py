from flask import Flask, render_template, request, redirect, url_for
from src.database.repository import Repository
from src.models.objet import Objet # Importation de ton modèle
import random

app = Flask(__name__)

@app.route('/')
def index():
    # On récupère les objets depuis la base grâce à ta méthode
    objets = Repository.get_all_objets()
    return render_template('index.html', objets=objets)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    # 1. On récupère les données envoyées par le formulaire HTML
    nom = request.form.get('nom')
    description = request.form.get('description')
    prix = request.form.get('prix')

    if nom and prix:
        # 2. On crée un nouvel objet (on génère un ID )
        nouvel_id = random.randint(1000, 9999)
        nouvel_objet = Objet(id_objet=nouvel_id, nom=nom, description=description, prix_depart=float(prix))
        
        # 3. On utilise ton Repository pour l'enregistrer dans la base .db
        Repository.save_objet(nouvel_objet)

    # 4. On redirige vers l'accueil pour voir la liste mise à jour
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
