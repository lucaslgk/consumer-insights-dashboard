"""
Fonctions de nettoyage et transformation des données
pour les datasets Customer Shopping et Airbnb
"""
import pandas as pd


def preprocess_airbnb(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et transforme le dataset Airbnb Open Data.

    Étapes:
    - Suppression des doublons
    - Suppression des colonnes inutiles (license, house_rules)
    - Suppression des lignes sans price ou neighbourhood group
    - Remplacement des NaN dans reviews per month par 0
    - Conversion de price et service fee en float

    Args:
        df: DataFrame brut du CSV Airbnb

    Returns:
        DataFrame nettoyé
    """
    df = df.copy()

    # Suppression des doublons
    df = df.drop_duplicates(ignore_index=True)

    # Suppression des colonnes inutiles
    columns_to_drop = ['license', 'house_rules']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Suppression des lignes sans price ou neighbourhood group
    df = df.dropna(subset=['price', 'neighbourhood group'])

    # Remplacement des NaN dans reviews per month par 0
    if 'reviews per month' in df.columns:
        df['reviews per month'] = df['reviews per month'].fillna(0)

    # Conversion de price et service fee en float (suppression $ et ,)
    if 'price' in df.columns:
        df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

    if 'service fee' in df.columns:
        df['service fee'] = df['service fee'].replace(r'[\$,]', '', regex=True).astype(float)

    return df


def preprocess_shopping(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie et transforme le dataset Customer Shopping Behavior.

    Le dataset est déjà propre (0 doublons, 0 NaN), cette fonction
    effectue uniquement des vérifications et retourne le DataFrame.

    Args:
        df: DataFrame brut du CSV Shopping

    Returns:
        DataFrame nettoyé
    """
    df = df.copy()

    # Suppression des doublons (par précaution)
    df = df.drop_duplicates(ignore_index=True)

    return df


def detect_dataset_type(df: pd.DataFrame) -> str:
    """
    Détecte automatiquement le type de dataset (airbnb ou shopping)
    en fonction des colonnes présentes.

    Args:
        df: DataFrame à analyser

    Returns:
        'airbnb', 'shopping' ou 'unknown'
    """
    columns = set(df.columns.str.lower())

    # Colonnes spécifiques à Airbnb
    airbnb_markers = {'neighbourhood group', 'room type', 'host id', 'availability 365'}

    # Colonnes spécifiques à Shopping
    shopping_markers = {'customer id', 'purchase amount (usd)', 'item purchased', 'category'}

    if airbnb_markers.intersection(columns):
        return 'airbnb'
    elif shopping_markers.intersection(columns):
        return 'shopping'

    return 'unknown'


def preprocess_auto(df: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    """
    Détecte automatiquement le type de dataset et applique
    le preprocessing approprié.

    Args:
        df: DataFrame brut

    Returns:
        Tuple (DataFrame nettoyé, type de dataset)
    """
    dataset_type = detect_dataset_type(df)

    if dataset_type == 'airbnb':
        return preprocess_airbnb(df), dataset_type
    elif dataset_type == 'shopping':
        return preprocess_shopping(df), dataset_type
    else:
        return df, dataset_type
