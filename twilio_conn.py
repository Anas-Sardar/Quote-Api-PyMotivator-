from twilio.rest import Client
from config import auth_token,account_sid,whatsapp_number

def set_twilio_connection(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    return client

def send_whatsapp_text(client,quote):
      message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=quote,
        to=whatsapp_number
        )
      return message.sid

client = set_twilio_connection(account_sid, auth_token)