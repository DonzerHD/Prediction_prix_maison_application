# Prédiction de prix immobiliers
Ce projet vise à prédire les prix des maisons à partir de différentes variables telles que le nombre de chambres, de salles de bains, la superficie, etc. Le but est d'aider les acheteurs potentiels à estimer le prix d'une maison avant de l'acheter, ainsi que les vendeurs à estimer le prix de leur propriété avant de la mettre en vente.

Le projet utilise un ensemble de données provenant de King County, dans l'État de Washington, aux États-Unis. L'ensemble de données contient les informations sur les maisons vendues entre 2014 et 2015. Il contient des informations sur des maisons, chacune avec leurs caractéristiques.


# Données
Les données utilisées ont été obtenues à partir de [cette source](https://www.google.com/url?q=https://www.kaggle.com/datasets/harlfoxem/housesalesprediction/discussion&sa=D&source=docs&ust=1677335823102793&usg=AOvVaw3CZB_mSKOkhQ7p8MDTDq3K). Elles contiennent des informations sur les maisons vendues entre mai 2014 et mai 2015, telles que le nombre de chambres, de salles de bains, la surface habitable, le nombre d'étages, la condition de la maison, le nombre de vues, etc.

# Notebooks
Ce projet est basé sur plusieurs notebooks :

- data cleaning analyst : ce notebook contient l'analyse exploratoire des données et le nettoyage des données pour supprimer les valeurs manquantes, les données aberrantes et les doublons.
- data preparation : ce notebook contient la préparation des données pour le modèle de prédiction. Cela inclut la normalisation des variables, la séparation des données en ensembles de formation et de test, la création de variables indicatrices pour les variables catégorielles, etc.
- data modelisation : ce notebook contient la création et l'entraînement du modèle de prédiction. Différents algorithmes de régression sont comparés pour sélectionner le meilleur modèle.
- data model complet : Dans ce notebook, nous comparons les performances des deux modèles et choisissons le modèle qui donne les meilleurs résultats pour la prédiction des prix des maisons.

# Technologies utilisées
Le projet a été développé en utilisant les technologies suivantes :
- Python : pour le développement de l'application web et de l'analyse des données.
- Django : pour le développement de l'application web .
- Jupyter Notebook : pour l'analyse des données et la création des modèles de prédiction.
- Pandas : pour l'analyse des données.
- Numpy : pour l'analyse des données.
- Matplotlib : pour la visualisation des données.
- Seaborn : pour la visualisation des données.
- Scikit-learn : pour la création des modèles de prédiction.
- Pickle : pour la sauvegarde du modèle de prédiction.
- Folium : pour la création de la carte interactive dans le jupyter notebook.
- HTML / CSS / Javascript : pour le développement de l'application web.
- Leaflet : pour la création de la carte interactive.

# Utilisation
L'application web permet aux utilisateurs souhaitant acheter ou vendre une maison d'estimer son prix en saisissant les informations relatives à la propriété. De plus, la carte interactive leur permet de sélectionner l'emplacement de la maison en entrant les coordonnées de latitude et de longitude.

# Lancer le serveur de développement :
- Exécutez la commande suivante pour démarrer le serveur de développement : `python manage.py runserver`
- Assurez-vous que toutes les technologies utilisées sont installées et que vous êtes dans le dossier du projet.
- Accédez à l'application en entrant http://localhost:8000/ dans votre navigateur web.

# Auteurs
* **Thomas.l59** _alias_ [@DonzerHD](https://github.com/DonzerHD)

# Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
