import requests
import json
from data.aws_s3 import get_products_from_s3
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

API_KEY = os.getenv("API_KEY")

def generate_response(user_input):
    """Gera uma resposta baseada nos produtos armazenados no S3"""
    
    try:
        # Obtendo os dados do S3
        products_data = get_products_from_s3()
        if not products_data:
            return "Desculpe, não consegui obter dados de produtos."
        
        print("Dados de produtos obtidos com sucesso.")

        # Limitar a quantidade de produtos no prompt
        products_data = products_data[:100]  # Limita a 100 produtos (ajuste conforme necessário)

        # Construção do prompt
        prompt = f"""
        Você é um assistente especializado em produtos. Aqui está a lista de produtos disponíveis:
        
        {products_data}

        Agora, responda da forma mais útil e detalhada possível para a seguinte pergunta do usuário:
        {user_input}
        """

        print("Prompt criado com sucesso:", prompt)

        # Criando a requisição para o OpenRouter
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "google/gemini-2.0-flash-lite-preview-02-05:free",  # Modelo do Google Gemini
                "messages": [
                    {
                        "role": "system",
                        "content": "Você é um especialista em produtos."
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt  # Usando o prompt construído
                            }
                        ]
                    }
                ]
            })
        )

        print("Requisição criada com sucesso.")
        print("Status da resposta:", response.status_code)
        print("Resposta da API:", response.text)  # Log detalhado da resposta

        # Verificando a resposta
        if response.status_code == 200:
            completion = response.json()
            if completion.get("choices") and completion["choices"][0].get("message", {}).get("content"):
                return completion["choices"][0]["message"]["content"]
            else:
                return "❌ Não foi possível gerar uma resposta (estrutura da resposta inválida)"
        else:
            return f"⛔ Erro na requisição: {response.status_code} - {response.text}"
    
    except Exception as e:
        return f"⛔ Erro crítico: {str(e)}"

# Exemplo de uso
user_input = "Quais são os produtos mais populares?"
response = generate_response(user_input)
print(response)
