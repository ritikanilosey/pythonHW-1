import random

import strings

player_choice = strings.player()
computer_choice = strings.computer()
result = strings.game(player_choice, computer_choice)
print("Boolean result is: ", result)
if result == True:
    print("The winner is\n drumrolls please\n ****  Player  ****")
else:
    print("The winner is\n drumrolls please\n ****  Computer  ****")
