import streamlit as st
from openai import OpenAI

# Archivos de instrucciones del sistema
INSTRUCTIONS_FILES = {
    "inversiones": "instructions_inversiones.txt",
    "comercio_exterior": "instructions_comercio_exterior.txt",
}

# Obtener clave API de secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Inicializar variables en st.session_state
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "initial_message_shown" not in st.session_state:
    st.session_state.initial_message_shown = False

# Mostrar título principal
st.title("💬 Sofía, Asistente Virtual de la Agencia I-COMEX")

# Si no se ha seleccionado un tema, mostrar botones
if st.session_state.selected_topic is None:
    # Descripción inicial y botones de selección
    st.write(
        "Sofía, el agente de IA de la Agencia I-COMEX, está diseñada para responder tus preguntas sobre comercio exterior e inversiones en La Pampa. "
        "Obtené más información sobre la Agencia I-COMEX en su [sitio web oficial](https://icomexlapampa.org/es/)."
    )
    st.write("¿Sobre qué tema necesitas ayuda?")
    col1, col2 = st.columns(2)
    if col1.button("Oportunidades de Inversión"):
        st.session_state.selected_topic = "inversiones"
        st.session_state.initial_message = (
            "¡Hola! Soy Sofía, la asistente virtual de I-COMEX 😊. "
            "Parece que te interesan las oportunidades de inversión en La Pampa. "
            "Decime, ¿hay algo en particular que quisieras saber?"
        )
    if col2.button("Exportación de Servicios"):
        st.session_state.selected_topic = "comercio_exterior"
        st.session_state.initial_message = (
            "¡Hola! Soy Sofía, la asistente virtual de I-COMEX 😊. "
            "¿Estás planificando exportar tus servicios? "
            "Contame un poco más sobre lo que te gustaría saber."
        )
    # Detener la ejecución aquí si no se ha seleccionado un tema
    st.stop()

# Continuar solo si el tema está seleccionado
selected_topic = st.session_state.selected_topic

# Mostrar título según la temática seleccionada
if selected_topic == "inversiones":
    st.subheader("Oportunidades de Inversión")
elif selected_topic == "comercio_exterior":
    st.subheader("Exportación de Servicios")

# Leer el archivo de instrucciones correspondiente
try:
    with open(INSTRUCTIONS_FILES[selected_topic], "r", encoding="utf-8") as file:
        system_instructions = file.read().strip()
except FileNotFoundError:
    st.error(f"No se encontró el archivo de instrucciones para {selected_topic}.")
    system_instructions = None

# Agregar mensaje del sistema y mensaje inicial si no se han mostrado
if not st.session_state.initial_message_shown:
    if system_instructions:
        st.session_state.messages.append({"role": "system", "content": system_instructions})
    st.session_state.messages.append({"role": "assistant", "content": st.session_state.initial_message})
    st.session_state.initial_message_shown = True

# Renderizar todos los mensajes en orden
for message in st.session_state.messages:
    if message["role"] != "system":  # Ignorar mensajes del sistema
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Campo de entrada para el usuario
if prompt := st.chat_input("Contame en qué te puedo ayudar..."):
    # Agregar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Crear un cliente de OpenAI
    client = OpenAI(api_key=openai_api_key)

    # Generar una respuesta usando OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages,
        stream=True,
        temperature=0.2
    )

    # Mostrar la respuesta y guardarla en el estado de la sesión
    with st.chat_message("assistant"):
        response_content = st.write_stream(response)
    st.session_state.messages.append({"role": "assistant", "content": response_content})
