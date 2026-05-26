from flask import Flask, render_template, request, redirect, url_for
from src.database.repository import Repository
from src.models.objet import Objet
import random

app = Flask(__name__)


# =======================
# PAGE ACCUEIL (LISTE)
# =======================
@app.route('/')
def index():
    objets = Repository.get_all_objets()
    return render_template('index.html', objets=objets)


# =======================
# AJOUTER OBJET
# =======================
@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form.get('nom')
    description = request.form.get('description')
    prix = request.form.get('prix')

    if nom and prix:
        nouvel_id = random.randint(1000, 9999)

        nouvel_objet = Objet(
            id_objet=nouvel_id,
            nom=nom,
            description=description,
            prix_depart=float(prix)
        )

        Repository.save_objet(nouvel_objet)

    return redirect(url_for('index'))


# =======================
# SUPPRIMER OBJET
# =======================
@app.route('/supprimer/<int:objet_id>', methods=['POST'])
def supprimer(objet_id):
    print("ID SUPPRESSION :", objet_id)  # test
    Repository.delete_objet(objet_id)
    return redirect(url_for('index'))
# =======================
# AFFICHER FORM MODIFICATION
# =======================
@app.route('/modifier/<int:objet_id>', methods=['GET'])
def afficher_modification(objet_id):
    objets = Repository.get_all_objets()
    objet = next((o for o in objets if o.id == objet_id), None)

    if objet:
        return render_template('modifier.html', objet=objet)

    return redirect(url_for('index'))


# =======================
# ENREGISTRER MODIFICATION
# =======================
@app.route('/modifier/<int:objet_id>', methods=['POST'])
def modifier(objet_id):
    nom = request.form.get('nom')
    description = request.form.get('description')
    prix = request.form.get('prix')

    objets = Repository.get_all_objets()
    objet = next((o for o in objets if o.id == objet_id), None)

    if objet:
        objet.nom = nom
        objet.description = description
        objet.prix_actuel = float(prix)

        Repository.update_objet(objet)

    return redirect(url_for('index'))


# =======================
# RUN APP
# =======================
if __name__ == '__main__':
    app.run(debug=True)