from io import BytesIO
from fpdf import FPDF
import streamlit as st

# Función para generar el archivo PDF
def generar_pdf(messages):
    pdf = FPDF()
    pdf.add_page()

    # Agregar la fuente personalizada (asegúrate que existan estos archivos)
    pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf', uni=True)


    # Logo
    pdf.image("logs/front-log.png", x=10, y=8, w=30)

    # Título
    pdf.set_font("DejaVu", style="BU", size=24)
    pdf.set_text_color(70, 130, 180)
    pdf.set_xy(10, 50)
    pdf.cell(0, 10, txt="Clases particulares La Pampa", ln=True, align="C")
    pdf.ln(20)

    # Mensajes
    for message in messages:
        if message["role"] == "user":
            pdf.set_font("DejaVu", style="B", size=12)
            pdf.set_text_color(0, 0, 230)
            role = "Usuario"
            avatar_path = "logs/user_avatar.png"
        else:
            pdf.set_font("DejaVu", size=12)
            pdf.set_text_color(10, 10, 10)
            role = "Profesor"
            avatar_path = "logs/front-log.png"

        # Avatar
        pdf.image(avatar_path, x=10, y=pdf.get_y(), w=10, h=10)
        pdf.set_xy(25, pdf.get_y())
       
        try:
            pdf.multi_cell(pdf.w - 40, 10, txt=f"{role}: {message['content'][:1000]}") 
        except IndexError as e:
            print(f"Error procesando el mensaje: {message['content']} -> {e}")
            pdf.multi_cell(0, 10, txt=f"{role}: [Mensaje no pudo ser procesado]")
            
    # Guardar el PDF en memoria sin codificación extra
    pdf_output = BytesIO()
    pdf_bytes = pdf.output(dest="S")  # Codificación compatible con Unicode
    pdf_output.write(pdf_bytes)
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
