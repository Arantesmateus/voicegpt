# 🎙️ Voice GPT

> Assistente de voz inteligente desenvolvido em Python com transcrição de áudio, síntese de fala e integração com LLM via Groq.

Projeto criado durante o **Bootcamp Bradesco - GenAI & Dados** na [DIO](https://www.dio.me/).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MCVvgOmfm2WQm840FPIVBIQiJbLCNE11?usp=sharing)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?logo=openai&logoColor=white)

---

## 🚀 Sobre o Projeto

O **Voice GPT** é um assistente de voz que permite ao usuário conversar com uma IA utilizando a fala. O fluxo funciona da seguinte forma:

1. 🎤 **Gravação** — Captura o áudio do microfone em tempo real
2. 📝 **Transcrição** — Converte a fala em texto com o modelo Whisper
3. 🤖 **Processamento** — Envia o texto para o LLM via API da Groq
4. 🔊 **Resposta** — Converte a resposta gerada em áudio com gTTS e reproduz

---

## 🛠️ Tecnologias e Bibliotecas

| Biblioteca | Função |
|---|---|
| `whisper` | Transcrição de fala para texto (Speech-to-Text) |
| `groq` | Integração com LLM via API Groq |
| `gTTS` | Síntese de voz (Text-to-Speech) |
| `sounddevice` | Captura de áudio do microfone |
| `scipy` | Leitura e escrita de arquivos de áudio |
| `playsound` | Reprodução do áudio gerado |
| `numpy` | Manipulação de arrays de áudio |
| `python-dotenv` | Gerenciamento de variáveis de ambiente |

---

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.10+
- Uma chave de API da [Groq](https://console.groq.com/)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/voice-gpt.git
cd voice-gpt

# Instale as dependências
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

### Execução

```bash
python main.py
```

Ou acesse diretamente pelo **Google Colab** no badge acima. ☝️

---

## 📁 Estrutura do Projeto

```
voice-gpt/
├── main.py          # Script principal
├── .env             # Variáveis de ambiente (não versionar)
├── .env.example     # Exemplo de configuração
├── requirements.txt # Dependências do projeto
└── README.md
```

---

## 📚 Contexto

Este projeto foi desenvolvido como parte do **Bootcamp Bradesco - GenAI & Dados** oferecido pela DIO, com o objetivo de explorar na prática o uso de modelos de linguagem, transcrição de áudio e síntese de voz em Python.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
