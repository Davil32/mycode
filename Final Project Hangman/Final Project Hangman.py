"""provides access to a function"""
# the commands below access two files to generate the words and extract the visuals
import random
from words import words
from hangman_visual import lives_visual_dict
"""provides formatting function"""
# the cprint argument can change the output to colour, number style, upper or lower case letters
# the figlet_format helps convert ascii texts to ascii art fonts
import string
from termcolor import cprint
from pyfiglet import figlet_format
# Thanks to Eric for help on the code above
# Thanks to Kylie for help on some of the code below
cprint(figlet_format('THE HANGMAN SHOW!', font='starwars'),
       'yellow', attrs=['bold'])
# print of initial steps to invite in the game
print('I want to play a game with you, hangman, lets begin!')
"""prompts a user to enter a valid word"""
# Some words have spaces and/or - in the middle of the words. So we need to find out valid word
def get_valid_word(words):
    # randomly chooses words from the list
    word = random.choice(words)
    # the commands below is used to execute a block statements repeatedly until a given condition is true
    while '-' in word or ' ' in word:
        word = random.choice(words)
    # the loop iterate until we get the word that does not have - or space on it.
    return word.upper()

def hangman():
    word = get_valid_word(words)
    # keeps track of what already has been guessed in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    # what the user had guessed
    used_letters = set()

    tries = 7

    # getting user input
    while len(word_letters) > 0 and tries > 0:
        # prints out message and letters used, ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", tries, "tries until your execution and the letters you have used are: ")
        print(", ".join(used_letters))
        # what the current word is
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print(lives_visual_dict[tries])
        print('The word that will pardon is: ', ' '.join(word_list))

        user_letter = input('The letter that can save you is: ').upper()
        # both alphabet and user letters are sets, the "-" makes the difference between the two sets
        # all the characters in the alphabet that are not in used letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # if the letter that user just guessed in the word, it would be removed from word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                # takes away a life if wrong and prints otu a message of letter
                tries = tries - 1
                print('\nThe letter you chose,', user_letter, 'wont save you, tried again.')
            # prints out a message if same letter is used
        elif user_letter in used_letters:
            print('\nStop buying time by reusing the same letter, really. Tried another one.')
            # prints out a continuous message when inputting a letter
        else:
            print('\nThat is not the letter you need.')

    # gets here when len(word_letters) == 0 OR when tries == 0
    # displays the visual to show the progression of the tool and character
    # the cprint argument will display an output once the game is lost
    if tries == 0:
        print(lives_visual_dict[tries])
        print('Those that do not appreciate the word, dont deserve the freedom! the word was', word)
        cprint(figlet_format('YOU MAY REST IN PEACE', font='starwars'),
               'yellow', attrs=['bold'])
        # the cprint argument will display an output once the game is won
    else:
        print('CONGRATULATIONS! You have been save by the word', word, '!!')
        cprint(figlet_format('ENJOY LIFE', font='starwars'),
               'yellow', attrs=['bold'])


if __name__ == '__main__':
        hangman()
