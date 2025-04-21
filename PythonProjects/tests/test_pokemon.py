import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'YOUR_TOKEN' # заменить на свои данные
HEADER = {'Content-Type': 'application/json'}
TRAINER_ID = 'YOUR_ID' # заменить на свои данные

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers')
    assert response.status_code == 200

def test_response_name():
    response_name = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'YOUR_NAME' # заменить на свои данные