#Importação das bibliotecas
import streamlit as st 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib
from joblib import load
import time

#carregando os dados 
df_modelo = pd.read_csv('https://raw.githubusercontent.com/denis-hwk/datathon_postech_fiap_9dtat_grupo140/refs/heads/main/modelo/df_modelo.csv')

############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Formulário para Avaliação de Risco de Defasagem</h1>", unsafe_allow_html = True)

st.warning('Preencha o formulário com todos os dados de avaliações do ano atual e do ano anterior, depois clique no botão **ENVIAR** no final da página.')

# Input de indicadores do ano atual
st.markdown("<h2 style='text-align: center; '> Indicadores do ano atual </h1>", unsafe_allow_html = True)

# Indicador de Auto Avalição do ano atual (IAA)
st.write('### Indicador de Auto Avalição do ano atual (IAA)')
input_IAA_Atual = st.number_input('Digite a nota IAA do ano atual', min_value=0.00, format="%0.1f")

# Indicador de Engajamento do ano atual (IEG)
st.write('### Indicador de Engajamento do ano atual (IEG)')
input_IEG_Atual = st.number_input('Digite a nota IEG do ano atual', min_value=0.00, format="%0.1f")

# Indicador Psicossocial do ano atual (IPS)
st.write('### Indicador Psicossocial do ano atual (IPS)')
input_IPS_Atual = st.number_input('Digite a nota IPS do ano atual', min_value=0.00, format="%0.1f")

# Indicador Psicopedagógico  do ano atual (IPP)
st.write('### Indicador Psicopedagógico do ano atual (IPP)')
input_IPP_Atual = st.number_input('Digite a nota IPP do ano atual', min_value=0.00, format="%0.1f")

# Indicador de Aprendizagem do ano atual (IDA)
st.write('### Indicador de Engajamento do ano atual (IDA)')
input_IDA_Atual = st.number_input('Digite a nota IDA do ano atual', min_value=0.00, format="%0.1f")

# Input de indicadores do ano anterior
st.markdown("<h2 style='text-align: center; '> Indicadores do ano anterior </h1>", unsafe_allow_html = True)

# Indicador de Auto Avalição do ano anterior (IAA)
st.write('### Indicador de Auto Avalição do ano anterior (IAA)')
input_IAA_A_1 = st.number_input('Digite a nota IAA do ano anterior', min_value=0.00, format="%0.1f")

# Indicador de Engajamento do ano anterior (IEG)
st.write('### Indicador de Engajamento do ano anterior (IEG)')
input_IEG_A_1 = st.number_input('Digite a nota IEG do ano anterior', min_value=0.00, format="%0.1f")

# Indicador Psicossocial do ano anterior (IPS)
st.write('### Indicador Psicossocial do ano anterior (IPS)')
input_IPS_A_1 = st.number_input('Digite a nota IPS do ano anterior', min_value=0.00, format="%0.1f")

# Indicador Psicopedagógico  do ano anterior (IPP)
st.write('### Indicador Psicopedagógico do ano anterior (IPP)')
input_IPP_A_1 = st.number_input('Digite a nota IPP do ano anterior', min_value=0.00, format="%0.1f")

# Indicador de Aprendizagem do ano anterior (IDA)
st.write('### Indicador de Engajamento do ano anterior (IDA)')
input_IDA_A_1 = st.number_input('Digite a nota IDA do ano anterior', min_value=0.00, format="%0.1f")

# Indicador de Defasagem do ano anterior (Defasagem)
st.write('### Indicador de Defasagem do ano anterior (Defasagem)')
input_defasagem_A_1 = float(st.slider('Indique a defasagem do ano anterior', -3, 3))
input_defasagem_dict = {-3: 0, 
                        -2: 1,
                        -1: 2,
                         0: 3,
                         1: 4,
                         2: 5,
                         3: 6}
input_defasagem_A_1 = input_defasagem_dict.get(input_defasagem_A_1)

# Lista de todas as variáveis: 
novo_aluno = [input_IAA_Atual, # Indicador de Auto Avalição do ano atual (IAA_Atual)
              input_IEG_Atual, # Indicador de Engajamento do ano atual (IEG_Atual)
              input_IPS_Atual, # Indicador Psicossocial do ano atual (IPS_Atual)
              input_IPP_Atual, # Indicador Psicopedagógico do ano atual (IPP_Atual)
              input_IDA_Atual, # Indicador de Aprendizagem do ano atual (IDA_Atual)
              0,               # Indicador de Defasagem do ano atual (Defasagem_Atual)
              input_IAA_A_1,   # Indicador de Auto Avalição do ano anterior (IAA_A-1)
              input_IEG_A_1,   # Indicador de Engajamento do ano anterior (IEG_A-1)
              input_IPS_A_1,   # Indicador Psicossocial do ano anterior (IPS_A-1)
              input_IPP_A_1,   # Indicador Psicopedagógico  do ano anterior (IPP_A-1)
              input_IDA_A_1,   # Indicador de Aprendizagem do ano anterior (IDA_A-1)
              input_defasagem_A_1,  # Indicador de Defasagem do ano anterior (Defasagem_A-1)
              ]

# Separação das amostras de treino e teste
def df_train_test_split(df, test_size):
  seed = 1337
  df_train, df_test = train_test_split(df_modelo, test_size=test_size, random_state=seed)
  return df_train, df_test

df_train, df_test = df_train_test_split(df_modelo, 0.3)

# Consolidando dados do novo cliente
novo_cliente_modelo = pd.DataFrame([novo_aluno], columns=df_test.columns)

# Adicionando novo cliente ao dataframe dos dados de teste
df_novo_cliente  = pd.concat([df_test, novo_cliente_modelo], ignore_index=True)

# Separando variáveis para treino do modelo
X_train, y_train = df_train.drop(columns='Defasagem_Atual'), df_train['Defasagem_Atual']

# Removendo a coluna target do teste
previsao_novo_cliente = df_novo_cliente.drop(columns='Defasagem_Atual')

# Gerar previsão do modelo 
if st.button('Enviar'):
    # Criar a barra de progresso
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Etapa 1: Carregando o modelo
    status_text.text('Carregando modelo...')
    progress_bar.progress(25)
    model = joblib.load('modelo/random_forest_classifier.joblib')
    model.fit(X_train, y_train)
    
    # Etapa 2: Preparando dados
    status_text.text('Preparando dados para previsão...')
    progress_bar.progress(50)
    time.sleep(0.3)  # Pequena pausa para visualização
    
    # Etapa 3: Executando previsão
    status_text.text('Executando modelo de previsão...')
    progress_bar.progress(75)
    score = model.predict_proba(previsao_novo_cliente)
    
    # Etapa 4: Finalizando
    status_text.text('Finalizando...')
    progress_bar.progress(100)
    time.sleep(0.3)
    
    # Limpar a barra de progresso e texto de status
    progress_bar.empty()
    status_text.empty()
    
    # Mostrar resultado
    st.write(score[-1])