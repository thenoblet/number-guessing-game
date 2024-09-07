#!/usr/bin/env python3

"""
Number Guessing Game

This module implements a simple number guessing game where the player is
prompted to guess a number between 1 and 100. The player selects a difficulty
level, which determines the number of attempts they have to guess the number.
The game will provide feedback on whether the guess was too high or too low,
and tracks the time taken to guess correctly.

Difficulty Levels:
    - Easy: 5 chances
    - Medium: 3 chances
    - Hard: 1 chance

The player can choose to play another round after each game ends.
"""

import random
import time
import sys
from typing import Tuple
from utils import (
    get_difficulty_level,
    get_decision,
    get_user_guess,
    MIN_RANGE,
    MAX_RANGE,
    EASY_CHANCES,
    MEDIUM_CHANCES,
    HARD_CHANCES
    )


def main() -> None:
    """
    Main game loop. Starts the game, displays the summary, and checks if the
    player wants to play another round.
    Exits the game if the player decides not to continue.
    """
    while True:
        welcome()
        attempts, time_taken = start_game()
        print(f"\nGame Summary::")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {time_taken:.2f} seconds\n")
        decision = get_decision()

        if decision == "no":
            print("THANKS FOR PLAYING")
            sys.exit()


def welcome() -> None:
    """
    Prints the welcome message and instructions for the player.

    Displays the number of chances available based on the difficulty level.
    """
    print("Welcome to the Number Guessing Game!\n"
          "I am thinking of a number between 1 and 100\n"
          "You have some number of chances depending on the level you choose\n\n"

          "Please select the difficulty level:\n"
          f"1. Easy ({EASY_CHANCES} Chances)\n"
          f"2. Medium ({MEDIUM_CHANCES} Chances)\n"
          f"3. Hard ({HARD_CHANCES} Chance)\n")


def start_game() -> Tuple[int, float]:
    """
    Starts the guessing game based on the selected difficulty level.

    The player has a limited number of chances based on the chosen difficulty.
    The game provides feedback on whether the guess is too high or too low.

    Returns:
        Tuple[int, float]: The number of attempts and the time taken to guess.
    """
    attempts = 0
    random_number = random.randint(MIN_RANGE, MAX_RANGE)
    chances = get_difficulty_level()

    start_time = time.time()

    while chances > 0:
        guess = get_user_guess()
        attempts += 1

        if random_number == guess:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"\nCongratulations! You guessed the number in {attempts} attempts\n")
            print(f"It took you {elapsed_time:.2f} seconds\n")
            return attempts, elapsed_time
        elif random_number > guess:
            print(f"\n\nIncorrect! The number is greater than {guess}\n")
        else:
            print(f"\n\nIncorrect! The number is less than {guess}\n")

        chances -= 1
        if chances > 0:
            print(f"You have {chances} chances left!\n")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"GAME OVER! The number was {random_number}\n")
            print(f"It took you {elapsed_time:.2f} seconds\n")
            return attempts, elapsed_time


if __name__ == "__main__":
    main()
