import random
import os


def read_file():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [line.replace('\n', '') for line in f]
    return words


def transform_word(word):
    new_word = word
    letter_cases = {
        "á": 'a',
        "é": 'e',
        "í": 'i',
        "ó": 'o',
        "ú": 'u'
    }
    for letter in word:
        if letter_cases.get(letter) != None:
            new_word = new_word.replace(letter, letter_cases[letter])
    return new_word


def verify_letter(letter, word):
    word_enumerate = [{letter: index} for index, letter in enumerate(word)]
    letter_filter = list(
        filter(lambda let: let.get(letter) != None, word_enumerate))
    return letter_filter


def build_interfaz(word, total_lives):
    space_letter = ""
    error = ''
    partial_word = [i for i in word]
    space_letter = ''.join(["_ " for i in word])

    while(space_letter.replace(' ', '').lower() != word and total_lives != 0):
        print(str(error) + "\nGuest the word!\n" + space_letter + '\n')
        print("Su numero de intentos es:", total_lives)
        error = ''
        try:
            letter = transform_word(input("Ingrese una letra: ").lower())
            if len(letter) > 1 or letter.isdigit():
                raise ValueError('ADVERTENCIA: Solo se pueden ingresar letras')
            letters_find = verify_letter(letter, partial_word)
            if len(letters_find) != 0:
                space_letter_list = space_letter.split(' ')
                for letter_dict in letters_find:
                    space_letter_list[letter_dict.get(letter)] = letter.upper()
                    space_letter = " ".join(space_letter_list)
                    partial_word[letter_dict.get(letter)] = ' '
            total_lives -= 1
        except ValueError as ve:
            error = ve
        finally:
            os.system('cls')
    return total_lives


def run():
    list_words = read_file()
    random_word = random.choice(list_words).lower()
    total_lives = len(random_word) * 2
    lives = build_interfaz(transform_word(random_word), total_lives)
    if (lives != 0):
        print('Felicidades ha adivinado la palabra:',
              random_word.upper(), '!!!!')
        print('Su numero de intentos fueron: ', lives + 1 , '/', total_lives )
    else:
        print('Ha gastado todas sus vidas :c, la palabra era', random_word.upper())


if __name__ == '__main__':
    run()
