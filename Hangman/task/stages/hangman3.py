import random


words = ['python', 'java', 'kotlin', 'javascript']
selected = random.choice(words)
# print('selected is', selected)  # for debugging purposes

print('H A N G M A N')
user_input = input('Guess the word: ')
print('You survived!' if user_input == selected else 'You lost!')
