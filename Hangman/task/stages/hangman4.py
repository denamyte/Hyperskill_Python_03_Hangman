import random


word = random.choice(['python', 'java', 'kotlin', 'javascript'])
print('H A N G M A N')
hint = word[:3] + "-" * (len(word) - 3)
user_input = input(f'Guess the word {hint}: ')
print('You survived!' if user_input == word else 'You lost!')
