import random
import requests
import time

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
    response = requests.get(url)
    pokemon_data = response.json()

    pokemon = {
        'name': pokemon_data['name'].capitalize(),
        'id': pokemon_data['id'],
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        'base_experience': pokemon_data['base_experience'],
        'moves': len(pokemon_data['moves']),
        'abilities': len(pokemon_data['abilities'])
    }
    return pokemon


stat_mapping = {
    1: 'height',
    2: 'weight',
    3: 'base_experience',
    4: 'moves',
    5: 'abilities',
}

num_rounds = 3
round_delay = 5
game_break = 2

player_wins = 0
opponent_wins = 0

print('\nWelcome to a game of Top Trumps with Pokemons')

for round_num in range(1, num_rounds + 1):
    print(f'\nRound {round_num}:')

    player_pokemon_choices = [random_pokemon() for _ in range(2)]
    print("Choose your Pokemon:")
    for i, pokemon in enumerate(player_pokemon_choices, start=1):
        print(f"{i}. {pokemon['name']}")

    selected_index = int(input("Enter the number corresponding to the Pokemon you want to use: "))
    while selected_index not in [1, 2]:
        print("Invalid choice, please select a valid number.")
        selected_index = int(input("Enter the number corresponding to the Pokemon you want to use: "))

    selected_pokemon = player_pokemon_choices[selected_index - 1]
    print(f"You selected {selected_pokemon['name']}")

    opponent_pokemon = random_pokemon()
    print(f'The opponent was given {opponent_pokemon["name"]}')

    time.sleep(game_break)

    if round_num % 2 == 0:
        selected_stat = random.choice(list(stat_mapping.values()))
        time.sleep(game_break)
        print(f"The opponent chose to compare '{selected_stat}'")

    else:
        print("Choose a stat:")
        for key, value in stat_mapping.items():
            print(f"{key}. {value}")

        stat_choice = int(input('Enter the number corresponding to the stat you want to use: '))

        while stat_choice not in stat_mapping:
            print("Invalid choice, please select a valid number.")
            stat_choice = int(input('Enter the number corresponding to the stat you want to use: '))

        selected_stat = stat_mapping[stat_choice]

    my_stat = selected_pokemon[selected_stat]
    opponent_stat = opponent_pokemon[selected_stat]

    time.sleep(game_break)
    print(f'\nYour Pokémon {selected_pokemon["name"]} has {my_stat} {selected_stat}')
    print(f'Opponent\'s Pokémon {opponent_pokemon["name"]} has {opponent_stat} {selected_stat}')

    if my_stat > opponent_stat:
        print('You Win this round! 🎉')
        player_wins += 1
    elif my_stat < opponent_stat:
        print('You Lose this round! 😞')
        opponent_wins += 1
    else:
        print('Draw this round! ⚖️')

    if round_num < num_rounds:
        print(f'\nNext round will start in {round_delay} seconds...')
        time.sleep(round_delay)

print('\nGame Over!')
if player_wins > opponent_wins:
    print('Congratulations! You won the game! 🎉')
elif player_wins < opponent_wins:
    print('Sorry, you lost the game. 😞')
else:
    print('The game ended in a tie. ⚖️')
