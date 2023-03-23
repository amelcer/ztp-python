
import requests

API_URL = 'https://api.exchangerate.host/latest'


response = requests.get(API_URL, {"base": "PLN"})
data = response.json()


if not data['success']:
    exit('Error')

print(data['rates'])
