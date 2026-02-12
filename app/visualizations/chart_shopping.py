"""
Visualisations pour le dataset Customer Shopping Behavior - 4 KPI
"""
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from app.database.queries_shopping import (
    get_sales_by_category,
    get_sales_by_gender_season,
    get_avg_basket_by_age,
    get_payment_methods
)


def render_shopping_dashboard(filters: dict = None) -> None:
    """
    Affiche le dashboard complet pour Customer Shopping.
    """


    st.header("Dashboard Customer Shopping Behavior")

    # Ligne 1 2 graphiques
    col1, col2 = st.columns(2)

    with col1:
        render_sales_by_category(filters)

    with col2:
        render_payment_methods(filters)

    # Ligne 2 avec 2 graphiques
    col3, col4 = st.columns(2)

    with col3:
        render_avg_basket_by_age(filters)

    with col4:
        render_sales_by_gender_season(filters)


def render_sales_by_category(filters: dict = None) -> None:
    
    """
    Bar chart des ventes par catégorie
    """
    st.subheader("Ventes par Catégorie")

    df = get_sales_by_category(filters)

    fig = px.bar(
        df,
        x='categorie',
        y='total_ventes',
        color='categorie',
        text='total_ventes',
        labels={'categorie': 'Catégorie', 'total_ventes': 'Ventes (USD)'}
    )
    fig.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
    fig.update_layout(showlegend=False, height=400)

    st.plotly_chart(fig, use_container_width=True)


def render_sales_by_gender_season(filters: dict = None) -> None:
    """
    Heatmap ventes par genre et saison
    """


    st.subheader("Ventes par Genre et Saison")

    df = get_sales_by_gender_season(filters)

    # Pivot pour la heatmap
    pivot_df = df.pivot(index='genre', columns='saison', values='total_ventes')

    fig = px.imshow(
        pivot_df,
        labels=dict(x="Saison", y="Genre", color="Ventes (USD)"),
        color_continuous_scale='Blues',
        text_auto='.0f'
    )
    fig.update_layout(height=400)

    st.plotly_chart(fig, use_container_width=True)


def render_avg_basket_by_age(filters: dict = None) -> None:
    """
    Bar chart du panier moyen par tranche d'âge
    """

    st.subheader("Panier Moyen par Tranche d'Âge")

    df = get_avg_basket_by_age(filters)

    fig = px.bar(
        df,
        x='tranche_age',
        y='panier_moyen',
        color='panier_moyen',
        text='panier_moyen',
        labels={'tranche_age': "Tranche d'âge", 'panier_moyen': 'Panier moyen (USD)'},
        color_continuous_scale='Viridis'
    )
    fig.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
    fig.update_layout(showlegend=False, height=400)

    st.plotly_chart(fig, use_container_width=True)


def render_payment_methods(filters: dict = None) -> None:
    """
    
    Pie chart des méthodes de paiement
    """
    st.subheader("Méthodes de Paiement")

    df = get_payment_methods(filters)

    fig = px.pie(
        df,
        values='nb_transactions',
        names='methode_paiement',
        hole=0.4,
        labels={'methode_paiement': 'Méthode', 'nb_transactions': 'Transactions'}
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400)

    st.plotly_chart(fig, use_container_width=True)
