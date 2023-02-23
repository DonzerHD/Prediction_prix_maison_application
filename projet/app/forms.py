from django import forms

class PredictionForm(forms.Form):
    bedrooms = forms.IntegerField(label='Nombre de chambres')
    bathrooms = forms.FloatField(label='Nombre de salles de bain')
    surface = forms.FloatField(label='Surface')
    floors = forms.IntegerField(label='Nombre d\'étages')
    waterfront = forms.BooleanField(required=False, label='Vue sur la mer')
    view = forms.ChoiceField(choices=[('0', 'Aucune'), ('1', 'Faible'), ('2', 'Moyenne'), ('3', 'Bonne'), ('4', 'Très bonne')], label='Qualité de la vue')
    condition = forms.ChoiceField(choices=[('1', 'Mauvaise'), ('2', 'Moyenne'), ('3', 'Bonne'), ('4', 'Très bonne'), ('5', 'Excellente')], label='État de la maison')
    grade = forms.ChoiceField(choices=[('1', 'Faible'), ('2', 'Moyen'), ('3', 'Moyen+'), ('4', 'Bon'), ('5', 'Bon+'), ('6', 'Très bon'), ('7', 'Très bon+'), ('8', 'Excellent'), ('9', 'Excellent+'), ('10', 'Fantastique'), ('11', 'Fantastique+'), ('12', 'Paradisiaque')], label='Note de qualité générale de la maison')
    price_per_sqft = forms.FloatField(label='Prix du pied carré')