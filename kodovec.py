# Александър Захаринов
# Клас: 8а
# Номер: 3

import os

MAX_ERRORS = 6

def read_word_from_file(file_name):
    if not os.path.exists(file_name):
        print("Файлът не съществува!")
        return None
    
    with open(file_name, 'r', encoding='utf-8') as file:
        word = file.readline().strip().lower()
    return word

def display_word_progress(word, guessed_letters):
    display = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print(display)

def get_user_input():
    return input("Опитай се да познаеш буква: ").strip().lower()

def update_guessed_letters(letter, guessed_letters):
    guessed_letters.add(letter)

def display_hangman(errors):
    stages = [
        """
         _______
         |/    |
         |     
         |    
         |    
         |    
         |___
        """,
        """
         _______
         |/    |
         |    (_)
         |    
         |    
         |    
         |___
        """,
        """
         _______
         |/    |
         |    (_)
         |     |
         |    
         |    
         |___
        """,
        """
         _______
         |/    |
         |    (_)
         |    \|
         |    
         |    
         |___
        """,
        """
         _______
         |/    |
         |    (_)
         |    \|/
         |    
         |    
         |___
        """,
        """
         _______
         |/    |
         |    (_)
         |    \|/
         |     |
         |    
         |___
        """,
        """
         _______
         |/    |
         |    (_)
         |    \|/
         |     |
         |    / \
         |___
        """
    ]
    print(stages[errors])

def play_game():
    file_name = input("Дай името на файла: ").strip()
    word = read_word_from_file(file_name)
    if word is None:
        return
    
    guessed_letters = set()
    errors = 0
    
    while errors < MAX_ERRORS:
        display_word_progress(word, guessed_letters)
        letter = get_user_input()
        
        if not letter.isalpha() or len(letter) != 1:
            print("Моля въведи буква или въведи само една.")
            continue

        if letter in guessed_letters:
            print("Вече си познал тази буква.")
            continue
        
        update_guessed_letters(letter, guessed_letters)
        
        if letter in word:
            if all(l in guessed_letters for l in word):
                display_word_progress(word, guessed_letters)
                print("Другия път ще загубиш!")
                return
        else:
            errors += 1
            print(f":( Остават ти {MAX_ERRORS - errors} опита.")
            display_hangman(errors)
    
    print("Смешка загуби! *кофти тръпка*")
    display_hangman(errors)
    print(f"Думата беше: {word}")

if __name__ == "__main__":
    play_game()