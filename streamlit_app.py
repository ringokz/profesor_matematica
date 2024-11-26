import streamlit as st
import frontend
from openai import OpenAI
from PIL import Image
import sidebar

# Configuración de la página
PRIMARY_COLOR = "#4b83c0"
SECONDARY_COLOR = "#878889"
BACKGROUND_COLOR = "#ffffff"  # Changed background to white

ICOMEX_LOGO_PATH = "logos/ICOMEX_Logos sin fondo.png"
SOFIA_AVATAR_PATH = "logos/sofia_avatar.png"
USER_LOGO_PATH = "logos/user_avatar.png"
st.set_page_config(page_title="SofIA - Asesora Virtual", layout="centered", page_icon=SOFIA_AVATAR_PATH)

# Inicializar estilos personalizados
frontend.render_custom_styles()

# Cachear las imágenes
@st.cache_data
def load_image(image_path):
    return Image.open(image_path)

sofia_logo = load_image(SOFIA_AVATAR_PATH)
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
    st.session_state.rendered_message_ids = set()
if "show_form" not in st.session_state:
    st.session_state.show_form = False

# Renderizar el encabezado (siempre visible)
frontend.render_title()

# Sidebar with a button to toggle form
with st.sidebar:
    if st.session_state.selected_topic:
        if st.button("Enviar conversación por correo"):
            st.session_state.show_form = True

# Render the form if enabled
if st.session_state.show_form:
    sidebar.save_conversation_form()

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
        instructions = sidebar.load_instructions(st.session_state.selected_topic)
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
                    frontend.render_dynamic_message(message, avatar=sofia_logo)
                else:
                    frontend.render_chat_message(message["role"], message["content"], avatar=user_logo)
                st.session_state.rendered_message_ids.add(message_id)
            else:
                frontend.render_chat_message(message["role"], message["content"],
                                             avatar=sofia_logo if message["role"] == "assistant" else user_logo)

    # Renderizar el campo de entrada
    if prompt := frontend.render_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        frontend.render_chat_message("user", prompt, avatar=user_logo)

        client = OpenAI(api_key=st.secrets["openai"]["api_key"])
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            temperature=0
        )
        response_content = response.choices[0].message.content
        response_message = {"role": "assistant", "content": response_content}
        st.session_state.messages.append(response_message)
        frontend.render_dynamic_message(response_message, avatar=sofia_logo)
        st.session_state.rendered_message_ids.add(f"assistant-{len(st.session_state.messages) - 1}")
