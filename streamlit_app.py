import streamlit as st
import frontend
from openai import OpenAI

# Configuración de la página
SOFIA_LOGO_PATH = "logos/SofIA sin fondo.png"
st.set_page_config(page_title="Sofía - Asistente Virtual", layout="centered", page_icon=SOFIA_LOGO_PATH)

# Inicializar estilos personalizados
frontend.render_custom_styles()

# Inicialización del estado
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "initial_message_shown" not in st.session_state:
    st.session_state.initial_message_shown = False

# Archivos de instrucciones del sistema
INSTRUCTIONS_FILES = {
    "Oportunidades de Inversión": "instructions_inversiones.txt",
    "Exportación de Servicios": "instructions_comercio_exterior.txt",
}

# Obtener clave API de secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Función para cargar instrucciones
def load_instructions(topic):
    try:
        with open(INSTRUCTIONS_FILES[topic], "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        st.error(f"No se encontró el archivo de instrucciones para {topic}.")
        return None

# Renderizar el encabezado principal
frontend.render_title()

# Renderizar la introducción si no se ha seleccionado un tema
if st.session_state.selected_topic is None:
    frontend.render_intro()

# Mostrar subtítulo, instrucciones y chat si se seleccionó un tema
if st.session_state.selected_topic:
    frontend.render_subheader(st.session_state.selected_topic)

    # Cargar las instrucciones del sistema solo una vez
    if not st.session_state.initial_message_shown:
        instructions = load_instructions(st.session_state.selected_topic)
        if instructions:
            # Agregar el mensaje del sistema solo para el contexto del LLM
            st.session_state.messages.append({"role": "system", "content": instructions})
        # Agregar el mensaje inicial del asistente para la interfaz
        st.session_state.messages.append({"role": "assistant", "content": st.session_state.initial_message})
        st.session_state.initial_message_shown = True

    # Renderizar los mensajes, filtrando los mensajes del sistema
    for message in st.session_state.messages:
        if message["role"] != "system":  # Ignorar mensajes del sistema
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Renderizar el campo de entrada
    if prompt := frontend.render_input():
        # Agregar el mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Crear un cliente de OpenAI
        client = OpenAI(api_key=openai_api_key)

        # Generar una respuesta usando OpenAI
        # Generar una respuesta usando OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            temperature=0.2
        )

        # Capturar y procesar la respuesta del asistente
        response_content = response.choices[0].message.content  # Acceder al atributo directamente
        with st.chat_message("assistant"):
            st.markdown(response_content)
        st.session_state.messages.append({"role": "assistant", "content": response_content})