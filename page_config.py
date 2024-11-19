import streamlit as st

# Set page configuration
def configure_page():
    st.set_page_config(page_title="Sofía - Asistente Virtual I-COMEX", page_icon="💬", layout="centered")

    PRIMARY_COLOR = "#4a83c0"
    SECONDARY_COLOR = "#878889"
    BACKGROUND_COLOR = "#f4f5f7"
    FONT_FAMILY = "Fira Sans"

    # Custom CSS styles
    st.markdown(f"""
        <style>
            body {{
                background-color: {BACKGROUND_COLOR};
                color: {SECONDARY_COLOR};
                font-family: '{FONT_FAMILY}', sans-serif;
            }}
            .stApp {{
                background-color: {BACKGROUND_COLOR};
            }}
            .header {{
                background-color: {PRIMARY_COLOR};
                padding: 20px;
                border-radius: 10px;
                text-align: center;
            }}
            .header img {{
                max-width: 300px;
            }}
            .header h1 {{
                color: white;
                font-size: 32px;
                margin: 0;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Header with logo and title
    st.markdown("""
        <div class="header">
            <img src="horizontal_logo.png" alt="Logo I-COMEX">
            <h1>Sofía - Asistente Virtual de I-COMEX</h1>
        </div>
    """, unsafe_allow_html=True)
