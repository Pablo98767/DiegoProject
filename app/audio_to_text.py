import speech_recognition as sr

def transcribe_audio(audio_file):
    """Converte áudio para texto usando SpeechRecognition"""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        return text
    except sr.UnknownValueError:
        return "Não foi possível entender o áudio."
    except sr.RequestError:
        return "Erro ao conectar com o serviço de reconhecimento de voz."
