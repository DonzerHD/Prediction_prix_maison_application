import csv
from django.shortcuts import render
from .forms import PredictionForm
import joblib
import os
import pandas as pd

"""Définir le chemin vers le fichier pkl"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_FILEPATH = os.path.join(BASE_DIR, 'app/ia', 'ia.pkl')

# Create your views here.
def index(request):
    """Page d'accueil"""
    with open('app/ia/data/kc_house_data_clean_knn.csv') as file:
        """Afficher les 30 premières lignes du dataset"""
        reader = csv.reader(file)
        rows = [row for i, row in enumerate(reader) if i < 30] # Seulement les 30 premières lignes
    form = PredictionForm(request.POST or None)
    result = 0

    if form.is_valid():
        """Prédire le prix de vente"""
        # Charger le modèle pré-entraîné
        data = form.cleaned_data
        """Transformer les données en dataframe"""
        df = pd.DataFrame(data, index=[0])
        """Model prediction"""
        model = joblib.load(MODEL_FILEPATH)
        result = model.predict(df)[0].round(2)
    else:
        print('Form is not valid')
    context = {
        'form': form,
        'result': result,
        'rows': rows
    }
    return render(request, 'index.html', context)

