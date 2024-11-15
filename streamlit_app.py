import streamlit as st
from openai import OpenAI

# [MODIFICACIÓN] Lectura del archivo con las instrucciones del sistema.
try:
    with open("system_instructions.txt", "r") as file:
        system_instructions = file.read().strip()  # Leer y limpiar el contenido del archivo.
except FileNotFoundError:
    st.error("El archivo 'system_instructions.txt' no se encontró. Por favor, asegúrate de que esté en el directorio.")
    system_instructions = None

# Mostrar título y descripción.
st.title("💬 Sofía, Asistente Virtual de la Agencia I-COMEX")
st.write(
    "Sofía, el agente de IA de la Agencia I-COMEX, está diseñada para responder tus preguntas sobre comercio exterior e inversiones en La Pampa. "
    "Obtené más información sobre la Agencia I-COMEX en su [sitio web oficial](https://icomexlapampa.org/es/)."
)

# Pedir al usuario su clave de API.
openai_api_key = st.text_input("Código Secreto Agencia I-COMEX", type="password")
if not openai_api_key:
    st.info("Pegá acá el código que Lauti te pasó para poder continuar.", icon="🗝️")
else:
    # Crear un cliente de OpenAI.
    client = OpenAI(api_key=openai_api_key)

    # [MODIFICACIÓN] Inicializar los mensajes en `st.session_state`, incluyendo el mensaje del sistema.
    if "messages" not in st.session_state:
        st.session_state.messages = []
        if system_instructions:
            st.session_state.messages.append({"role": "system", "content": system_instructions})

    # [MODIFICACIÓN] Mostrar solo los mensajes que no son del sistema.
    for message in st.session_state.messages:
        if message["role"] != "system":  # Ignorar mensajes del sistema.
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Crear un campo de entrada para que el usuario envíe mensajes.
    if prompt := st.chat_input("Contame en qué te puedo ayudar..."):
        # Guardar y mostrar el mensaje del usuario.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar una respuesta usando la API de OpenAI.
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,  # [MODIFICACIÓN] Se envían todos los mensajes, incluyendo el del sistema.
            stream=True,
            temperature=0.2
        )

        # Mostrar la respuesta y guardarla en el estado de la sesión.
        with st.chat_message("assistant"):
            response_content = st.write_stream(response)
        st.session_state.messages.append({"role": "assistant", "content": response_content})
