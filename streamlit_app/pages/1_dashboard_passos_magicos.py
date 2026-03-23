import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import statsmodels.api as sm 
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(layout="wide")

url = 'https://raw.githubusercontent.com/denis-hwk/datathon_postech_fiap_9dtat_grupo140/refs/heads/main/streamlit_app/dados/df_dashboard.csv'
df_final = pd.read_csv(url, delimiter = ',')

# Dados IAN
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

# Dados IDA
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

# Dados IEG
dados_IEG = df_final[['RA', 'IEG_2022', 'IEG_2023', 'IEG_2024']]
dados_IEG = pd.melt(
    dados_IEG,
    id_vars = ['RA'],
    value_vars = ['IEG_2022', 'IEG_2023', 'IEG_2024'],
    var_name = 'Ano',
    value_name = 'IEG'
    )
dados_IEG['Ano'] = dados_IEG['Ano'].str.replace('IEG_', '')

# Dados IPV
dados_IPV = df_final[['RA', 'IPV_2022', 'IPV_2023', 'IPV_2024']]
dados_IPV = pd.melt(
    dados_IPV,
    id_vars = ['RA'],
    value_vars = ['IPV_2022', 'IPV_2023', 'IPV_2024'],
    var_name = 'Ano',
    value_name = 'IPV'
    )
dados_IPV['Ano'] = dados_IPV['Ano'].str.replace('IPV_', '')

# Dados IAA
dados_IAA = df_final[['RA', 'IAA_2022', 'IAA_2023', 'IAA_2024']]
dados_IAA = pd.melt(
    dados_IAA,
    id_vars = ['RA'],
    value_vars = ['IAA_2022', 'IAA_2023', 'IAA_2024'],
    var_name = 'Ano',
    value_name = 'IAA'
    )

# Dados IPS
dados_IPS = df_final[['RA', 'IPS_2022', 'IPS_2023', 'IPS_2024']]
dados_IPS = pd.melt(
    dados_IPS,
    id_vars = ['RA'],
    value_vars = ['IPS_2022', 'IPS_2023', 'IPS_2024'],
    var_name = 'Ano',
    value_name = 'IPS'
    )
dados_IPS['Ano'] = dados_IPS['Ano'].str.replace('IPS_', '')

# Dados_IPP
dados_IPP = df_final[['RA', 'IPP_2022', 'IPP_2023', 'IPP_2024']]
dados_IPP = pd.melt(
    dados_IPP,
    id_vars = ['RA'],
    value_vars = ['IPP_2022', 'IPP_2023', 'IPP_2024'],
    var_name = 'Ano',
    value_name = 'IPP'
    )
dados_IPP['Ano'] = dados_IPP['Ano'].str.replace('IPP_', '')

# Dados Ponto de Virada
dados_IPV = df_final[['RA', 'IPV_2022', 'IPV_2023', 'IPV_2024']]
dados_IPV = pd.melt(
    dados_IPV,
    id_vars = ['RA'],
    value_vars = ['IPV_2022', 'IPV_2023', 'IPV_2024'],
    var_name = 'Ano',
    value_name = 'IPV'
    )
dados_IPV['Ano'] = dados_IPV['Ano'].str.replace('IPV_', '')

# Dados Desenvolvimento Educacional
dados_INDE = df_final[['RA', 'INDE_2022', 'INDE_2023', 'INDE_2024']]
dados_INDE = pd.melt(
    dados_INDE,
    id_vars = ['RA'],
    value_vars = ['INDE_2022', 'INDE_2023', 'INDE_2024'],
    var_name = 'Ano',
    value_name = 'INDE'
    )
dados_INDE['Ano'] = dados_INDE['Ano'].str.replace('INDE_', '')

# Dados Engajamento, Aprendizagem e Ponto de Virada
dados_IEG_IDA = dados_IEG.merge(dados_IDA, on=['RA', 'Ano'], how='left')
dados_eng_desempenho = dados_IEG_IDA.merge(dados_IPV, on=['RA', 'Ano'], how='left')

# Dados Auto Avaliação, Aprendizagem e Engajamento
dados_IAA_IDA = dados_IAA.merge(dados_IDA, on=['RA', 'Ano'], how='left')
dados_autoavaliacao = dados_IAA_IDA.merge(dados_IEG, on=['RA', 'Ano'], how='left')
dados_autoavaliacao.dropna(subset=['IAA', 'IDA', 'IEG'], inplace=True)

# Dados Engajamento, Aprendizagem e Psicossocial
dados_IEG_IDA = dados_IEG.merge(dados_IDA, on=['RA', 'Ano'], how='left')
dados_desempenho = dados_IEG_IDA.merge(dados_IPS, on=['RA', 'Ano'], how='left')

# Média Psicossocial, Engajamento e Aprendizagem
media_ips_anual = dados_desempenho.groupby('Ano')['IPS'].mean().reset_index()
media_ieg_anual = dados_desempenho.groupby('Ano')['IEG'].mean().reset_index()
media_ida_anual = dados_desempenho.groupby('Ano')['IDA'].mean().reset_index()

media_ips_ieg_ian_anual = media_ips_anual.merge(media_ieg_anual, on='Ano', how='left').merge(media_ida_anual, on='Ano', how='left')

# Dados Psicopedagógico e Adequação de Nível
dados_ipp_ian = dados_IPP.merge(dados_IAN, on=['RA', 'Ano'], how='left')
dados_ipp_ian.dropna(subset=['IPP', 'IAN'], inplace=True)

# Dados Ponto de Virada, Aprendizagem, Engajamento, Psicossocial, Psicopedagógico, Auto-avaliação
dados_ipv_ida = dados_IPV.merge(dados_IDA, on=['RA', 'Ano'], how='left')
dados_ipv_ieg = dados_ipv_ida.merge(dados_IEG, on=['RA', 'Ano'], how='left')
dados_ipv_ips = dados_ipv_ieg.merge(dados_IPS, on=['RA', 'Ano'], how='left')
dados_ipv_ipp = dados_ipv_ips.merge(dados_IPP, on=['RA', 'Ano'], how='left')
dados_ponto_de_virada = dados_ipv_ipp.merge(dados_IAA, on=['RA', 'Ano'], how='left')
dados_ponto_de_virada.dropna(subset=['IPV', 'IDA', 'IEG', 'IPS', 'IPP', 'IAA'])

# Dados Desenvolvimento Educacional, Engajamento, Aprendizado, Psicopedagógico, Psicossocial, Auto-Avaliação
dados_INDE_IDA = dados_INDE.merge(dados_IDA, on=['RA', 'Ano'], how='left')
dados_INDE_IEG = dados_INDE_IDA.merge(dados_IEG, on=['RA', 'Ano'], how='left')
dados_INDE_IPP = dados_INDE_IEG.merge(dados_IPP, on=['RA', 'Ano'], how='left')
dados_INDE_IAA = dados_INDE_IPP.merge(dados_IAA, on=['RA', 'Ano'], how='left')
dados_multidimendisionalidade = dados_INDE_IAA.merge(dados_IPS, on=['RA', 'Ano'], how='left')
dados_multidimendisionalidade.dropna(subset=['INDE', 'IDA', 'IEG', 'IPP', 'IPS', 'IAA'], inplace=True)

############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Dashboard para Análise de Dados sobre o Passos Mágicos </h1>", unsafe_allow_html = True)

col11, col12 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col11:
    
    st.write('### Distribuição Indicador de Adequação de Nível Anual')
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

    st.plotly_chart(fig_ian, width='stretch')

with col12:

    st.write('### Distribuição Indicador de Aprendizagem')
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

col21, col22 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col21:

    st.write('### Dispersão entre Indicador de Engagamento e Indicador de Ponto de Virada')

    fig_ieg_ipv = px.scatter(
    dados_eng_desempenho,
    x='IEG',
    y='IPV',
    trendline='ols'
    )

    st.plotly_chart(fig_ieg_ipv, width='stretch')

with col22:

    st.write('### Dispersão entre Indicador de Engagamento e Indicador de Aprendizagem')

    fig_ieg_ida = px.scatter(
        dados_eng_desempenho,
        x='IEG',
        y='IDA',
        trendline='ols'
    )
    st.plotly_chart(fig_ieg_ida, width='stretch')

col31, col32 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col31:
    
    st.write('### Dispersão entre Indicador de Auto-Avaliação e Indicador de Aprendizagem')

    fig_iaa_ida = px.scatter(
        dados_autoavaliacao,
        x='IAA',
        y='IDA',
        trendline='ols'
    )

    st.plotly_chart(fig_iaa_ida, width='stretch')

with col32:

    st.write('### Dispersão entre Indicador de Auto-Avaliação e Indicador de Engajamento')

    fig_iaa_ieg = px.scatter(
        dados_autoavaliacao,
        x='IAA',
        y='IEG',
        trendline='ols'
    )
    st.plotly_chart(fig_iaa_ieg, width='stretch')

col41, col42 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col41:
    
    st.write('### Boxplot do Indicador Psicossocial Anual')

    fig_ips = px.box(
        dados_desempenho,
        x='IPS',
        color='Ano')
    st.plotly_chart(fig_ips, width='stretch')

with col42:

    st.write('### Boxplot do Indicador Engajamento Anual')

    fig_ieg_box = px.box(
        dados_desempenho,
        x='IEG',
        color='Ano'
        )
    st.plotly_chart(fig_ieg_box, width='stretch')

col51, col52 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col51:
    
    st.write('### Boxplot do Indicador Aprendizagem Anual')

    fig_ida = px.box(
        dados_desempenho,
        x='IDA',
        color='Ano'
        )
    st.plotly_chart(fig_ida, width='stretch')

with col52:

    st.write('### Gráfico Média Anual IPS, IEG e IDA')

    fig_media_ips_ieg_ian = px.bar(
        media_ips_ieg_ian_anual,
        x='Ano',
        y=['IPS', 'IEG', 'IDA'],
        title='Média de IPS, IEG e IDA por Ano',
        barmode='group'
        )
    st.plotly_chart(fig_media_ips_ieg_ian, width='stretch')

col61, col62 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col61:
    
    st.write('### Histograma do Indicador Psicopedagógico Anual')

    fig_ipp = px.histogram(
        dados_ipp_ian,
        x='IPP',
        y='RA',
        color='Ano',
        histfunc='count',
        histnorm='percent',
        barmode='group',
        nbins=20
        )
    st.plotly_chart(fig_ipp, width='stretch')

with col62:

    st.write('### Matriz de Correlação IPV, IDA, IEG, IPS, IPP, IAA')

    matriz_correlacao_ponto_de_virada = dados_ponto_de_virada[['IPV', 'IDA', 'IEG', 'IPS', 'IPP', 'IAA']].corr()
    fig_matriz_corr_ipv = px.imshow(matriz_correlacao_ponto_de_virada, text_auto=True)
    st.plotly_chart(fig_matriz_corr_ipv, use_container_width=True)

col71, col72 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col71:
    
    st.write('### Matriz de Correlação INDE, IDA, IEG, IPP, IPS, IAA')

    matriz_correlacao_inde = dados_multidimendisionalidade[['INDE', 'IDA', 'IEG', 'IPP', 'IPS','IAA']].corr()
    fig_correlacao_inde = px.imshow(matriz_correlacao_inde, text_auto=True)
    st.plotly_chart(fig_correlacao_inde, width='stretch')

with col72:

    st.write('### Dispersão Desenvolvimento Educacional e Aprendizagem')

    fig_inde_ida = px.scatter(
        dados_multidimendisionalidade,
        x='INDE',
        y='IDA',
        color='Ano',
        trendline='ols'
        )
    st.plotly_chart(fig_inde_ida, width='stretch')

col81, col82 = st.columns(2, gap="small", vertical_alignment="top", border=False, width="stretch")

with col81:
    
    st.write('### Histograma do Indicador Psicopedagógico Anual')

    fig_inde_ieg = px.scatter(
        dados_multidimendisionalidade,
        x='INDE',
        y='IEG',
        color='Ano',
        trendline='ols'
        )
    st.plotly_chart(fig_inde_ieg, width='stretch')

with col82:

    st.write('### Matriz de Correlação IPV, IDA, IEG, IPS, IPP, IAA')

    fig_inde_ipp = px.scatter(
        dados_multidimendisionalidade,
        x='INDE',
        y='IPP',
        color='Ano',
        trendline='ols'
        )
    st.plotly_chart(fig_inde_ipp, width='stretch')