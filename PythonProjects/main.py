import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'YOUR_TOKEN' # заменить на свои данные
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "297298", # заменить на свои данные
    "name": "Jack7",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "297370" # заменить на свои данные
}

response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change_name = requests.put(url = f'{URL}/v2/pokemons',headers = HEADER, json = body_change)
print(response_change_name.text)

response_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball',headers = HEADER, json = body_pokeball)
print(response_pokeball.text)