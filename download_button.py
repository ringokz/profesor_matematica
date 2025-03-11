from io import BytesIO
from fpdf import FPDF
import os
import streamlit as st

# Función para generar el archivo PDF
def generar_pdf(messages):
    pdf = FPDF()
    pdf.add_page()

    # Verificar si las fuentes existen antes de agregarlas
    font_path = "fonts/DejaVuSans.ttf"
    bold_font_path = "fonts/DejaVuSans-Bold.ttf"

    if os.path.exists(font_path) and os.path.exists(bold_font_path):
        pdf.add_font('DejaVu', '', font_path, uni=True)
        pdf.add_font('DejaVu', 'B', bold_font_path, uni=True)
    else:
        st.warning("⚠️ Fuentes no encontradas. Usando Arial como predeterminado.")
        pdf.set_font("Arial", size=12)

    # Logo
    pdf.image("logs/front-log.png", x=10, y=8, w=30)

    # Título
    pdf.set_font("Arial", style="BU", size=24)
    pdf.set_text_color(70, 130, 180)
    pdf.set_xy(10, 50)
    pdf.cell(0, 10, txt="Clases particulares La Pampa", ln=True, align="C")
    pdf.ln(20)

    # Mensajes
    for message in messages:
        if message["role"] == "user":
            pdf.set_font("Arial", style="B", size=12)
            pdf.set_text_color(0, 0, 230)
            role = "Usuario"
            avatar_path = "logs/user_avatar.png"
        else:
            pdf.set_font("Arial", size=12)
            pdf.set_text_color(10, 10, 10)
            role = "Profesor"
            avatar_path = "logs/front-log.png"

        # Avatar
        pdf.image(avatar_path, x=10, y=pdf.get_y(), w=10, h=10)
        pdf.set_xy(25, pdf.get_y())
       
        try:
            pdf.multi_cell(0, 10, txt=f"{role}: {message['content'][:1000]}")
        except Exception as e:
            st.error(f"Error procesando el mensaje: {e}")
            pdf.multi_cell(0, 10, txt=f"{role}: [Mensaje no pudo ser procesado]")

    # Guardar el PDF en memoria
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest="S"))  # Usar encoding compatible
    pdf_output.seek(0)
    return pdf_output

# Función para mostrar el botón de descarga
def renderizar_boton_descarga(messages):
    pdf_buffer = generar_pdf(messages)
    st.sidebar.download_button(
        label="Descargar conversación",
        data=pdf_buffer,
        file_name="chat_con_profesor.pdf",
        mime="application/pdf"
    )
