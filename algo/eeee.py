"""
def get_guessed_word(secret_word, letters_guessed):
    result = " "
    for letter in secret_word:
        if letter in letters_guessed:
            result = result + letter
        else:
            result = result+ '_'
def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        t = True
        if i not in letters_guessed:
            return False
    return t
def hangman(secret_word):
    s=len(secret_word)
    print("your secret word counatain:",s,"letter")
    print("you have 6 guesses left ")
    def get_guessed_word(secret_word, letters_guessed):
        result = " "
        for letter in secret_word:
            if letter in letters_guessed:
                result = result + letter
            else:
                result = result + '_'
"""



























