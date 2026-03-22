import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(layout="wide")

url = 'https://raw.githubusercontent.com/denis-hwk/datathon_postech_fiap_9dtat_grupo140/refs/heads/main/streamlit_app/dados/df_dashboard.csv'
df_final = pd.read_csv(url, delimiter = ',')

############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Dashboard para Análise de Dados sobre o Passos Mágicos </h1>", unsafe_allow_html = True)

col11, col21 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col11:
    dados_IAN = df_final[['RA', 'IAN_2022', 'IAN_2023', 'IAN_2024']]
    dados_IAN = pd.melt(
        dados_IAN,
        id_vars = ['RA'],
        value_vars = ['IAN_2022', 'IAN_2023', 'IAN_2024'],
        var_name = 'Ano',
        value_name = 'IAN'
        )
    dados_IAN['Ano'] = dados_IAN['Ano'].str.replace('IAN_', '')
    dados_IAN.dropna(subset=['IAN'], inplace=True)

    contagem_IAN = dados_IAN.groupby(['Ano','IAN'])['RA'].nunique().reset_index()

    # Gráfico de Proporções de IAN por ano
    st.write('### Distribuição IAN anual')
    fig_ian = px.bar(
        contagem_IAN,
        x='Ano',
        y='RA',
        color='IAN',
        barmode='stack'
        )
    
    fig_ian.update_traces(
        hovertemplate='IAN: %{y:.1f}<extra></extra>'
        )
    
    fig_ian.update_layout(
        barnorm="percent", 
        yaxis=dict(title='Percentual'
        )
    )

    st.plotly_chart(fig_ian, use_container_width=True)

    

with col21:
    dados_IDA = df_final[['RA', 'IDA_2022', 'IDA_2023', 'IDA_2024']]

    dados_IDA = pd.melt(
        dados_IDA,
        id_vars = ['RA'],
        value_vars = ['IDA_2022', 'IDA_2023', 'IDA_2024'],
        var_name = 'Ano',
        value_name = 'IDA'
        )
    
    dados_IDA['Ano'] = dados_IDA['Ano'].str.replace('IDA_', '')

    dados_IDA.dropna(subset=['IDA'], inplace=True)
    
    # Gráfico de IDA ao longo dos anos
    fig_ida = px.histogram(
        dados_IDA,
        x='IDA',
        y='RA',
        color='Ano',
        barmode='group',
        histnorm='percent',
        histfunc='count',
        nbins=20
        )
    st.plotly_chart(fig_ida, use_container_width=True)