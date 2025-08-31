import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# =============================
# Estilos personalizados
# =============================
st.markdown(
    """
    <style>
        /* fundo */
        body {
            background: linear-gradient(135deg, #1c1c1c, #3a3a3a);
            font-family: 'Arial', sans-serif;
        }
        /* estilo dos botoes links */
        .st-emotion-cache-a0ovpn{
            display: inline-block;
            padding: 12px 28px;
            background: linear-gradient(90deg, #00aaff 0%, #0055a2 100%);
            color: #fff;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1.1em;
            box-shadow: 0 4px 16px rgba(0,170,255,0.15);
            cursor: pointer;
            text-decoration: none;
            transition: background 0.3s, transform 0.2s;
            margin-top: 10px;
        }
        .st-emotion-cache-a0ovpn:hover {
            background: linear-gradient(90deg, #0055a2 0%, #00aaff 100%);
            transform: scale(1.05);
            color: #fff;
}
        .main { 
            background-color: transparent; 
            color: #FFFFFF; 
        }
        /* botões */
        .stButton>button, .stDownloadButton>button {
            color: #FFFFFF; 
            background-color: #0055a2; 
            border-radius: 8px; 
            padding: 12px 24px;
            transition: all 0.3s ease; 
            font-weight: bold; 
            border: none;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #003366; 
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
        }
        /* animação  */
        .section-header {
            font-size: 36px; 
            font-weight: bold; 
            color: #00aaff; 
            margin-top: 20px;
            animation: slideIn 1s ease-out;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        @keyframes slideIn {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        /* Imagen no menu lateral */
        .sidebar-image {
            border-radius: 50%; 
            width: 180px; 
            height: 180px; 
            display: block; 
            margin: 0 auto 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }
        .sidebar-image:hover {
            transform: scale(1.1);
        }
        /* Estilos para "cards"  */
        .card {
            background-color: #2c2c2c; 
            padding: 20px; 
            border-radius: 10px; 
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .card h3 {
            margin-top: 0;
            color: #00aaff;
        }
        .card a {
            color: #00aaff;
            text-decoration: none;
            font-weight: bold;
        }
        .espaco{
            margin-bottom: 50px;

        }
    </style>
    """, unsafe_allow_html=True
)


# =============================
# Navegação tabs
# =============================
tabs = st.tabs(["Inicio", "Experiencia", "Formação", "Certificados", "Habilidades"])

# =============================
# Página de Inicio
# =============================
with tabs[0]:
    st.title("Raphael Fernandes França")
    col1, col2 = st.columns([1, 2], vertical_alignment="center")
    with col1:
        st.image("assets/img/eu.jpg", width=250)
    with col2:
        st.markdown("## Ciência da Computação | Analista de Dados")
        st.write(
            "Graduando em Ciência da Computação com experiência em desenvolvimento, automação e análise de dados. Tenho conhecimento em Python, SQL, Power BI, Streamlit e APIs, aplicados em diversos projetos. Busco aplicar minhas habilidades na área de Ciência de Dados e Business Intelligence, apoiando a gestão pública e privada na tomada de decisão orientada por dados."
        )

# =============================
# Experiencia Profesional
# =============================
with tabs[1]:
    st.markdown("<div class='section-header'>Experiencia Profesional</div>", unsafe_allow_html=True)
    experiences = [
    {
        "role": "Residente Tecnológico",
        "company": "Tribunal de Justiça do Amapá (TJAP)",
        "description": "Desenvolvi sistemas de análise e automação utilizando Python, Streamlit e integração com a API Gemini. Criei dashboards interativos para monitoramento de redes com Zabbix e implementei soluções de transcrição automática de áudios, contribuindo para a modernização digital do tribunal."
    },
    {
        "role": "Bolsa TI - Suporte e Automação",
        "company": "Núcleo de Tecnologia da Informação (UNIFAP)",
        "description": "Atuei em manutenção e configuração de infraestrutura tecnológica, além de apoiar processos de backup e segurança de rede. Desenvolvi automações internas para otimizar atividades administrativas, fortalecendo a eficiência operacional da instituição."
    },
    {
        "role": "Monitor II - Suporte de TI",
        "company": "Programa Amapá Jovem",
        "description": "Prestei suporte tecnológico em escolas parceiras e órgãos públicos, organizando relatórios administrativos e auxiliando na informatização de processos. Contribuí para a melhoria da gestão de dados escolares e de frequência de alunos."
    },
    {
        "role": "Projetos em Ciência de Dados e Automação",
        "company": "Independente",
        "description": "Desenvolvi soluções práticas aplicadas a análise de dados e automação: dashboards em Power BI para gestão de vendas, sistemas em Python + Streamlit para monitoramento de redes, web scraping para coleta de dados jurídicos e modelos de transcrição de áudios com IA."
    }
]

    for exp in experiences:
        st.markdown(
            f"<div class='card'><h3>{exp['role']} - {exp['company']}</h3><p>{exp['description']}</p></div>",
            unsafe_allow_html=True
        )

# =============================
# Educação
# =============================
with tabs[2]:
    st.markdown("<div class='section-header'>Formação</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'><h3>Bacharelado em Ciência da Computação</h3>"
        "<p>Universidade Federal do Amapá (UNIFAP) (2019 - Atual, 9º semestre)</p>"
        "<p>Formação sólida em programação, análise de dados, redes de computadores e desenvolvimento de software. "
        "</p></div>",
        unsafe_allow_html=True
    )

# =============================
# Certificaciones y Cursos
# =============================
with tabs[3]:
    st.markdown("<div class='section-header'>Certificados e Cursos</div>", unsafe_allow_html=True)
    certifications = [
        "Curso de Aplicação de Power BI para Aprimoramento de Gestão",
        "Curso de Aperfeiçoamento em Inteligência Artificial com Foco no Desenvolvimento Sustentável na Amazônia",
        "Técnico Operador de Computador – IFAP",
        "Técnico Auxiliar Home Office – UNIFAP"
    ]
    for cert in certifications:
        st.markdown(f"<div class='card'><p>{cert}</p></div>", unsafe_allow_html=True)

# =============================
# Habilidades Técnicas
# =============================
with tabs[4]:
    st.markdown("<div class='section-header'>Habilidades Técnicas</div>", unsafe_allow_html=True)
    skills = """
    <ul>
        <li>💻 <b>Linguagens:</b> Python, SQL, JavaScript, PHP</li>
        <li>📚 <b>Frameworks e bibliotecas:</b> Streamlit, Flat, plotly, numpy, pandas, matplotlib, PyTorch.</li>
        <li>🗄️ <b>Bancos de dados:</b> PostgreSQL, mySQL, SQL Server </li>
        <li>📊 <b>Visualização:</b> Power BI, Streamlit, Storytelling</li>
        <li>☁️ <b>Ferramentas e Ambiente:</b> Google Colab, Excel/Google Sheets, Docker, Git/GitHub</li>
        <li>🛠️ <b>Metodologias:</b> Scrum, Kanban</li>
    </ul>
    """
    st.markdown(f"<div class='card'>{skills}</div>", unsafe_allow_html=True)
# =============================
# FIM DA PRIMEIRA SESSÃO
# =============================
# PARTE 2: INICIO DA SESSÃO
# =============================

tabs_extra = st.tabs(["Projetos Destacados", "Metricas", "Contato"])

# -----------------------------
# Proyectos Destacados
# -----------------------------
with tabs_extra[0]:
    st.markdown("<div class='section-header'>Projetos Destacados</div>", unsafe_allow_html=True)

    projects = [
        {
            "title": "📊 Dashboard de Gestão de Vendas (Power BI)",
            "description": (
                "Criei um dashboard interativo em Power BI para monitorar faturamento, ticket médio, produtos mais vendidos "
                "e crescimento anual. A ferramenta apoia gestores na tomada de decisões estratégicas baseadas em dados de vendas."
            ),
            "link": "pages/gestao-venda.py",
            "img": "assets/img/gestao-vendas.png"
        },
        {
            "title": "🌐 Monitoramento de Redes (Python + Streamlit + Zabbix)",
            "description": (
                "Desenvolvi um sistema para monitorar em tempo real o status das redes de diferentes comarcas do Amapá, "
                "utilizando Python, Streamlit e integração com a API do Zabbix. O dashboard facilita a detecção rápida de falhas."
            ),
            "link": "https://github.com/RaphaelFF/",
            "img": "assets/img/setic.jpg"
        },
        {
            "title": "📝 Transcritor e Resumidor de Áudio (Python + API Gemini)",
            "description": (
                "Implementei uma solução em Python integrada à API Gemini para transcrever e resumir áudios. "
                "O sistema foi aplicado em contexto jurídico, otimizando a análise de sessões e gravações."
            ),
            "link": "https://github.com/RaphaelFF/",
            "img": ""
        },
        {
            "title": "🤖 Web Scraping para Automação no TJAP",
            "description": (
                "Automatizei a coleta e o salvamento de imagens do portal do TJAP utilizando Python e Selenium. "
                "O projeto agilizou a digitalização de conteúdo e a preservação de registros institucionais."
            ),
            "link": "https://github.com/RaphaelFF/",
            "img": ""
        },
        {
            "title": "🎰 Analisador de Padrões de Aposta (Python)",
            "description": (
                "Desenvolvi scripts exploratórios em Python para identificar padrões estatísticos em apostas "
                "da roleta europeia. O estudo demonstra aplicação prática de análise de dados em contextos probabilísticos."
            ),
            "link": "https://github.com/RaphaelFF/",
            "img": ""
        }
    ]

    for proj in projects:
        st.markdown(f"<div class='card'><h3>{proj['title']}</h3>", unsafe_allow_html=True)
        if proj['img']:
            st.image(proj['img'], use_container_width=True)
        st.markdown(f" <p>{proj['description']}</p>", unsafe_allow_html=True)
        
        st.page_link(proj['link'], label="🔗 ver projeto completo")
        st.markdown("<div class='espaco'>", unsafe_allow_html=True)
        
    

# -----------------------------
# Visualizaciones Interactivas
# -----------------------------
with tabs_extra[1]:
    st.markdown("<div class='section-header'>Metricas</div>", unsafe_allow_html=True)
    st.write(
        "Explora mis visualizaciones de datos que muestran mi dominio en el análisis y la interpretación de información. "
        "Estas herramientas interactivas permiten apreciar de forma dinámica los resultados de mis modelos y análisis."
    )
    # Ejemplo: gráfico de barras para habilidades
    data = pd.DataFrame({
        "Habilidad": ["Python", "SQL", "Machine Learning", "Visualización", "Cloud"],
        "Nivel": [95, 90, 85, 80, 75]
    })
    fig_bar = px.bar(data, x="Habilidad", y="Nivel", title="Dominio de Habilidades", labels={"Nivel": "Porcentaje (%)"})
    st.plotly_chart(fig_bar)
    
    # Ejemplo: gráfico de dispersión para mostrar progreso en proyectos
    data_scatter = pd.DataFrame({
        "Tiempo (meses)": [1, 2, 3, 4, 5, 6],
        "Progreso (%)": [10, 30, 50, 70, 85, 95]
    })
    fig_scatter = px.scatter(data_scatter, x="Tiempo (meses)", y="Progreso (%)", title="Progreso en Proyectos a lo largo del Tiempo")
    st.plotly_chart(fig_scatter)

# -----------------------------
# Descargas de CVs
# -----------------------------
with tabs_extra[2]:
    st.markdown("<div class='section-header'>Contato</div>", unsafe_allow_html=True)
 