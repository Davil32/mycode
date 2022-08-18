import random
from words import words
from hangman_visual import lives_visual_dict
import string
from termcolor import cprint
from pyfiglet import figlet_format
# Thanks to Eric for the above code
cprint(figlet_format('THE HANGMAN SHOW!', font='starwars'),
       'yellow', attrs=['bold'])
print('Welcome to your hanging, Lets get it on!')
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    tries = 7

    # getting user input
    while len(word_letters) > 0 and tries > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        print('You have', tries, 'tries until your execution and your letters used are: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print(lives_visual_dict[tries])
        print('The word that will pardon is: ', ' '.join(word_list))

        user_letter = input('The letter that can save you is: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                tries = tries - 1  # takes away a life if wrong
                print('\nThe letter you chose,', user_letter, 'wont save you, tried again.')

        elif user_letter in used_letters:
            print('\nStop buying time by reusing the same letter, really. Tried another one.')

        else:
            print('\nThat is not the letter you need.')

    # gets here when len(word_letters) == 0 OR when tries == 0
    if tries == 0:
        print(lives_visual_dict[tries])
        print('My you rest in peace, finish him. The word you need was', word)
    else:
        print('NO WAY! You have been save by the magic word', word, '!!')


if __name__ == '__main__':
    hangman()
