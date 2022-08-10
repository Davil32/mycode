#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Creating a simple dice program utilizing classes."""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

    def prog_info(self):
        print("My Dice Game .v02")
        print("You have three rolls of the dice to match a number you select.")
        print("Good Luck!!")
        print("---------------------------------------------------------------")
        print(f'You will win 2 times your wager if you guess on the 1st roll.')
        print(f'You will win 1 1/2 times your wager if you guess on the 2nd roll.')
        print(f'You can win your wager if you guess on the 3rd roll.')
        print("---------------------------------------------------------------")

    def total_bank(bank):
    bet = 0
    while bet <= 0 or bet > min([500,bank]):
        print(f"You have ${bank} in your bank.")
        a = input("Enter your bet (or Q to quit): ")
        if a == 'q': exit()
        bet = int(a)
    return bank,bet

def main():
    """called at run time"""

    ## create our player objects
    player1 = Player()
    player2 = Player()

    player1.roll()
    player2.roll()

    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    # determine which player won
    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw!")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == "__main__":
    main()

