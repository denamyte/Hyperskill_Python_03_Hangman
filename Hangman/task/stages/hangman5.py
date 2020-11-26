import random


word = random.choice(['python', 'java', 'kotlin', 'javascript'])
word = list(word)
guessed_letters = []  # this could be a set


def get_hint_str():
    output = map(lambda char: char if char in guessed_letters else '-', word)
    return ''.join(output)


print('H A N G M A N')
for _ in range(8):
    print()
    print(get_hint_str())
    guessed_letters.append(input('Input a letter: '))
print("\nThanks for playing!\nWe'll see how well you did in the next stage")
