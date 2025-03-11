from io import BytesIO
from fpdf import FPDF
import streamlit as st
import os

def generar_pdf(messages):
    pdf = FPDF()
    pdf.add_page()

    # Configuración de fuentes (sin cambios)
    font_path = os.path.abspath("fonts/DejaVuSans.ttf")
    bold_font_path = os.path.abspath("fonts/DejaVuSans-Bold.ttf")

    fuentes_cargadas = False
    if os.path.exists(font_path) and os.path.exists(bold_font_path):
        try:
            pdf.add_font("DejaVu", "", font_path, uni=True)
            pdf.add_font("DejaVu", "B", bold_font_path, uni=True)
            pdf.set_font("DejaVu", size=12)
            fuentes_cargadas = True
        except Exception as e:
            st.warning(f"⚠️ Error cargando fuentes: {e}")

    if not fuentes_cargadas:
        st.warning("⚠️ Usando Arial como predeterminado.")
        pdf.set_font("Arial", size=12)

    # Generar contenido del PDF (sin cambios)
    pdf.cell(0, 10, txt="Clases particulares La Pampa", ln=True, align="C")
    pdf.ln(20)

    for message in messages:
        role = "Usuario" if message["role"] == "user" else "Profesor"
        pdf.set_font("DejaVu" if fuentes_cargadas else "Arial", style="B" if message["role"] == "user" else "", size=12)
        pdf.multi_cell(0, 10, txt=f"{role}: {message['content']}")

    # Guardar el contenido del PDF como bytes en BytesIO
    pdf_output = BytesIO()
    pdf_content = pdf.output(dest="S") # Dest="S" devuelve el contenido en bytes
    pdf_output.write(pdf_content)
    pdf_output.seek(0)  # Reiniciar el puntero al inicio del archivo
    return pdf_output

def renderizar_boton_descarga(messages):
    pdf_buffer = generar_pdf(messages)
    st.sidebar.download_button(
        label="Descargar conversación",
        data=pdf_buffer,
        file_name="chat_con_profesor.pdf",
        mime="application/pdf"
    )
