import random


def player():
    print("Lets play Rock,Paper,Scissor,Lizard, Spock\n")
    print("Choose S for Scissors")
    print("Choose P for Paper")
    print("Choose R for Rock")
    print("Choose L for Lizard")
    print("Choose V for Spock")

    choice = input("Now enter your Choice, player!: ").upper()
    if choice != "S" and choice != "P" and choice != "R" and choice != "L" and choice != "V":
        print("Invalid input")
        player()

    elif choice == "S":
        print("You picked Scissors")
    elif choice == "P":
        print("You picked Paper")
    elif choice == "R":
        print("You picked Rock")
    elif choice == "L":
        print("You picked Lizard")
    elif choice == "V":
        print("You picked Spock")
    return choice


def computer():
    possible_actions = ["S", "P", "R", "L", "V"]
    pick = random.choice(possible_actions)

    if pick == "S":
        print("Genius computer picked Scissors")
    elif pick == "P":
        print("Genius computer picked Paper")
    elif pick == "R":
        print("Genius computer picked Rock")
    elif pick == "L":
        print("Genius computer picked Lizard")
    elif pick == "V":
        print("Genius computer picked Spock")
    return pick


def game(player_choice, computer_choice):


    if computer_choice == player_choice:
        print("Oh no! its a \n ** TIE **")
        print("Lets do it again")
        return game(player(), computer())
    # condition 1
    elif player_choice == "S" and computer_choice == "P":
        return True
    elif player_choice == "P" and computer_choice == "S":
        return False
    # condition 2
    elif player_choice == "P" and computer_choice == "R":
        return True
    elif player_choice == "R" and computer_choice == "P":
        return False
    # condition 3
    elif player_choice == "R" and computer_choice == "L":
        return True
    elif player_choice == "L" and computer_choice == "R":
        return False
    # condition 4
    elif player_choice == "V" and computer_choice == "L":
        return True
    elif player_choice == "L" and computer_choice == "V":
        return False
    # condition 5
    elif player_choice == "V" and computer_choice == "S":
        return True
    elif player_choice == "S" and computer_choice == "V":
        return False
    # condition 6
    elif player_choice == "S" and computer_choice == "L":
        return True
    elif player_choice == "L" and computer_choice == "S":
        return False
    # condition 7
    elif player_choice == "L" and computer_choice == "P":
        return True
    elif player_choice == "P" and computer_choice == "L":
        return False
    # condition 8
    elif player_choice == "V" and computer_choice == "R":
        return True
    elif player_choice == "R" and computer_choice == "V":
        return False
    # condition 9
    elif player_choice == "R" and computer_choice == "S":
        return True
    elif player_choice == "S" and computer_choice == "R":
        return False
    else:
        return False