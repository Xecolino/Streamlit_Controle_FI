import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(
    page_title="home",
    layout="wide"
)

if "data" not in st.session_state:
    df_data = pd.read_excel('datasets/OnDrive_Controle_FI.xlsx')
    df_data = df_data.sort_values(by="PATRIMONIO LIQUIDO", ascending=False)
    st.session_state['data'] = df_data


st.markdown("# CONTROLE FI OFICIAL! 🚀")
st.sidebar.markdown("Desenvolvido por [Xeco Academy](https://xeco.academy)")

btn = st.button("Acesse os dados na Intranet BB")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    
st.markdown(
    """
    Gerenciamos a contabilidade de fundos de investimento, garantindo a precisão e transparência dos registros financeiros. 
    Nossa equipe especializada monitora os ativos, passivos e o patrimônio líquido dos fundos, assegurando a conformidade 
    com as regulamentações do mercado financeiro. 
    Elaboramos demonstrações financeiras detalhadas e relatórios gerenciais, fornecendo informações claras e confiáveis para a tomada de decisões estratégicas. 
    Atuamos como guardiões da saúde financeira dos fundos, otimizando a gestão tributária e o cumprimento de obrigações fiscais. 
    Nosso objetivo é assegurar a integridade e a confiabilidade das informações contábeis, promovendo a confiança dos investidores e a sustentabilidade dos fundos.
"""
)    