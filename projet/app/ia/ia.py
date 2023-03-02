import os
import pandas as pd
from joblib import dump
from django.conf import settings
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

"""Charger le dataset"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, 'ia/data', 'kc_house_data_clean_knn.csv'))

# Création de la variable cible
y = df['price']
X = df.drop(['price'], axis=1)

# Division en jeux de données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# On cree un pipeline de preprocessing pour les variables numériques
numeric_features = ['bedrooms', 'bathrooms', 'surface', 'floors', 'waterfront', 'lat', 'long']
numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),  # imputation des valeurs manquantes
    ('scaler', MinMaxScaler()),  # normalisation des données
])

# On cree un pre-processeur pour les variables catégorielles
categorial_features = ["zipcode" , "grade" , "condition" , 'view']
categorical_transformer = OneHotEncoder(sparse=False , handle_unknown='ignore')

# On crée un préprocesseur global pour les deux types de variables
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorial_features)
    ]
)

# On obtient un pipeline complet avec un modèle de KNN
knn_4 = KNeighborsRegressor(n_neighbors=5, weights='distance', p=1)
pipe = Pipeline([
    ('prep', preprocessor),
    ('knn', knn_4)
])

# Entrainement sur X_train
trained_pipe = pipe.fit(X_train, y_train)

# Faire des prédictions sur le jeu de test0
y_pred = trained_pipe.predict(X_test)

# Calculer les métriques d'évaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

"""Afficher les résultats"""
print(f'MAE : {mae}')
print(f'R2 : {r2}')
print(X_test.head(2))

# sauvegarde du pipeline entraîné en tant que fichier pkl
dump(trained_pipe, os.path.join(BASE_DIR, 'ia', 'ia.pkl'))