"""
Visualisations pour le dataset Airbnb Open Data : 4 KPI avec graphiques Plotly
"""
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from app.database.queries_airbnb import (
    get_avg_price_by_neighbourhood,
    get_room_type_distribution,
    get_avg_availability_by_neighbourhood,
    get_avg_rating_by_room_type
)


def render_airbnb_dashboard(filters: dict = None) -> None:
    
    """

    Affiche le dashboard complet pour Airbnb.
    """
    st.header("Dashboard Airbnb Open Data")

    # Ligne 1: 2 graphiques
    col1, col2 = st.columns(2)

    with col1:
        render_avg_price_by_neighbourhood(filters)

    with col2:
        render_room_type_distribution(filters)

    # Ligne 2: 2 graphiques
    col3, col4 = st.columns(2)

    with col3:
        render_avg_availability(filters)

    with col4:
        render_avg_rating_by_room_type(filters)


def render_avg_price_by_neighbourhood(filters: dict = None) -> None:
    """
    KPI 1: Bar chart du prix moyen par quartier
    """


    st.subheader("Prix Moyen par Quartier")



    df = get_avg_price_by_neighbourhood(filters)

    fig = px.bar(
        df,
        x='quartier',
        y='prix_moyen',
        color='prix_moyen',
        text='prix_moyen',
        labels={'quartier': 'Quartier', 'prix_moyen': 'Prix moyen ($)'},
        color_continuous_scale='Reds'
    )
    fig.update_traces(texttemplate='$%{text:.0f}', textposition='outside')
    fig.update_layout(showlegend=False, height=400)

    st.plotly_chart(fig, use_container_width=True)


def render_room_type_distribution(filters: dict = None) -> None:
    """
    KPI 2 : distribution des types de logement (pie chart)
    """
    st.subheader("Types de Logement")

    df = get_room_type_distribution(filters)

    fig = px.pie(
        df,
        values='nb_logements',
        names='type_logement',
        hole=0.4,
        labels={'type_logement': 'Type', 'nb_logements': 'Logements'}
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400)

    st.plotly_chart(fig, use_container_width=True)


def render_avg_availability(filters: dict = None) -> None:
    """
    KPI 3: bar chart de la disponibilité moyenne par quartier
    """
    
    st.subheader("Disponibilité Moyenne (jours/an)")

    df = get_avg_availability_by_neighbourhood(filters)

    fig = px.bar(
        df,
        x='quartier',
        y='disponibilite_moyenne',
        color='disponibilite_moyenne',
        text='disponibilite_moyenne',
        labels={'quartier': 'Quartier', 'disponibilite_moyenne': 'Jours disponibles'},
        color_continuous_scale='Greens'
    )
    fig.update_traces(texttemplate='%{text:.0f}j', textposition='outside')
    fig.update_layout(showlegend=False, height=400)

    st.plotly_chart(fig, use_container_width=True)


def render_avg_rating_by_room_type(filters: dict = None) -> None:
    
    
    """
    KPI 4: Bar chart des notes moyennes par type de logement
    """
    st.subheader("Note Moyenne par Type de Logement")

    df = get_avg_rating_by_room_type(filters)

    fig = px.bar(
        df,
        x='type_logement',
        y='note_moyenne',
        color='note_moyenne',
        text='note_moyenne',
        labels={'type_logement': 'Type', 'note_moyenne': 'Note moyenne'},
        color_continuous_scale='Purples'
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(showlegend=False, height=400, yaxis_range=[0, 5])

    st.plotly_chart(fig, use_container_width=True)
