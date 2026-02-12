"""
Application streamlit
"""
import streamlit as st

import sys
from pathlib import Path

# Connexion au bon dossier pour les imports (à ne pas modifier)
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.components.file_uploader import render_file_uploader
from app.components.sidebar import render_sidebar_filters
from app.visualizations.chart_shopping import render_shopping_dashboard
from app.visualizations.chart_airbnb import render_airbnb_dashboard


# Paramètres de la page
st.set_page_config(
    page_title="Consumer Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    """
    Fonction principale de l'application avec choix automatique du dashboard en fonction du dataset inséré

    """
    # Titre principal
    st.title("Consumer Insights Dashboard")
    st.markdown("Analyse interactive de données avec DuckDB et Streamlit")

    st.divider()

    # Section upload de fichier
    df, dataset_type = render_file_uploader()

    # Si un fichier est chargé affiche le dashboard
    if df is not None and dataset_type in ['shopping', 'airbnb']:
        st.divider()

        # Filtres
        filters = render_sidebar_filters(dataset_type)

        # Affichage du dashboard selon le type de dataset
        if dataset_type == 'shopping':
            render_shopping_dashboard(filters)
        elif dataset_type == 'airbnb':
            render_airbnb_dashboard(filters)

    elif df is not None and dataset_type == 'unknown':
        st.warning("Les données n'ont pas été reconnues. Veuillez insérer un fichier au format CSV compatible.")
        st.info("Fichiers supportés : Customer Shopping Behavior, Airbnb Open Data")


if __name__ == "__main__":
    main()
