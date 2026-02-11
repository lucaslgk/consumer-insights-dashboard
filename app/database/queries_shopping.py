"""
Requêtes SQL pour Customer Shopping Behavior
KPIs: Ventes par catégorie, Genre/Saison, Panier moyen par âge, Méthodes de paiement
"""
import pandas as pd
from app.database.connection import execute_query


def get_sales_by_category(filters: dict = None) -> pd.DataFrame:
    """
    Total des ventes par catégorie de produit
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT
            Category as categorie,
            SUM("Purchase Amount (USD)") as total_ventes,
            COUNT(*) as nb_transactions
        FROM shopping
        {where_clause}
        GROUP BY Category
        ORDER BY total_ventes DESC
    """
    return execute_query(query)


def get_sales_by_gender_season(filters: dict = None) -> pd.DataFrame:
    """
    Ventes par genre et par saison
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT
            Gender as genre,
            Season as saison,
            SUM("Purchase Amount (USD)") as total_ventes,
            COUNT(*) as nb_transactions
        FROM shopping
        {where_clause}
        GROUP BY Gender, Season
        ORDER BY genre, saison
    """
    return execute_query(query)


def get_avg_basket_by_age(filters: dict = None) -> pd.DataFrame:
    """
    Panier moyen par tranche d'âge
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT
            CASE
                WHEN Age < 25 THEN '18-24'
                WHEN Age < 35 THEN '25-34'
                WHEN Age < 45 THEN '35-44'
                WHEN Age < 55 THEN '45-54'
                ELSE '55+'
            END as tranche_age,
            ROUND(AVG("Purchase Amount (USD)"), 2) as panier_moyen,
            COUNT(*) as nb_clients
        FROM shopping
        {where_clause}
        GROUP BY tranche_age
        ORDER BY tranche_age
    """
    return execute_query(query)


def get_payment_methods(filters: dict = None) -> pd.DataFrame:
    """
    Répartition des méthodes de paiement
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT
            "Payment Method" as methode_paiement,
            COUNT(*) as nb_transactions,
            ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as pourcentage
        FROM shopping
        {where_clause}
        GROUP BY "Payment Method"
        ORDER BY nb_transactions DESC
    """
    return execute_query(query)


def get_filter_options() -> dict:
    """
    Retourne les valeurs uniques pour les filtres
    """
    locations = execute_query("SELECT DISTINCT Location FROM shopping ORDER BY Location")
    categories = execute_query("SELECT DISTINCT Category FROM shopping ORDER BY Category")
    seasons = execute_query("SELECT DISTINCT Season FROM shopping ORDER BY Season")
    genders = execute_query("SELECT DISTINCT Gender FROM shopping ORDER BY Gender")

    return {
        'locations': locations['Location'].tolist(),
        'categories': categories['Category'].tolist(),
        'seasons': seasons['Season'].tolist(),
        'genders': genders['Gender'].tolist()
    }


def _build_where_clause(filters: dict = None) -> str:
    """
    Construit la clause WHERE à partir des filtres
    """
    if not filters:
        return ""

    conditions = []

    if filters.get('location'):
        locations = "', '".join(filters['location'])
        conditions.append(f"Location IN ('{locations}')")

    if filters.get('category'):
        categories = "', '".join(filters['category'])
        conditions.append(f"Category IN ('{categories}')")

    if filters.get('season'):
        seasons = "', '".join(filters['season'])
        conditions.append(f"Season IN ('{seasons}')")

    if filters.get('gender'):
        genders = "', '".join(filters['gender'])
        conditions.append(f"Gender IN ('{genders}')")

    if conditions:
        return "WHERE " + " AND ".join(conditions)

    return ""
