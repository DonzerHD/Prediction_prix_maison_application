from django import forms
import pandas as pd

"""Charger le dataset"""
df = pd.read_csv('app/ia/data/kc_house_data_clean_knn.csv')

class PredictionForm(forms.Form):
    """Formulaire de prédiction"""
    # Définir les champs du formulaire pour les variables numériques
    bedrooms = forms.IntegerField(label='Bedrooms' , widget=forms.TextInput(attrs={'class' : 'form-input'}))
    bathrooms = forms.FloatField(label='Bathrooms' , widget=forms.TextInput(attrs={'class' : 'form-input'}))
    surface = forms.IntegerField(label='Surface' , widget=forms.TextInput(attrs={'class' : 'form-input'}))
    floors = forms.FloatField(label='Floors' , widget=forms.TextInput(attrs={'class' : 'form-input'}))
    waterfront = forms.BooleanField(required=False, label='Vue sur la mer'  , widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}))

        
    GRADE_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        # Ajouter toutes les options de 'grade'
    ]
    grade = forms.TypedChoiceField(coerce=int , label='Grade', choices=GRADE_CHOICES , widget=forms.Select(attrs={'class' : 'form-select'}))
    
    # Définir les champs du formulaire pour les variables catégorielles
    zipcodes = sorted(df['zipcode'].unique())
    ZIPCODE_CHOICES = [(zip, zip) for zip in zipcodes]
    zipcode = forms.TypedChoiceField(coerce=int ,label='Zipcode', choices=ZIPCODE_CHOICES , widget=forms.Select(attrs={'class' : 'form-select'}))
    
    CONDITION_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        # Ajouter toutes les options de 'condition'
    ]
    condition = forms.TypedChoiceField(coerce=int ,label='Condition', choices=CONDITION_CHOICES , widget=forms.Select(attrs={'class' : 'form-select'}))
    
    VIEW_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        # Ajouter toutes les options de 'view'
    ]
    view = forms.TypedChoiceField(coerce=int , label='View', choices=VIEW_CHOICES , widget=forms.Select(attrs={'class' : 'form-select'}))
    
    """Formulaire de localisation"""
    lat = forms.FloatField(label='Latitude', widget=forms.TextInput(attrs={'id': 'id_lat', 'readonly': 'readonly' ,'class' : 'form-input'}))
    long = forms.FloatField(label='Longitude', widget=forms.TextInput(attrs={'id': 'id_long', 'readonly': 'readonly' , 'class' : 'form-input'}))
