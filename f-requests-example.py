import requests

# do get request
result = requests.get('https://catfact.ninja/breeds')

print(result.text)
