import streamlit as st
from openai import OpenAI
from PIL import Image
import frontend
import uuid
import download_button


# Configuración inicial
st.set_page_config(
    page_title="Albert - Asesor de Matemáticas",
    layout="centered",
    page_icon="logs/front-log.webp"
)

# Inicializar estado
if "messages" not in st.session_state:
    st.session_state.messages = []
if "rendered_message_ids" not in st.session_state:
    st.session_state.rendered_message_ids = set()
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Cachear imágenes y textos
@st.cache_data
def load_image(path):
    return Image.open(path)

@st.cache_data
def cargar_texto(path):
    with open(path, "r", encoding="utf-8") as archivo:
        return archivo.read()

# Cargar instrucciones y contenido base
MATH_INSTRUCTIONS = cargar_texto("math_instructions.md")
PRELIMINARES_MATEMATICA = cargar_texto("preliminares_matematica.md")

# Cargar avatares
albert_logo = load_image("logs/agente-albert-avatar.png")
user_logo = load_image("logs/user_avatar.png")

# Mostrar el botón de descarga en la parte superior izquierda
if "messages" in st.session_state and st.session_state.messages:
    col1, col2 = st.columns([1, 4])
    with col1:
        download_button.renderizar_boton_descarga(st.session_state.messages)
    with col2:
        pass

frontend.render_custom_styles()
frontend.render_title()
frontend.render_intro()

# Mostrar mensajes existentes
for i, message in enumerate(st.session_state.messages):
    message_id = f"{message['role']}-{i}"
    if message_id not in st.session_state.rendered_message_ids:
        avatar = albert_logo if message["role"] == "assistant" else user_logo
        frontend.render_chat_message(message["role"], message["content"], avatar=avatar)
        st.session_state.rendered_message_ids.add(message_id)


def validar_respuesta_matematica(respuesta):
    # Permitir respuestas no matemáticas
    if "$" not in respuesta and "$$" not in respuesta:
        return respuesta  # Respuesta no matemática permitida
    return respuesta  # Formato válido



# Input para enviar mensajes
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Mostrar y guardar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    frontend.render_chat_message("user", prompt, avatar=user_logo)

    # Crear contexto inicial con instrucciones y contenido del libro
    contexto_inicial = [
        {"role": "system", "content": "Es OBLIGATORIO que EVITES utilizar texto plano para las operaciones matemáticas y SIEMPRE debas usar formato LaTeX. Por ejemplo, $x^2 + 2x + 1 = 0$. Devuelve las ecuaciones matemáticas según las reglas establecidas."},
        {"role": "system", "content": MATH_INSTRUCTIONS},
        {"role": "assistant", "content": PRELIMINARES_MATEMATICA},
    ]

    # Combinar contexto inicial con los mensajes previos
    mensajes_completos = contexto_inicial + st.session_state.messages

    # Obtener respuesta del asistente
    client = OpenAI(api_key=st.secrets["openai"]["api_key"])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensajes_completos,
        temperature=0.3,
        top_p=0.1,
        frequency_penalty=0.2,
        presence_penalty=0.2,
    )
    response_content = validar_respuesta_matematica(response.choices[0].message.content)

    # Mostrar y guardar la respuesta del asistente
    assistant_message = {"role": "assistant", "content": response_content}
    st.session_state.messages.append(assistant_message)
    frontend.render_dynamic_message(assistant_message, avatar=albert_logo)
