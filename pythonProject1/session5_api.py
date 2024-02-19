import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon)

# Exercise 5.3: Get the height and weight of a specific Pokemon
import requests

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])

# moves
import requests

pokemon_number = input("What is the Pokemon's ID? ")

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
response = requests.get(url)
pokemon = response.json()

moves = pokemon['moves']

for move in moves:
    print(move['move']['name'])