import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração inicial da página
# st.set_page_config(
#     page_title="Projeto: Dashboard de Gestão de Vendas",
#     layout="wide",
# )
st.page_link("pages/home.py", icon="🏠")
st.title("📊 Projeto – Dashboard de Gestão de Vendas")

st.markdown("""
**Contexto:** Este projeto foi desenvolvido para transformar dados brutos de vendas de uma empresa fictícia entre 2022 e 2024 em um dashboard estratégico de Power BI. O objetivo principal foi capacitar gestores com insights claros e acionáveis para a tomada de decisão.
""")
st.image("assets/img/gestao-vendas.png", caption="Dashboard de Gestão de Vendas (Power BI)", use_container_width=True)

st.markdown("---")

# Seção de Resultados e KPIs (agora no início para maior impacto)
st.header("📈 Resultados e KPIs Chave")
st.markdown("Ao consolidar e analisar os dados, conseguimos fornecer uma visão clara do desempenho de vendas, gerando os seguintes resultados:")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Receita Total", value="R$ 548,51 Mi")
with col2:
    st.metric(label="Produtos Vendidos", value="2,12 Mi")
with col3:
    st.metric(label="Ticket Médio", value="R$ 478,65")
with col4:
    st.metric(label="Clientes Atendidos", value="18,48 Mil")

st.markdown("---")

# Seção de Insights (a mais importante)
st.header("🔎 Análise e Insights Estratégicos")
st.markdown("""
A análise de dados revelou informações cruciais para o planejamento comercial e de marketing:
- **Desafio de Mercado:** Identificamos uma **queda significativa nas vendas entre 2023 e 2024**, sinalizando a necessidade urgente de uma revisão estratégica.
- **Oportunidade de Mercado:** O **público feminino representa a maior parte das vendas**, o que aponta para uma grande oportunidade de lançar campanhas de marketing e produtos segmentados para este público.
- **Risco de Dependência:** As marcas **Contoso** e **Northwind Traders** concentram a maior parte da receita. Isso destaca um **risco de dependência de poucos fornecedores**, exigindo uma estratégia de diversificação.
- **Expansão Geográfica:** Enquanto a América do Norte e Europa lideram, a análise mostra um **potencial de crescimento inexplorado na Ásia**, indicando onde a expansão de mercado deve ser focada.
""")

st.markdown("---")

# Seção de Processo e Ferramentas
st.header("⚙️ Processo e Ferramentas Utilizadas")
st.markdown("""
O projeto seguiu uma metodologia completa de Business Intelligence, que incluiu:
- **Fontes de Dados:** Bases de Vendas (2022-2024), Cadastro de Clientes, Lojas e Produtos, todas em formato Excel.
- **ETL (Extract, Transform, Load):** Utilizei **Power Query** no Power BI para limpeza, tratamento e consolidação dos dados.
- **Modelagem de Dados:** Criei um modelo de dados relacional (esquema estrela) para otimizar o desempenho e a análise.
- **Visualização e Storytelling:** Desenvolvi um dashboard intuitivo e claro, com métricas e gráficos que contam a história dos dados de forma visual.
""")

st.markdown("---")

# Exemplo de visualização (Demonstrando suas habilidades em Python)
st.header("🖼️ Demonstração Visual (criada com Python)")
st.write("Aqui, um exemplo de como a evolução do faturamento pode ser visualizada, replicando um dos gráficos do dashboard.")

# Dados fictícios para o gráfico (você pode usar seus dados reais)
data_vendas = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Faturamento": [50, 55, 70, 65, 80, 85]
})
fig = px.line(
    data_vendas, 
    x="Mês", 
    y="Faturamento", 
    title="Evolução Mensal do Faturamento",
    labels={"Faturamento": "Faturamento (em Milhares de R$)"},
    markers=True,
    line_shape="linear"
)
st.plotly_chart(fig)


st.markdown("---")

# Conclusão e Call to Action
st.header("🚀 Conclusão e Habilidades Demonstradas")
st.markdown("""
Este projeto vai além da criação de um dashboard; ele demonstra minha capacidade de:
- **Transformar dados em valor de negócio.**
- **Identificar problemas e oportunidades** em conjuntos de dados complexos.
- **Comunicação de dados:** Usar o **storytelling** para apresentar informações de forma clara e convincente.
- **Habilidades técnicas:** Domínio em **Power BI (DAX e Power Query)** e **análise de dados**.
""")

st.markdown(
    "[Acesse o repositório completo do projeto no GitHub](https://github.com/RaphaelFF/)"
)