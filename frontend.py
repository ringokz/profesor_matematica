import streamlit as st
import time


# Paleta de colores y rutas de los logos
PRIMARY_COLOR = "#4b83c0"
SECONDARY_COLOR = "#878889"
BACKGROUND_COLOR = "#f4f5f7"

FRONT_LOGO_PATH = "logs/front-log.webp"
ALBERT_LOGO_PATH = "logs/agente-albert.webp"
CLASES_PARTICULARES_LOGO = "logs/clases-particulares-logo.webp"

# Estilo personalizado
def render_custom_styles():
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {BACKGROUND_COLOR};
            }}
            .stSidebar {{
                background-color: #f0f0f0;
                border-right: 1px solid {SECONDARY_COLOR};
            }}
            input, textarea {{
                border: 1px solid {SECONDARY_COLOR};
                border-radius: 5px;
                padding: 8px;
            }}
            .title {{
                color: {PRIMARY_COLOR};
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 0rem;
                margin-top: 0rem
            }}
            .space {{
                margin-bottom: 8rem;
            }}
            .intro-text {{
                font-size: 1.35rem;
                line-height: 1.6;
                margin-bottom: 0rem;
                text-align: justify;
            }}
            .intro-question {{
                font-size: 1.5rem;
                font-weight: bold;
                text-align: center;
                margin-bottom: 1rem;
            }}
            .stButton>button {{
                background-color: {SECONDARY_COLOR};
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 24px;
                font-size: 30px !important;
                transition: background-color 0.3s ease;
            }}
            .stButton>button:hover {{
                background-color: {PRIMARY_COLOR};
                color: white;
            }}
            .button-container {{
                display: flex;
                justify-content: center;
                gap: 1.5rem;
                margin-top: 2rem;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Renderizar el título con logos
def render_title():
    st.markdown(
        '<div class="space"></div>',
        unsafe_allow_html=True
    )
    logo_col1, logo_col2 = st.columns([1, 2.3], gap="medium")
    with logo_col1:
        st.image(ALBERT_LOGO_PATH, use_container_width=True)
    with logo_col2:
        st.image(CLASES_PARTICULARES_LOGO, use_container_width=True)
        
    st.markdown(
        '<div class="title">Albert, asesor Matemático</div>',
        unsafe_allow_html=True,
    )

# Renderizar subtítulo con efecto de escritura
def render_subheader(topic):
    container = st.empty()
    displayed_text = ""
    for char in topic:
        displayed_text += char
        container.subheader(displayed_text)
        time.sleep(0.01)

# Renderizar la introducción y los botones iniciales
def render_intro():
    st.markdown(
        """
        <div class="intro-text">
        Soy <b>Albert</b>, asesor virtual de <b>Clases Particulares La Pampa</b>.<br>
        Estoy aquí para ayudarte en todas tus consultas matemáticas.
        </div>
        <div class="intro-question">
        <br/>
        ¿Qué tema quieres tratar hoy?
        </div>
        """,
        unsafe_allow_html=True,
    )

# Campo de entrada del usuario
def render_input():
    return st.chat_input("Escribe tu mensaje aquí...")

# Renderizar mensaje dinámico con efecto de escritura
def render_dynamic_message(message, avatar=None):
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar=avatar):
            container = st.empty()
            displayed_text = ""
            for char in message["content"]:
                displayed_text += char
                # Detectar contenido LaTeX y mostrar con formato matemático
                if "$$" in displayed_text or "$" in displayed_text:
                    container.markdown(displayed_text, unsafe_allow_html=True)
                else:
                    container.markdown(displayed_text)
                time.sleep(0.0005)


# Renderizar mensaje estático sin efecto
def render_chat_message(role, content, avatar=None):
    with st.chat_message(role, avatar=avatar):
        # Detectar expresiones LaTeX y renderizarlas correctamente
        if "$$" in content or "$" in content:
            st.markdown(content, unsafe_allow_html=True)
        else:
            st.markdown(content)

