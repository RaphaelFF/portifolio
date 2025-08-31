import streamlit as st
from pathlib import Path

pg = st.navigation(
    [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/gestao-venda.py", title="Gestão de Vendas"),
        st.Page("pages/setic.py", title="SETIC"),
        
    ],
    position="hidden",
)
st.markdown(
    """
    <style>

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

    </style>
    """, unsafe_allow_html=True
)

# =============================
# Menu lateral: Informação e CV
# =============================

    
st.sidebar.title("Raphael Fernandes França")
st.sidebar.image("assets/img/eu.jpg", width=180, caption="Analista de Dados | Ciencia da Computação")
st.sidebar.markdown("📍 Macapá - AP")
st.sidebar.markdown("**📞 Teléfono:** (96) 98423 - 5032")
st.sidebar.markdown("**📧 Correo:** raphaelfranca4026@gmail.com")

# CV
cv_es_path = "assets/documents/cv.pdf"

# Fução para baixar CV
def baixar_cv(file_path, label, file_name, unique_key):
    if Path(file_path).is_file():
        with open(file_path, "rb") as file_data:
            st.sidebar.download_button(
                label=label,
                data=file_data,
                file_name=file_name,
                mime="application/pdf",
                key=unique_key,
            )

baixar_cv(cv_es_path, "📄 Baixar CV", "cv-raphael-franca.pdf", unique_key="boton_es_cv")


pg.run()