# Consumer Insights Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=black) ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)

> **Projet MBA Big Data & IA - Environnement de développement 2025-2026**  
> Dashboard interactif d'aide à la décision

---

## Table des matières
1. [Description](#description)
2. [Technologies](#technologies)
3. [Fonctionnalités principales](#fonctionnalités-principales)
4. [Installation](#installation)
5. [Utilisation](#utilisation)
6. [Structure du projet](#structure-du-projet)
7. [Membres du projet](#membres-du-projet)

## Description
Ce projet est une application web interactive développée avec Streamlit et DuckDB. Elle permet d'analyser deux types de données : le comportement d'achat des consommateurs et les locations Airbnb. L'objectif est de fournir une interface simple pour importer des données CSV, les stocker dans une base de données performante et visualiser des indicateurs clés.

## Technologies
Le projet utilise les technologies suivantes :
* **Python** : Langage de programmation principal.
* **Streamlit** : Framework pour la création de l'interface web.
* **DuckDB** : Base de données SQL analytique embarquée.
* **Pandas** : Manipulation et traitement des données.
* **Plotly** : Création des graphiques interactifs.

## Fonctionnalités principales
- Import de fichiers CSV avec détection automatique du format.
- Stockage et requêtage optimisé des données via DuckDB.
- Tableaux de bord interactifs pour visualiser les tendances.
- Filtrage dynamique des résultats (par catégorie, région, prix, etc.).

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/lucaslgk/consumer-insights-dashboard.git
   ```

2. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Pour lancer l'application, exécutez la commande suivante depuis la racine du projet :

```bash
streamlit run app/main.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut.

## Structure du projet

* **app/** : Contient le code source (main.py, composants, base de données).
* **data/** : Dossier destiné aux fichiers sources CSV.
* **tests/** : Tests unitaires du projet.

## Membres du projet
* **Camille THAUVIN** : Gestion de l'upload, connexion DuckDB, création de la sidebar.
* **Ines TAIBI** : Implémentation des requêtes SQL et filtres.
* **Lucas GOUMARD** : Preprocessing des données et création du dashboard.

