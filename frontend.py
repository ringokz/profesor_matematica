import streamlit as st

# Colores y logos
PRIMARY_COLOR = "#4b83c0"
SECONDARY_COLOR = "#878889"
BACKGROUND_COLOR = "#f4f5f7"

FRONT_LOGO_PATH = "logs/front-log.webp"
CLASES_PARTICULARES_PATH = "logs/clases-particulares-la-pampa.webp"

# Estilos personalizados
def render_custom_styles():
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {BACKGROUND_COLOR};
            }}
            .stButton>button {{
                background-color: {SECONDARY_COLOR};
                color: white;
                font-size: 20px;
                font-weight: bold;
                padding: 15px 30px;
                border: none;
                border-radius: 10px;
                transition: background-color 0.3s ease;
                display: flex;
                justify-content: center;
                align-items: center;
                width: 200px;
                margin: auto;
            }}
            .stButton>button:hover {{
                background-color: {PRIMARY_COLOR};
                color: white;
            }}
            .title {{
                text-align: start;
                color: {PRIMARY_COLOR};
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 1rem;
            }}
            .intro-text {{
                font-size: 1.35rem;
                text-align: start;
                margin-bottom: 1.5rem;
            }}
            .intro-question {{
                font-size: 1.5rem;
                font-weight: bold;
                text-align: center;
                margin-bottom: 2rem;
            }}
            .welcome-message{{
                font-size: 3rem;
                font-weight: normal;
                text-align: start;
                color: #333;
                margin-top: 10px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Renderizar título
def render_title():
    st.image(CLASES_PARTICULARES_PATH, use_container_width=True)
    st.markdown(
        '<div class="title">Profesor de Matemáticas</div>', 
        unsafe_allow_html=True)

# Renderizar introducción con botón "Comenzar"
def render_intro():
    st.markdown(
        """
        <div class="intro-text">
        Soy <b>el profesor de Clases Particulares La Pampa</b>.
        Estoy aquí para ayudarte en todas tus consultas.
        </div>
        <div class="intro-question">
        <b>¿Sobre qué tema puedo ser de ayuda?</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Función para mostrar mensajes en el chat
def render_chat_message(role, content, avatar=None):
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)

# Función para iniciar el chat al presionar el botón "Comenzar"
def start_chat():
    st.session_state.chat_active = True
    st.rerun() 
