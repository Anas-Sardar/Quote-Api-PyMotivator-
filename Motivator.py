import requests
from twilio_conn import send_whatsapp_text,client 
url = "https://api.quotable.io/quotes/random"
while True:
    res = requests.get(url=url)
    data = res.json()
    if isinstance(data, list):
        # If the API returns a list of quotes, pick the first one
        data = data[0]

    tags = data.get('tags', [])
    if any(tag.lower() in ['inspirational', 'motivational'] for tag in tags):
        break

quote = data['content']
author = data['author']
tags = data['tags']

print("Quote:", quote)
print("Author:", author)
#print("Category:", tags)

send_whatsapp_text(client,quote,author)