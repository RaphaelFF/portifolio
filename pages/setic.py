import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração inicial da página
# st.set_page_config(
#     page_title="Projeto: Dashboard de Gestão de Vendas",
#     layout="wide",
# )

st.title("📊 Projeto – Dashboard de Gestão de Vendas")

st.markdown("""
**Contexto:** Este projeto foi desenvolvido para transformar dados brutos de vendas de uma empresa fictícia entre 2022 e 2024 em um dashboard estratégico de Power BI. O objetivo principal foi capacitar gestores com insights claros e acionáveis para a tomada de decisão.
""")
st.image("assets/img/gestao-vendas.png", caption="Dashboard de Gestão de Vendas (Power BI)", use_container_width=True)
