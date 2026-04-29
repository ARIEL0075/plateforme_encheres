from flask import Flask, render_template
from src.database.repository import Repository

app = Flask(__name__)

@app.route('/')
def index():
    # On récupère les objets depuis la base grâce à ta nouvelle méthode
    objets = Repository.get_all_objets()
    return render_template('index.html', objets=objets)

if __name__ == '__main__':
    app.run(debug=True)
