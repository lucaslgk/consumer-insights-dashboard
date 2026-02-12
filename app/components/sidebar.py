"""
Composants de la barre latérale avec filtres dynamiques
"""
import streamlit as st

from app.database.queries_shopping import get_filter_options as get_shopping_filters
from app.database.queries_airbnb import get_filter_options as get_airbnb_filters


def render_sidebar_filters(dataset_type: str) -> dict:
    st.sidebar.header("Filtres")

    if dataset_type == 'shopping':
        return _render_shopping_filters()
    elif dataset_type == 'airbnb':
        return _render_airbnb_filters()

    return {}


def _render_shopping_filters() -> dict:
    """
    Filtres pour Customer Shopping
    """
    filters = {}

    try:
        options = get_shopping_filters()

        # Filtre par catégorie
        selected_categories = st.sidebar.multiselect(
            "Catégorie",
            options=options['categories'],
            default=None,
            placeholder="Toutes les catégories"
        )
        if selected_categories:
            filters['category'] = selected_categories

        # Filtre par saison
        selected_seasons = st.sidebar.multiselect(
            "Saison",
            options=options['seasons'],
            default=None,
            placeholder="Toutes les saisons"
        )
        if selected_seasons:
            filters['season'] = selected_seasons

        # Filtre par genre
        selected_genders = st.sidebar.multiselect(
            "Genre",
            options=options['genders'],
            default=None,
            placeholder="Tous les genres"
        )
        if selected_genders:
            filters['gender'] = selected_genders

        # Filtre par localisation
        selected_locations = st.sidebar.multiselect(
            "Localisation",
            options=options['locations'],
            default=None,
            placeholder="Toutes les localisations"
        )
        if selected_locations:
            filters['location'] = selected_locations

    except Exception as e:
        st.sidebar.warning(f"Erreur chargement filtres: {e}")

    return filters


def _render_airbnb_filters() -> dict:
    """
    Filtres pour Airbnb
    """
    filters = {}

    try:
        options = get_airbnb_filters()

        # Filtre par quartier
        selected_neighbourhoods = st.sidebar.multiselect(
            "Quartier",
            options=options['neighbourhoods'],
            default=None,
            placeholder="Tous les quartiers"
        )
        if selected_neighbourhoods:
            filters['neighbourhood'] = selected_neighbourhoods

        # Filtre par type de logement
        selected_room_types = st.sidebar.multiselect(
            "Type de logement",
            options=options['room_types'],
            default=None,
            placeholder="Tous les types"
        )
        if selected_room_types:
            filters['room_type'] = selected_room_types

        # Filtre par politique d'annulation
        selected_policies = st.sidebar.multiselect(
            "Politique d'annulation",
            options=options['cancellation_policies'],
            default=None,
            placeholder="Toutes les politiques"
        )
        if selected_policies:
            filters['cancellation_policy'] = selected_policies

        # Filtre par prix
        st.sidebar.subheader("Fourchette de prix")
        price_min = st.sidebar.number_input("Prix min ($)", min_value=0, value=0)
        price_max = st.sidebar.number_input("Prix max ($)", min_value=0, value=0)

        if price_min > 0:
            filters['price_min'] = price_min
        if price_max > 0:
            filters['price_max'] = price_max

    except Exception as e:
        st.sidebar.warning(f"Erreur chargement filtres: {e}")

    return filters
