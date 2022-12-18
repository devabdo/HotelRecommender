import requests

url = "https://hotels4.p.rapidapi.com/locations/v3/search"

API_KEY = '5fa5658111mshd1008bbe356bc06p1ac1f6jsn9e45212f9333'
HEADERS = {
    'X-RapidAPI-Key': API_KEY,
    'X-RapidAPI-Host': 'hotels4.p.rapidapi.com',
}


def search(query: str):
    params = {'q': f'{query} hotels', 'locale': 'en_US'}
    response = requests.request(
        'GET', url, headers=HEADERS, params=params)
    data = response.json()
    result = []
    for entity in data.get('sr', []):
        if entity['type'] == 'HOTEL':
            result.append(entity['regionNames']['displayName'])
    return result
