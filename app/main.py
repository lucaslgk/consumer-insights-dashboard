"""
Point d'entrée de l'application streamlit
"""
import streamlit as st

import sys
from pathlib import Path

# Ajouter le dossier parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.components.file_uploader import render_file_uploader
from app.components.sidebar import render_sidebar_filters
from app.visualizations.chart_shopping import render_shopping_dashboard
from app.visualizations.chart_airbnb import render_airbnb_dashboard


# Configuration de la page
st.set_page_config(
    page_title="Consumer Insights Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    """
    Fonction principale de l'application.
    """
    # Titre principal
    st.title("📊 Consumer Insights Dashboard")
    st.markdown("Analyse interactive de données avec DuckDB et Streamlit")

    st.divider()

    # Section upload de fichier
    df, dataset_type = render_file_uploader()

    # Si un fichier est chargé, afficher le dashboard
    if df is not None and dataset_type in ['shopping', 'airbnb']:
        st.divider()

        # Filtres dans la sidebar
        filters = render_sidebar_filters(dataset_type)

        # Affichage du dashboard selon le type de dataset
        if dataset_type == 'shopping':
            render_shopping_dashboard(filters)
        elif dataset_type == 'airbnb':
            render_airbnb_dashboard(filters)

    elif df is not None and dataset_type == 'unknown':
        st.warning("Le type de dataset n'a pas été reconnu. Veuillez téléverser un fichier CSV compatible.")
        st.info("Formats supportés : Customer Shopping Behavior, Airbnb Open Data")


if __name__ == "__main__":
    main()
