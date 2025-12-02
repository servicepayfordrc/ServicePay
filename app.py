# Backend Flask minimal pour servir le site vitrine ServicePay.
from flask import Flask, render_template

# Initialisation de l'application Flask
app = Flask(__name__)

# Définition de la route principale ('/')
@app.route('/')
def home():
    # La fonction render_template cherchera 'index.html' dans un dossier 'templates' par défaut.
    # Pour cet environnement, nous supposons qu'elle sert simplement le fichier index.html.
    return render_template('index.html')

# Point d'entrée pour lancer le serveur
if __name__ == '__main__':
    # Le mode debug permet un rechargement automatique lors des changements de code.
    app.run(debug=True)
