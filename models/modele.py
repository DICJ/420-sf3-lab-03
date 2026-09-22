import pandas as pd
import pickle
import os
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg") # Permet d'utiliser matplotlib sans interface graphique

def exemple_de_fonction_testee(a, b):
    """
    Fonction de test pour vérifier le fonctionnement de l'application
    Elle retourne la somme de deux nombres
    """
    return a + b
    
def diagramme_a_moustache(column, df):
    """
    Création d'un diagramme à boîte de moustache pour la colonne demandée
    Si le DataFrame contient plus de 10 000 lignes, un échantillon aléatoire de 10 000 lignes est utilisé
    Le graphique est sauvegardé dans le dossier static/images/plots
    """
    if len(df) > 10000:
        df = df.sample(10000)
    fig, axes = plt.subplots()
    axes.boxplot([df[column]], tick_labels=[column])
    axes.set_xlabel("Variables")
    axes.set_ylabel(column)
    axes.set_title("Diagramme à boîte de moustache")
    plt.savefig(f'static/images/plots/exemple_boxplot.png')
    plt.close(fig)


def diagramme_a_barres(column, df):
    """    
    Création d'un diagramme à barres pour la colonne demandée
    Le graphique est sauvegardé dans le dossier static/images/plots
    """
    fig, axes = plt.subplots()
    df[column].value_counts().plot(kind='bar', ax=axes)
    axes.set_xlabel(column)
    axes.set_ylabel("Fréquence")
    axes.set_title("Diagramme à barre")
    plt.savefig(f'static/images/plots/exemple_barplot.png')
    plt.close(fig)


def obtenir_diagrammes():
    """
    Obtention des diagrammes à partir du fichier CSV
    """
    filename = "atomes.csv"
    try:
        df = pd.read_csv('datasets/' + filename) 
        message = "Le fichier spécifié est introuvable"

        diagramme_a_moustache("NumberofShells", df)
        diagramme_a_barres("Type", df)

        return "Diagrammes créés avec succès"
    except FileNotFoundError as e:
        return "Fichier introuvable"