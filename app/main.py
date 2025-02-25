import streamlit as st
from models.gpt_integration import generate_response
from audio_to_text import transcribe_audio
 
st.set_page_config(page_title="Chatbot GPT", layout="wide")

st.title("🤖 Chatbot de Produtos")

uploaded_file = st.file_uploader("Envie um áudio", type=["wav", "mp3", "ogg"])
user_input = st.text_area("Ou digite sua pergunta:")

if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")
    with st.spinner("Transcrevendo áudio..."):
        user_input = transcribe_audio(uploaded_file)
        st.write(f"📝 Texto extraído: {user_input}")

if st.button("Enviar"):
    if user_input:
        with st.spinner("Gerando resposta..."):
            response = generate_response(user_input)
            st.write(response)
    else:
        st.warning("Por favor, envie um áudio ou digite uma pergunta.")
