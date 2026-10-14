from flask import Flask, render_template, request, redirect, url_for, session, flash
from src.database.repository import Repository
from src.models.objet import Objet

app = Flask(__name__)
app.secret_key = 'une_cle_tres_secrete_pour_dev_vision' 

# ==========================================
# ACCUEIL ET AFFICHAGE
# ==========================================

@app.route('/')
def index():
    objets = Repository.get_all_objets()
    return render_template('index.html', objets=objets)

# ==========================================
# GESTION DES OBJETS (CRUD)
# ==========================================

@app.route('/ajouter', methods=['POST'])
def ajouter():
    if 'user_id' not in session:
        return redirect(url_for('connexion'))

    nom = request.form.get('nom')
    description = request.form.get('description')
    prix_str = request.form.get('prix')

    if nom and prix_str:
        try:
            prix_val = float(prix_str)
            if prix_val < 0:
                return "Le prix ne peut pas être négatif !", 400 
            
            nouvel_objet = Objet(None, nom, description, prix_val)
            Repository.save_objet(nouvel_objet)
        except ValueError:
            return "Format de prix invalide", 400

    return redirect(url_for('index'))

@app.route('/modifier/<int:objet_id>', methods=['GET'])
def afficher_modification(objet_id):
    if 'user_id' not in session:
        return redirect(url_for('connexion'))

    objets = Repository.get_all_objets()
    objet = next((o for o in objets if o.id == objet_id), None)

    if objet:
        return render_template('modifier.html', objet=objet)
    
    return redirect(url_for('index'))

@app.route('/modifier/<int:objet_id>', methods=['POST'])
def modifier(objet_id):
    if 'user_id' not in session:
        return redirect(url_for('connexion'))

    nom = request.form.get('nom')
    description = request.form.get('description')
    prix_str = request.form.get('prix')

    if nom and prix_str:
        try:
            prix_val = float(prix_str)
            if prix_val < 0: return "Le prix ne peut pas être négatif !", 400
            
            objets = Repository.get_all_objets()
            objet = next((o for o in objets if o.id == objet_id), None)
            
            if objet:
                objet.nom = nom
                objet.description = description
                objet.prix_actuel = prix_val
                Repository.update_objet(objet)
        except ValueError:
            return "Erreur de format", 400

    return redirect(url_for('index'))

@app.route('/supprimer/<int:objet_id>', methods=['POST'])
def supprimer(objet_id):
    if 'user_id' not in session:
        return redirect(url_for('connexion'))
    
    Repository.delete_objet(objet_id)
    return redirect(url_for('index'))

# ==========================================
# AUTHENTIFICATION
# ==========================================

@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if Repository.create_utilisateur(nom, email, password):
            return redirect(url_for('connexion'))
        else:
            return "Email déjà utilisé ou erreur lors de l'inscription."
            
    return render_template('inscription.html')

@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Repository.verify_utilisateur(email, password)
        if user:
            session['user_id'] = user['id']
            session['user_nom'] = user['nom']
            session['user_solde'] = user['solde']
            return redirect(url_for('index'))
        else:
            return "Identifiants incorrects."
            
    return render_template('connexion.html')

@app.route('/deconnexion')
def deconnexion():
    session.clear()
    return redirect(url_for('index'))

# ==========================================
# ENCHÈRES (Logique B : Vérification Solde + Débit)
# ==========================================

@app.route('/encherir/<int:objet_id>', methods=['POST'])
def encherir(objet_id):
    if 'user_id' not in session:
        return redirect(url_for('connexion'))

    montant_str = request.form.get('montant')
    user_id = session['user_id']
    
    if montant_str:
        try:
            nouveau_montant = float(montant_str)
            
            # 1. On récupère l'objet pour vérifier le prix actuel
            objets = Repository.get_all_objets()
            objet_actuel = next((o for o in objets if o.id == objet_id), None)

            if objet_actuel:
                # 2. Vérification : Mise supérieure au prix actuel
                if nouveau_montant <= objet_actuel.prix_actuel:
                    return f"Mise insuffisante ! Le prix actuel est de {objet_actuel.prix_actuel}€.", 400

                # 3. Tentative de placement de l'enchère (Logique de débit dans le repository)
                reussite, message = Repository.placer_enchere(user_id, objet_id, nouveau_montant)
                
                if reussite:
                    # 4. MISE À JOUR DU SOLDE DANS LA SESSION
                    # On déduit le montant pour que l'affichage soit instantané
                    session['user_solde'] -= nouveau_montant
                    return redirect(url_for('index'))
                else:
                    return f"Erreur : {message}", 400

        except ValueError:
            return "Format de montant invalide", 400
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)