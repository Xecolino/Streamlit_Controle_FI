import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FI Filtrados",
    page_icon="🏃🏼",
    layout="wide")



df_data = st.session_state["data"]


fundos = df_data['DRIVE'].value_counts().index
fundo  = st.sidebar.selectbox('Selecione o Fundo de Investimentos:', fundos)

df_players = df_data[(df_data["DRIVE"] == fundo)]
players = df_players["NOME DOS FUNDOS"].value_counts().index
player = st.sidebar.selectbox("Razão Social:", players)

player_stats = df_data[df_data["NOME DOS FUNDOS"] == player].iloc[0]

st.title(player_stats["CNPJ"])
st.title(player_stats["NOME DOS FUNDOS"])

st.markdown(f"**Drive:** {player_stats['DRIVE']}")
st.markdown(f"**GFI:** {player_stats['GFI']*1:.0f}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Encerramento do Exercício:** {player_stats['BALANÇO']}")
col2.markdown(f"**Auditor Externo:** {player_stats['AUDITORIA']}")
col3.markdown(f"**Data da Constituição:** {player_stats['DATA DA CONSTITUICAO']}")
st.divider()

st.subheader(f"PATRIMONIO LIQUIDO {player_stats['PATRIMONIO LIQUIDO']}")

# Define o valor mínimo e máximo da barra de progresso
min_value = 0
max_value = df_players["PATRIMONIO LIQUIDO"].max()

# Define o valor atual da barra de progresso
current_value = int(player_stats["PATRIMONIO LIQUIDO"])

# Cria a barra de progresso utilizando st.slider()
progress_value = st.slider("PATRIMONIO LIQUIDO", min_value=min_value, max_value=max_value, value=current_value, disabled=True)

# Exibe o valor atual da barra de progresso
st.write(f"Valor atual: {progress_value}")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor total do ativo do Fundo", value=f"R$ {player_stats['ATIVO']/1000:.0f}")
col2.markdown(f"**Situação do Fundo:** {player_stats['SITUACAO']}")
col3.markdown(f"**Conta Corrente do Fundo:** {player_stats['CONTA CORRENTE']}")

