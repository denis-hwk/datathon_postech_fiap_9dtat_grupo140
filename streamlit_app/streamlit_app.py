#Importação das bibliotecas
import streamlit as st 
import pandas as pd
from utils import MinMaxScalerFeatures, OneHotEncodingFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib
from joblib import load
import time
import plotly.express as px

st.set_page_config(page_title="FIAP Datathon - Passos Mágicos")
st.title("FIAP Datathon - Passos Mágicos")
st.write("Essa página é dedicada a apresentar uma solução de visualização dos dados provenientes das pesquisas PEDE de 2022 a 2024 e um modelo preditivo para o risco de defasagem dos alunos da instituição.")
st.write("\nTodo o conteúdo presente nessa página foi desenvolvido por Dênis Korin")