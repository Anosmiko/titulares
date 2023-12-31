import streamlit as st 
import pandas as pd


df = pd.read_parquet("titulares_2012_2022_sin_duplicados.parquet")

st.dataframe(df)