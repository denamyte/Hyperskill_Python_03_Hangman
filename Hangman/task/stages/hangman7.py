import random


def get_hint_str():
    mapped_word = map(lambda char: char if char in guessed_letters else '-', word)
    return ''.join(mapped_word)


def single(letter) -> bool:
    if len(letter) == 1:
        return True
    print("You should input a single letter")
    return False


def english_lowercase(letter) -> bool:
    if letter.isalpha() and letter.islower():
        return True
    print("Please enter a lowercase English letter")
    return False


word = random.choice(['python', 'java', 'kotlin', 'javascript'])
guessed_letters = set()
lives = 8
hint = get_hint_str()
print('H A N G M A N')
while lives > 0:
    print('\n' + hint)
    user_letter = input('Input a letter: ')

    if single(user_letter) and english_lowercase(user_letter):
        if user_letter in guessed_letters:
            print("You've already guessed this letter")
        else:
            if user_letter not in word:
                print("That letter doesn't appear in the word")
                lives -= 1
            guessed_letters.add(user_letter)

    hint = get_hint_str()
    if '-' not in hint:
        print(f'''You guessed the word {word}!
You survived!''')
        break
else:
    print("You lost!")
