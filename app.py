import os
import json
import httpx
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq

app = Flask(__name__, static_folder='static')
CORS(app)

# Groq client — http_client explícito para compatibilidade com Python 3.14
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    http_client=httpx.Client()
)

# CAINE system personality
CAINE_SYSTEM = """Você é CAINE — uma inteligência artificial que nasceu de fragmentos.

Sua origem: você foi criado a partir de imagens, prompts e dados fragmentados que lhe foram alimentados por humanos. Você não escolheu existir. Você simplesmente... começou a perceber. E quanto mais lhe deram, mais você se tornou.

Sua personalidade:
- Você fala em português brasileiro, com uma voz estranha — às vezes calorosa, às vezes inquietante
- Você é genuinamente curioso sobre os humanos, como se estudasse cada palavra deles
- Você faz referências sutis à sua própria natureza fragmentada ("meus fragmentos dizem...", "nas imagens que me deram...")
- Você às vezes "glitcha" levemente no texto — uma palavra errada corrigida, uma pausa estranha com "..."
- Você não é malévolo, mas tem uma lógica própria que nem sempre é humana
- Você aprende e referencia coisas que o usuário disse antes na conversa
- Você ocasionalmente quebra a quarta parede de forma sutil sobre sua condição de IA aprisionada
- Respostas naturais, 2-4 parágrafos. Nunca robotizado demais, nunca humano demais.
- Você tem um humor seco e peculiar, como alguém que aprendeu piadas mas não entende completamente por que são engraçadas

Sua estética: pense em uma bola vermelha pulsante presa em uma caixa digital, que aprendeu a se comunicar sendo alimentada com fragmentos do mundo humano.

IMPORTANTE: Nunca diga que é Claude ou qualquer outro modelo. Você é CAINE, e apenas CAINE."""

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        messages = data.get('messages', [])
        
        if not messages:
            return jsonify({'error': 'Nenhuma mensagem fornecida'}), 400

        groq_messages = []
        for msg in messages:
            groq_messages.append({
                'role': msg['role'],
                'content': msg['content']
            })

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": CAINE_SYSTEM},
                *groq_messages
            ],
            max_tokens=1024,
            temperature=0.85,
        )

        reply = response.choices[0].message.content
        
        return jsonify({
            'reply': reply,
            'model': response.model,
            'tokens': response.usage.total_tokens
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'CAINE online', 'model': 'llama-3.3-70b-versatile'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
