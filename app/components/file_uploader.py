"""
Composant Streamlit pour le téléversement de fichiers CSV
"""
import pandas as pd
import streamlit as st

from app.utils.data_processing import preprocess_auto
from app.database.connection import register_dataframe


def render_file_uploader() -> tuple[pd.DataFrame | None, str | None]:
    """
    Affiche le composant d'upload CSV et retourne le DataFrame traité
    """
    uploaded_file = st.file_uploader(
        "Téléverser un fichier CSV",
        type=["csv"],
        help="Fichiers supportés : Customer Shopping Behavior, Airbnb Open Data"
    )

    if uploaded_file is not None:
        try:
            # Lecture du CSV
            df_raw = pd.read_csv(uploaded_file, low_memory=False)

            # Preprocessing automatique selon le type de dataset
            df_clean, dataset_type = preprocess_auto(df_raw)

            # Protection contre la casse si un utilisateur uploade un dataset inconnu
            if dataset_type == 'unknown':
                st.warning("Type de dataset non reconnu. Aucun preprocessing appliqué.")
            else:
                st.success(f"Dataset **{dataset_type.upper()}** détecté et nettoyé.")

            # Enregistrement dans duckdb
            register_dataframe(df_clean, dataset_type)

            # Affichage
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Lignes", f"{len(df_clean):,}")
            with col2:
                st.metric("Colonnes", len(df_clean.columns))

            # Aperçu des data
            with st.expander("Aperçu des données"):
                st.dataframe(df_clean.head(10))

            return df_clean, dataset_type

        except Exception as e:
            st.error(f"Erreur lors du chargement : {e}")
            return None, None

    return None, None
