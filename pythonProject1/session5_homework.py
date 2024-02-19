# Question 2
poem = 'I like Python and I am not very good at poems'

with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)


# Question 3: POkemon
import requests
pokemon_ids = [34, 56, 98, 125, 76, 45]

with open('pokemon.txt', 'w') as pokemon_file:
    for id in pokemon_ids:
        url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
        response = requests.get(url)
        pokemon = response.json()
        pokemon_name = pokemon['name']
        moves = pokemon['moves']
        pokemon_file.write(f'Pokemon name is {pokemon_name} and these are its moves: \n')
        for move in moves:
            pokemon_file.write(f'{move['move']['name']}\n')

