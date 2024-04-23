import requests

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

content = data['content']
author = data['author']
tags = data['tags']

print("Quote:", content)
print("Author:", author)
#print("Category:", tags)