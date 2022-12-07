from multiprocessing import RLock
from multiprocessing.connection import wait
from os import system, name
from time import sleep
import random
import re


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def shoot():
    waitTime = 0.5
    chants = ("ROCK! ", "PAPER! ", "SCISSORS! ", "SHOOT!")
    chant = ""

    # iterate through the chants clearing the screen and printing them out
    for c in chants:
        clear()
        chant += c
        print(chant)
        sleep(waitTime)


def pickWinner(pc, cc):
    if (pc + 1) % 3 == cc:
        return "You Lose!"
    elif pc == cc:
        return "Draw!"
    else:
        return "You Win!"


# allowed choices
choices = {0: "rock", 1: "paper", 2: "scissors"}
print("Welcome to Rock Paper Scissors.")
playAgain = "y"

while playAgain == "y":

    playerChoice = int(
        input("Make a choice; 0 for rock, 1 for paper or 2 for scissors\n"))

    computerChoice = random.choice(list(choices))

    if playerChoice not in choices.keys():
        print("{} is an invalid choice.  Please enter 0 for rock,  1 for paper or 2 for scissors".format(
            playerChoice))
    else:
        shoot()

        print("You picked: {}".format(choices[playerChoice]))
        print("I picked: {}".format(choices[computerChoice]))

        print(pickWinner(playerChoice, computerChoice))

        playAgain = input("Play again? y for yes / n for no\n")
        clear()
        if playAgain != "y":
            playAgain = "n"
            print("Thanks for Playing")
