import streamlit as st
from models.gpt_integration import generate_response
from audio_to_text import transcribe_audio

st.set_page_config(page_title="Diego - Seus assistente de compras online", layout="wide")

# CSS para estilizar estilo whatssap
st.markdown("""
    <style>
    body {
        background-color: #ece5dd;
        font-family: Arial, sans-serif;
    }
    .stApp {
        background-color: #ece5dd;
    }
    .chat-container {
        max-width: 600px;
        margin: auto;
        background: #fff;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
    }
    .chat-header {
        background-color: #075e54;
        color: white;
        padding: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px 10px 0 0;
    }
    .chat-box {
        height: 400px;
        overflow-y: auto;
        padding: 10px;
        background: #ece5dd;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #dcf8c6;
        color: black;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        text-align: right;
        max-width: 80%;
        align-self: flex-end;
    }
    .bot-message {
        background-color: white;
        color: black;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        text-align: left;
        max-width: 80%;
        align-self: flex-start;
    }
    .stTextArea textarea {
        border-radius: 20px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #25d366;
        color: white;
        border-radius: 20px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-header">🤖 Diego - Seus assistente de compras online</div>', unsafe_allow_html=True)


uploaded_file = st.file_uploader("Envie um áudio", type=["wav", "mp3", "ogg"])
user_input = st.text_area("Ou digite sua pergunta:")

if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")
    with st.spinner("Transcrevendo áudio..."):
        user_input = transcribe_audio(uploaded_file)
        st.markdown(f'<div class="user-message">📝 Texto extraído: {user_input}</div>', unsafe_allow_html=True)

if st.button("Enviar"):
    if user_input:
        with st.spinner("Gerando resposta..."):
            response = generate_response(user_input)
            st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="bot-message">{response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Por favor, envie um áudio ou digite uma pergunta.")

st.markdown('</div>', unsafe_allow_html=True)
