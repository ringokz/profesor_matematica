import streamlit as st
from openai import OpenAI

# Archivos de instrucciones del sistema
INSTRUCTIONS_FILES = {
    "inversiones": "instructions_inversiones.txt",
    "comercio_exterior": "instructions_comercio_exterior.txt",
}

def normalize_messages(messages):
    """Normaliza los mensajes para garantizar codificación UTF-8."""
    normalized = []
    for message in messages:
        normalized_message = {key: value.encode("utf-8").decode("utf-8") if isinstance(value, str) else value
                              for key, value in message.items()}
        normalized.append(normalized_message)
    return normalized

# Mostrar título y descripción
st.title("💬 Sofía, Asistente Virtual de la Agencia I-COMEX")
st.write(
    "Sofía, el agente de IA de la Agencia I-COMEX, está diseñada para responder tus preguntas sobre comercio exterior e inversiones en La Pampa. "
    "Obtené más información sobre la Agencia I-COMEX en su [sitio web oficial](https://icomexlapampa.org/es/)."
)

# Elección inicial del tema
if "selected_topic" not in st.session_state:
    st.write("¿Sobre qué tema necesitas ayuda?")
    col1, col2 = st.columns(2)
    if col1.button("Oportunidades de Inversión"):  # Botón modificado
        st.session_state.selected_topic = "inversiones"
    if col2.button("Exportación de Servicios"):  # Botón modificado
        st.session_state.selected_topic = "comercio_exterior"

# Continuar solo si el tema está seleccionado
if "selected_topic" in st.session_state:
    selected_topic = st.session_state.selected_topic

    # Leer el archivo de instrucciones correspondiente
    try:
        with open(INSTRUCTIONS_FILES[selected_topic], "r", encoding="utf-8") as file:
            system_instructions = file.read().strip()
    except FileNotFoundError:
        st.error(f"No se encontró el archivo de instrucciones para {selected_topic}.")
        system_instructions = None

    # Pedir al usuario su clave de API
    openai_api_key = st.text_input("Código Secreto Agencia I-COMEX", type="password")
    if not openai_api_key:
        st.info("Pegá acá el código que Lauti te pasó para poder continuar.", icon="🗝️")
    else:
        # Crear un cliente de OpenAI
        client = OpenAI(api_key=openai_api_key.encode("utf-8").decode("utf-8"))

        # Inicializar los mensajes en `st.session_state`, incluyendo el mensaje del sistema
        if "messages" not in st.session_state:
            st.session_state.messages = []
            if system_instructions:
                st.session_state.messages.append({"role": "system", "content": system_instructions})

        # Mostrar solo los mensajes que no son del sistema
        for message in st.session_state.messages:
            if message["role"] != "system":
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Crear un campo de entrada para que el usuario envíe mensajes
        if prompt := st.chat_input("Contame en qué te puedo ayudar..."):
            # Guardar y mostrar el mensaje del usuario
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generar una respuesta usando la API de OpenAI
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=normalize_messages(st.session_state.messages),
                stream=True,
                temperature=0.2
            )

            # Mostrar la respuesta y guardarla en el estado de la sesión
            with st.chat_message("assistant"):
                response_content = st.write_stream(response)
            st.session_state.messages.append({"role": "assistant", "content": response_content})
