"""
Gestion de la connexion DuckDB
"""
import duckdb
import pandas as pd
import streamlit as st


@st.cache_resource
def get_connection() -> duckdb.DuckDBPyConnection:
    return duckdb.connect()


def register_dataframe(df: pd.DataFrame, table_name: str) -> None:
    conn = get_connection()
    conn.register(table_name, df)


def execute_query(query: str) -> pd.DataFrame:
    conn = get_connection()
    return conn.execute(query).df()


def table_exists(table_name: str) -> bool:
    conn = get_connection()
    try:
        conn.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
        return True
    except duckdb.CatalogException:
        return False


def get_table_info(table_name: str) -> pd.DataFrame:
    conn = get_connection()
    return conn.execute(f"DESCRIBE {table_name}").df()
