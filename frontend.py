import streamlit as st
import time

# Paleta de colores y rutas de los logos
PRIMARY_COLOR = "#4b83c0"
SECONDARY_COLOR = "#878889"
BACKGROUND_COLOR = "#f4f5f7"

ICOMEX_LOGO_PATH = "logos/ICOMEX_Logos sin fondo.png"
SOFIA_LOGO_PATH = "logos/SofIA sin fondo.png"

# Estilo personalizado
def render_custom_styles():
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {BACKGROUND_COLOR};
            }}
            .stSidebar {{
                background-color: #f0f0f0; /* Light gray background */
                border-right: 1px solid {SECONDARY_COLOR}; /* Separator */
            }}
            input {{
                border: 1px solid {SECONDARY_COLOR}; /* Input border color */
                border-radius: 5px; /* Rounded corners */
                padding: 8px;
            }}
            textarea {{
                border: 1px solid {SECONDARY_COLOR}; /* Textarea border color */
                border-radius: 5px; /* Rounded corners */
                padding: 8px;
            }}
            .title {{
                color: {PRIMARY_COLOR};
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 0rem;
            }}
            .intro-text {{
                font-size: 1.35rem;
                line-height: 1.6;  /* Ajustar espaciado entre líneas */
                margin-bottom: 0rem;
                text-align: justify; /* Justificar texto */
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


# Render the title with centered logos
def render_title():
    # Create columns with relative proportions
    logo_col1, logo_col2 = st.columns([1, 4], gap="medium", vertical_alignment="center")

    # Add images to the columns and center them
    with logo_col1:
        # Center the image in the column
        with st.container():
            st.image(SOFIA_LOGO_PATH, use_container_width=True)
    with logo_col2:
        # Center the image in the column
        with st.container():
            st.image(ICOMEX_LOGO_PATH, use_container_width=True)

    # Add a title below the logos, centered
    st.markdown(
        '<div class="title";">SofIA, asesora virtual</div>',
        unsafe_allow_html=True,
    )

# Renderizar subtítulo con efecto de escritura
def render_subheader(topic):
    container = st.empty()  # Crear un contenedor vacío para el texto dinámico
    text = topic
    displayed_text = ""
    for char in text:
        displayed_text += char
        container.subheader(displayed_text)  # Actualizar el contenedor
        time.sleep(0.0)

# Renderizar mensajes con efecto de escritura
def render_messages(messages):
    for message in messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                container = st.empty()
                text = message["content"]
                displayed_text = ""
                for char in text:
                    displayed_text += char
                    container.markdown(displayed_text)
                    time.sleep(0.002)

# Renderizar la introducción y los botones iniciales
def render_intro():
    st.markdown(
        """
        <div class="intro-text">
        Soy <b>SofIA</b>, la asesora virtual de IA de la Agencia I-COMEX.
        Estoy aquí para asesorarte sobre comercio exterior y las potencialidades de inversión en La Pampa.
        </div>
        <div class="intro-question">
        ¿Sobre qué tema puedo ser de ayuda?
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Uso directo de columnas para los botones
    btn_col1, btn_col2 = st.columns(2, gap="medium")
    with btn_col1:
        st.button(
            "**Oportunidades de Inversión**",
            key="intro_inversiones",
            on_click=select_investment,  # Conecta el callback
            use_container_width=True,
        )
    with btn_col2:
        st.button(
            "**¡Quiero exportar!**",
            key="intro_comercio",
            on_click=select_export,  # Conecta el callback
            use_container_width=True,
        )

# Renderizar campo de entrada
def render_input():
    return st.chat_input("Escribe tu mensaje aquí...")

# Funciones de selección
def select_investment():
    st.session_state.selected_topic = "Oportunidades de Inversión"
    st.session_state.initial_message = (
        "¡Hola! Soy Sofía, la asesora virtual de I-COMEX 😊. "
        "Parece que te interesan las oportunidades de inversión en La Pampa. "
        "Decime, ¿cuál es tu nombre y qué aspecto en particular quisieras saber?"
    )
    st.session_state.initial_message_shown = False

def select_export():
    st.session_state.selected_topic = "¡Quiero exportar!"
    st.session_state.initial_message = (
        "¡Hola! Soy Sofía, la asesora virtual de I-COMEX 😊. "
        "Me alegra saber que querés exportar, estoy aquí para ayudarte. "
        "Contame, ¿cómo te llamás y qué estás pensando exportar"
    )
    st.session_state.initial_message_shown = False

def render_dynamic_message(message, avatar=None):
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar=avatar):
            container = st.empty()
            text = message["content"]
            displayed_text = ""
            for char in text:
                displayed_text += char
                container.markdown(displayed_text)
                time.sleep(0.0005)

# Renderizar mensaje estático con avatar
def render_chat_message(role, content, avatar=None):
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)
