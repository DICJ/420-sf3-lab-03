from flask import Flask, render_template, request, redirect, make_response, session
import uuid
from models import modele
import os

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete' # Servira aux sessions cookies signés

@app.route('/')
def index():
    """
    Route principale de l'application
    Elle retourne deux diagrammes
    """
    message = modele.obtenir_diagrammes()
    return render_template('accueil.html', message=message)


