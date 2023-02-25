import random
from os import system, name
from time import sleep


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def shoot():
    wait_time = 0.5
    chants = ("ROCK! ", "PAPER! ", "SCISSORS! ", "SHOOT!")
    chant = ""

    # iterate through the chants clearing the screen and printing them out
    for c in chants:
        clear()
        chant += c
        print(chant)
        sleep(wait_time)


def pick_winner(pc, cc):
    if (pc + 1) % 3 == cc:
        return "You Lose!"
    elif pc == cc:
        return "Draw!"
    else:
        return "You Win!"


# allowed choices
choices = {0: "rock", 1: "paper", 2: "scissors"}
print("Welcome to Rock Paper Scissors.")
play_again = "y"

while play_again == "y":

    player_choice = int(
        input("Make a choice; 0 for rock, 1 for paper or 2 for scissors\n"))

    computer_choice = random.choice(list(choices))

    if player_choice not in choices.keys():
        print("{} is an invalid choice.  Please enter 0 for rock,  1 for paper or 2 for scissors".format(
            player_choice))
    else:
        shoot()

        print("You picked: {}".format(choices[player_choice]))
        print("I picked: {}".format(choices[computer_choice]))

        print(pick_winner(player_choice, computer_choice))

        play_again = input("Play again? y for yes / n for no\n")
        clear()
        if play_again != "y":
            play_again = "n"
            print("Thanks for Playing")
