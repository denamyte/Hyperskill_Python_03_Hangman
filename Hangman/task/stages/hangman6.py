import random


def get_hint_str():
    mapped_word = map(lambda char: char if char in guessed_letters else '-', word)
    return ''.join(mapped_word)


word = random.choice(['python', 'java', 'kotlin', 'javascript'])
guessed_letters = set()
lives = 8
hint = get_hint_str()
print('H A N G M A N')
while lives > 0:
    print()
    print(hint)
    user_letter = input('Input a letter: ')

    if user_letter in word:
        if user_letter in guessed_letters:
            print('No improvements')
            lives -= 1
        else:
            guessed_letters.add(user_letter)
    else:
        print("That letter doesn't appear in the word")
        lives -= 1

    hint = get_hint_str()
    if '-' not in hint:
        print(f'''
{word}
You guessed the word!
You survived!''')
        break
else:
    print("You lost!")
