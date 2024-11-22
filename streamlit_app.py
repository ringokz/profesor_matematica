import streamlit as st
import frontend
from openai import OpenAI
from PIL import Image

# Configuración de la página
SOFIA_LOGO_PATH = "logos/sofia avatar.png"
USER_LOGO_PATH = "logos/user avatar.png"
st.set_page_config(page_title="Sofía - Asistente de IA", layout="centered", page_icon=SOFIA_LOGO_PATH)

# Inicializar estilos personalizados
frontend.render_custom_styles()

# Cachear las imágenes
@st.cache_data
def load_image(image_path):
    return Image.open(image_path)

sofia_logo = load_image(SOFIA_LOGO_PATH)
user_logo = load_image(USER_LOGO_PATH)

# Inicialización del estado
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "initial_message_shown" not in st.session_state:
    st.session_state.initial_message_shown = False
if "subtitle_shown" not in st.session_state:
    st.session_state.subtitle_shown = False
if "rendered_message_ids" not in st.session_state:
    st.session_state.rendered_message_ids = set()  # Para rastrear mensajes ya renderizados

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

# Renderizar el encabezado (siempre visible)
frontend.render_title()

# Renderizar subtítulo dinámico basado en el tema seleccionado
if st.session_state.selected_topic:
    if not st.session_state.subtitle_shown:
        frontend.render_subheader(st.session_state.selected_topic)
        st.session_state.subtitle_shown = True
    else:
        st.subheader(st.session_state.selected_topic.capitalize())

# Renderizar la introducción y botones solo si no se ha seleccionado un tema
if st.session_state.selected_topic is None:
    frontend.render_intro()

# Mostrar chat y mensajes si se seleccionó un tema
if st.session_state.selected_topic:
    # Cargar las instrucciones del sistema solo una vez
    if not st.session_state.initial_message_shown:
        instructions = load_instructions(st.session_state.selected_topic)
        if instructions:
            st.session_state.messages.append({"role": "system", "content": instructions})
        st.session_state.messages.append({"role": "assistant", "content": st.session_state.initial_message})
        st.session_state.initial_message_shown = True

    # Renderizar mensajes existentes
    for i, message in enumerate(st.session_state.messages):
        if message["role"] != "system":
            message_id = f"{message['role']}-{i}"
            if message_id not in st.session_state.rendered_message_ids:
                if message["role"] == "assistant":
                    # Renderizar dinámicamente los nuevos mensajes del asistente con avatar
                    frontend.render_dynamic_message(message, avatar=sofia_logo)
                else:
                    # Renderizar estáticamente los mensajes del usuario con avatar
                    frontend.render_chat_message(message["role"], message["content"], avatar=user_logo)
                # Marcar el mensaje como renderizado
                st.session_state.rendered_message_ids.add(message_id)
            else:
                # Mostrar mensajes ya renderizados
                frontend.render_chat_message(message["role"], message["content"], 
                                             avatar=sofia_logo if message["role"] == "assistant" else user_logo)

    # Renderizar el campo de entrada
    if prompt := frontend.render_input():
        # Agregar el mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        frontend.render_chat_message("user", prompt, avatar=user_logo)

        # Crear un cliente de OpenAI
        client = OpenAI(api_key=openai_api_key)

        # Generar una respuesta usando OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            temperature=0
        )

        # Capturar y procesar la respuesta del asistente
        response_content = response.choices[0].message.content
        response_message = {"role": "assistant", "content": response_content}
        st.session_state.messages.append(response_message)

        # Renderizar dinámicamente la nueva respuesta del asistente
        frontend.render_dynamic_message(response_message, avatar=sofia_logo)
        # Marcar el mensaje como renderizado
        st.session_state.rendered_message_ids.add(f"assistant-{len(st.session_state.messages) - 1}")
