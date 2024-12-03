import streamlit as st
import frontend
from openai import OpenAI
from PIL import Image
import sidebar
import tempfile
from sidebar import clean_message_for_audio
from elevenlabs import ElevenLabs

# Configuración de la página
PRIMARY_COLOR = "#4b83c0"
SECONDARY_COLOR = "#878889"
BACKGROUND_COLOR = "#ffffff"

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
        sidebar.toggle_audio_button()  # Llama a la función para el botón
    if st.session_state.selected_topic:
        if st.button("Enviar conversación por correo"):
            st.session_state.show_form = True

# Render the form if enabled
if st.session_state.show_form:
    sidebar.save_conversation_form()

def generar_audio_elevenlabs_sdk(texto, voice_id="1BxAZWANeDIxeyHKSJF2"):
    try:
        # Inicializa el cliente de ElevenLabs con la clave API
        client = ElevenLabs(api_key=st.secrets["elevenlabs"]["api_key"])

        # Generar el audio usando el SDK
        audio_generator = client.text_to_speech.convert(
            voice_id=voice_id,
            model_id="eleven_turbo_v2_5",
            text=texto,
            voice_settings={
                "stability": 1,
                "similarity_boost": 1
            }
        )

        # Guardar el audio en un archivo temporal
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        with open(temp_audio.name, "wb") as f:
            for chunk in audio_generator:  # Iterar sobre el generador
                f.write(chunk)

        return temp_audio.name

    except Exception as e:
        st.error(f"Error al generar audio: {e}")
        return None

# Renderizar subtítulo dinámico basado en el tema seleccionado
if st.session_state.selected_topic:
    if not st.session_state.subtitle_shown:
        frontend.render_subheader(st.session_state.selected_topic)
        st.session_state.subtitle_shown = True
    else:
        st.subheader(st.session_state.selected_topic)

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
    # if prompt := frontend.render_input():
    #     st.session_state.messages.append({"role": "user", "content": prompt})
    #     frontend.render_chat_message("user", prompt, avatar=user_logo)

    #     client = OpenAI(api_key=st.secrets["openai"]["api_key"])
    #     response = client.chat.completions.create(
    #         model="gpt-4o-mini",
    #         messages=st.session_state.messages,
    #         temperature=0.3,       
    #         top_p=0.1,             
    #         frequency_penalty=0.2, 
    #         presence_penalty=0.2   
    #     )

    #     response_content = response.choices[0].message.content
    #     response_message = {"role": "assistant", "content": response_content}
    #     st.session_state.messages.append(response_message)

    #     # Renderizar el mensaje del chatbot
    #     frontend.render_dynamic_message(response_message, avatar=sofia_logo)
    #     st.session_state.rendered_message_ids.add(f"assistant-{len(st.session_state.messages) - 1}")

    #     # Generar y reproducir audio
    #     if st.session_state.audio_enabled:
    #         # Limpiar el texto antes de enviarlo a Eleven Labs
    #         texto_limpio = clean_message_for_audio(response_content)
    #         audio_path = generar_audio_elevenlabs_sdk(texto_limpio)
    #         if audio_path:
    #             st.audio(audio_path, format="audio/mp3")

    # Define settings for each topic
    TOPIC_CONFIG = {
        "¡Quiero exportar!": {
            "model": "gpt-4o-mini",
            "temperature": 0.3,
            "top_p": 0.1,
            "frequency_penalty": -0.5,
            "presence_penalty": -0.5,
        },
        "Oportunidades de Inversión": {
            "model": "gpt-4o-mini",
            "temperature": 0.3,
            "top_p": 0.1,
            "frequency_penalty": 0.2,
            "presence_penalty": 0.2,
        },
        "default": {
            "model": "gpt-4o-mini",
            "temperature": 0.3,
            "top_p": 0.1,
            "frequency_penalty": 0.2,
            "presence_penalty": 0.2,
        }
    }

    # Select configuration based on topic
    selected_topic = st.session_state.selected_topic
    if selected_topic in TOPIC_CONFIG:
        config = TOPIC_CONFIG[selected_topic]
    else:
        config = TOPIC_CONFIG["default"]

    # Render input and process response
    if prompt := frontend.render_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        frontend.render_chat_message("user", prompt, avatar=user_logo)

        # Set the bot thinking state to True
        st.session_state.is_thinking = True

        # OpenAI API call using the selected configuration
        client = OpenAI(api_key=st.secrets["openai"]["api_key"])
        response = client.chat.completions.create(
            model=config["model"],
            messages=st.session_state.messages,
            temperature=config["temperature"],
            top_p=config["top_p"],
            frequency_penalty=config["frequency_penalty"],
            presence_penalty=config["presence_penalty"],
        )

        # Extract response content and render
        response_content = response.choices[0].message.content
        response_message = {"role": "assistant", "content": response_content}
        st.session_state.messages.append(response_message)

        frontend.render_dynamic_message(response_message, avatar=sofia_logo)
        st.session_state.rendered_message_ids.add(f"assistant-{len(st.session_state.messages) - 1}")

        # Set the bot thinking state back to False
        st.session_state.is_thinking = False

        # Generate and play audio if enabled
        if st.session_state.audio_enabled:
            texto_limpio = clean_message_for_audio(response_content)
            audio_path = generar_audio_elevenlabs_sdk(texto_limpio)
            if audio_path:
                st.audio(audio_path, format="audio/mp3")