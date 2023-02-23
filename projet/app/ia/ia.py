from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsRegressor
from joblib import dump
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, 'ia/data', 'kc_house_data_clean_knn.csv'))

y = df['price']
X = df.drop(['price' , 'zipcode'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.21, random_state=42)

# On cree un pipeline de proprocessing pour les variables numériques
numeric_features = X.columns # on récupère les noms des variables numériques
numeric_transformer = Pipeline([
('imputer', SimpleImputer(strategy='mean')), # imputation des valeurs manquantes
])


# on déclare à quelles variables on applique quel transformer
preprocessor = ColumnTransformer(
transformers=[
('num', numeric_transformer, numeric_features),
]
)


# On obtient un pipeline de preprocessing qu'on peut utiliser dans un pipeline d'entainement
knn_4 = KNeighborsRegressor(n_neighbors=3 , weights='distance' , p=1)
pipe = Pipeline([
('prep', preprocessor),
('knn', knn_4)
])

# Entrainement sur X_train
trained_pipe = pipe.fit(X_train,y_train)

# scoring sur X_test
score = trained_pipe.score(X_test,y_test)
print(f'Score du modèle : {score}')

# Prédiction sur X_test
predict_lr_X = trained_pipe.predict(X_test)

# sauvegarde du pipeline entraîné en tant que fichier pkl
dump(trained_pipe, os.path.join(BASE_DIR, 'ia', 'ia.pkl'))