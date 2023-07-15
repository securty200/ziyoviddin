
import requests
from pprint import pprint as print


 
def curses():
    API='900091b478009c8dfb86af00'
    curse='USD'
    url = f'https://v6.exchangerate-api.com/v6/{API}/pair/{curse}/UZS'


    response = requests.get(url)

    return response.json()["conversion_rate"]
