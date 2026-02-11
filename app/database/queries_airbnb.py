
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
