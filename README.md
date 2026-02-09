# Consumer Insights Dashboard

## Présentation du projet

Application web interactive développée avec Streamlit permettant d'analyser et visualiser des données provenant de deux datasets :
- **Customer Shopping Behavior Dataset** : Analyse des comportements d'achat des clients
- **Airbnb Open Data** : Analyse des locations Airbnb

## Fonctionnalités

- Téléversement de fichiers CSV
- Stockage et interrogation des données avec DuckDB
- Visualisation de 4 KPIs par dataset
- Filtres dynamiques (date, région, catégorie, etc.)

## Installation

```bash
# Cloner le repository
git clone <url-du-repo>
cd consumer-insights-dashboard

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Exécution

```bash
streamlit run app/main.py
```

## Structure du projet

```
consumer-insights-dashboard/
├── app/
│   ├── main.py                    # Point d'entrée Streamlit
│   ├── components/                # Composants d'interface
│   ├── visualizations/            # Graphiques et KPIs
│   ├── database/                  # Connexion et requêtes DuckDB
│   └── utils/                     # Fonctions utilitaires
├── data/                          # Données CSV
└── tests/                         # Tests unitaires
```

## Répartition des tâches

| Membre | Responsabilités |
|--------|-----------------|
| Membre 1 | Upload CSV + Connexion DuckDB |
| Membre 2 | Requêtes SQL + Filtres dynamiques |
| Membre 3 | Visualisations Customer Shopping |
| Membre 4 | Visualisations Airbnb |

## Technologies utilisées

- Python 3.x
- Streamlit
- DuckDB
- Plotly / Altair
- Pandas
