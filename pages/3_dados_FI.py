import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dados",
    layout="wide"
)

df_data = st.session_state["data"]

fundos = df_data['DRIVE'].value_counts().index
fundo  = st.sidebar.selectbox('Selecione a Auditoria Externa:', fundos)

df_filtered = df_data[(df_data["DRIVE"] == fundo)].set_index("GFI")

st.markdown(df_filtered.iloc[0]["TIPO"])
st.markdown(f"## {fundo}")

columns = ["BALANÇO", "CNPJ", 'PATRIMONIO LIQUIDO', 'ATIVO', 'CONTA CORRENTE']

st.dataframe(df_filtered[columns],
             column_config={
                 "PATRIMONIO LIQUIDO": st.column_config.ProgressColumn(
                     "PATRIMONIO LIQUIDO",format="R$%f", min_value=0, max_value= 1000000),
                 "ATIVO": st.column_config.ProgressColumn("ATIVO", format="R$%f", 
                                                    min_value=0, max_value=df_filtered["ATIVO"].max())
            })

