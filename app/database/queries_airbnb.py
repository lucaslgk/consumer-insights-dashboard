
import pandas as pd
from app.database.connection import execute_query


def get_filter_options() -> dict:
    """
    Retourne les valeurs uniques pour les filtres
    """
    neighbourhoods = execute_query(
        'SELECT DISTINCT "neighbourhood group" FROM airbnb ORDER BY "neighbourhood group"'
    )
    room_types = execute_query(
        'SELECT DISTINCT "room type" FROM airbnb ORDER BY "room type"'
    )
    cancellation = execute_query(
        'SELECT DISTINCT cancellation_policy FROM airbnb WHERE cancellation_policy IS NOT NULL ORDER BY cancellation_policy'
    )

    return {
        'neighbourhoods': neighbourhoods['neighbourhood group'].tolist(),
        'room_types': room_types['room type'].tolist(),
        'cancellation_policies': cancellation['cancellation_policy'].tolist()
    }


def get_avg_price_by_neighbourhood(filters: dict = None) -> pd.DataFrame:
    """
    Prix moyen par quartier
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT 
            "neighbourhood group" as quartier,
            ROUND(AVG(price), 2) as prix_moyen
        FROM airbnb
        {where_clause}
        GROUP BY "neighbourhood group"
        ORDER BY prix_moyen DESC
    """
    return execute_query(query)


def get_room_type_distribution(filters: dict = None) -> pd.DataFrame:
    """
    Distribution des types de logement
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT 
            "room type" as type_logement,
            COUNT(*) as nb_logements
        FROM airbnb
        {where_clause}
        GROUP BY "room type"
        ORDER BY nb_logements DESC
    """
    return execute_query(query)


def get_avg_availability_by_neighbourhood(filters: dict = None) -> pd.DataFrame:
    """
    Disponibilité moyenne par quartier
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT 
            "neighbourhood group" as quartier,
            ROUND(AVG("availability 365"), 0) as disponibilite_moyenne
        FROM airbnb
        {where_clause}
        GROUP BY "neighbourhood group"
        ORDER BY disponibilite_moyenne DESC
    """
    return execute_query(query)


def get_avg_rating_by_room_type(filters: dict = None) -> pd.DataFrame:
    """
    Note moyenne par type de logement
    """
    where_clause = _build_where_clause(filters)
    query = f"""
        SELECT 
            "room type" as type_logement,
            ROUND(AVG("review rate number"), 2) as note_moyenne
        FROM airbnb
        {where_clause}
        GROUP BY "room type"
        ORDER BY note_moyenne DESC
    """
    return execute_query(query)


def _build_where_clause(filters: dict = None) -> str:
    """
    Construit la clause WHERE à partir des filtres.
    """
    if not filters:
        return ""

    conditions = []

    if filters.get('neighbourhood'):
        neighbourhoods = "', '".join(filters['neighbourhood'])
        conditions.append(f"\"neighbourhood group\" IN ('{neighbourhoods}')")

    if filters.get('room_type'):
        room_types = "', '".join(filters['room_type'])
        conditions.append(f"\"room type\" IN ('{room_types}')")

    if filters.get('cancellation_policy'):
        policies = "', '".join(filters['cancellation_policy'])
        conditions.append(f"cancellation_policy IN ('{policies}')")

    if filters.get('price_min') is not None:
        conditions.append(f"price >= {filters['price_min']}")

    if filters.get('price_max') is not None:
        conditions.append(f"price <= {filters['price_max']}")

    if conditions:
        return "WHERE " + " AND ".join(conditions)

    return ""
