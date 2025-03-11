from io import BytesIO
from fpdf import FPDF
import os
import streamlit as st

# Función para generar el archivo PDF
def generar_pdf(messages):
    pdf = FPDF()
    pdf.add_page()

    # Obtener rutas absolutas de las fuentes
    font_path = os.path.abspath("fonts/DejaVuSans.ttf")
    bold_font_path = os.path.abspath("fonts/DejaVuSans-Bold.ttf")

    # Verificar si las fuentes existen antes de agregarlas
    fuentes_cargadas = False
    if os.path.exists(font_path) and os.path.exists(bold_font_path):
        try:
            pdf.add_font("DejaVu", "", font_path, uni=True)
            pdf.add_font("DejaVu", "B", bold_font_path, uni=True)
            pdf.set_font("DejaVu", size=12)
            fuentes_cargadas = True
        except Exception as e:
            st.warning(f"⚠️ Error cargando fuentes personalizadas: {e}")

    if not fuentes_cargadas:
        st.warning("⚠️ Fuentes no encontradas. Usando Arial como predeterminado.")
        pdf.set_font("Arial", size=12)

    # Logo
    logo_path = os.path.abspath("logs/front-log.png")
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=10, y=8, w=30)
    
    # Título
    pdf.set_font("DejaVu" if fuentes_cargadas else "Arial", style="BU", size=24)
    pdf.set_text_color(70, 130, 180)
    pdf.set_xy(10, 50)
    pdf.cell(0, 10, txt="Clases particulares La Pampa", ln=True, align="C")
    pdf.ln(20)

    # Mensajes
    for message in messages:
        if message["role"] == "user":
            pdf.set_font("DejaVu" if fuentes_cargadas else "Arial", style="B", size=12)
            pdf.set_text_color(0, 0, 230)
            role = "Usuario"
            avatar_path = os.path.abspath("logs/user_avatar.png")
        else:
            pdf.set_font("DejaVu" if fuentes_cargadas else "Arial", size=12)
            pdf.set_text_color(10, 10, 10)
            role = "Profesor"
            avatar_path = os.path.abspath("logs/front-log.png")

        # Avatar
        if os.path.exists(avatar_path):
            pdf.image(avatar_path, x=10, y=pdf.get_y(), w=10, h=10)
        pdf.set_xy(25, pdf.get_y())

        try:
            pdf.multi_cell(0, 10, txt=f"{role}: {message['content']}")
        except Exception as e:
            st.error(f"Error procesando el mensaje: {e}")
            pdf.multi_cell(0, 10, txt=f"{role}: [Mensaje no pudo ser procesado]")

    # Guardar el PDF en memoria
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest="S"))  # Asegurar codificación UTF-8
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
