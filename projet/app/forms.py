from django import forms
import pandas as pd

df = pd.read_csv('app/ia/data/kc_house_data_clean_knn.csv')

class PredictionForm(forms.Form):
    # Définir les champs du formulaire pour les variables numériques
    bedrooms = forms.IntegerField(label='Bedrooms')
    bathrooms = forms.FloatField(label='Bathrooms')
    surface = forms.IntegerField(label='Surface')
    floors = forms.FloatField(label='Floors')
    waterfront = forms.BooleanField(required=False, label='Vue sur la mer')
    lat = forms.FloatField(label='Latitude')
    long = forms.FloatField(label='Longitude')
        
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
    grade = forms.TypedChoiceField(coerce=int , label='Grade', choices=GRADE_CHOICES)
    
    # Définir les champs du formulaire pour les variables catégorielles
    zipcodes = sorted(df['zipcode'].unique())
    ZIPCODE_CHOICES = [(zip, zip) for zip in zipcodes]
    zipcode = forms.TypedChoiceField(coerce=int ,label='Zipcode', choices=ZIPCODE_CHOICES)
    
    CONDITION_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        # Ajouter toutes les options de 'condition'
    ]
    condition = forms.TypedChoiceField(coerce=int ,label='Condition', choices=CONDITION_CHOICES)
    
    VIEW_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        # Ajouter toutes les options de 'view'
    ]
    view = forms.TypedChoiceField(coerce=int , label='View', choices=VIEW_CHOICES)
   
        