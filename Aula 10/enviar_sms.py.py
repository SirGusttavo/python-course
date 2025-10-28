from twilio.rest import Client
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Dados da conta (ocultos no .env)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_number = os.getenv('TWILIO_FROM')
to_number = os.getenv('TWILIO_TO')

client = Client(account_sid, auth_token)

# Mensagem de exemplo
mensagem = "Este é um teste de envio automático via Twilio com Python."

client.messages.create(
    from_=from_number,
    to=to_number,
    body=mensagem
)

print("Mensagem enviada com sucesso.")
