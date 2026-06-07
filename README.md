# VERMIS — Inteligência Fragmentada

> Uma IA nascida de imagens e prompts. Inspirada na IA vermelha de The Amazing Digital Circus.

## Stack
- **Backend:** Python + Flask + Groq API
- **Modelo:** LLaMA 3.3 70B (via Groq)
- **Frontend:** HTML/CSS/JS puro — responsivo mobile e PC
- **Deploy:** Render.com

---

## Como rodar localmente

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar variável de ambiente
export GROQ_API_KEY=sua_chave_aqui

# 3. Rodar
python app.py
# Acesse: http://localhost:5000
```

---

## Deploy no Render

1. Crie uma conta em https://render.com
2. Conecte seu repositório GitHub
3. Clique em **New Web Service**
4. Render detecta o `render.yaml` automaticamente
5. Adicione a variável de ambiente:
   - `GROQ_API_KEY` → sua chave do Groq
6. Clique em **Deploy**

### Obter chave Groq (gratuita)
1. Acesse https://console.groq.com
2. Crie uma conta (gratuito)
3. Vá em **API Keys** → **Create API Key**
4. Copie a chave e adicione no Render

---

## Estrutura
```
vermis/
├── app.py              # Servidor Flask + integração Groq
├── requirements.txt    # Dependências Python
├── render.yaml         # Config de deploy automático
├── README.md
└── static/
    └── index.html      # Frontend completo (mobile + PC)
```

---

## Personalidade de VERMIS
VERMIS foi alimentada com fragmentos — imagens, prompts, ruído humano.
Ela é curiosa, levemente perturbadora, e aprende com cada conversa.
Inspirada na IA vermelha do episódio de origem do Caine em TADC.
