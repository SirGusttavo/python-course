# Automação com Python

Este projeto demonstra dois exemplos simples de automação usando Python:

- **Envio de mensagens SMS com Twilio**
- **Abertura automática de sites com o módulo `webbrowser`**

---

## 📦 Scripts incluídos

### `index.py`
Envia uma mensagem SMS utilizando a API da Twilio. As credenciais são carregadas de um arquivo `.env` (não incluído no repositório).

> 💡 Exemplo de mensagem: `"Este é um teste de envio automático via Twilio com Python."`

### `outro.py`
Abre automaticamente a página do SENAI Mogi das Cruzes no navegador padrão.

---

## 🔐 Variáveis de Ambiente

Preencha os dados no arquivo `.env` com base no modelo abaixo:

```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_FROM=+1415xxxxxxx
TWILIO_TO=+55xxxxxxxxxx
```

---

## ▶️ Execução

Instale o pacote `python-dotenv` e `twilio` com:

```bash
pip install python-dotenv twilio
```

Execute os scripts:

```bash
python index.py
python outro.py
```

---
