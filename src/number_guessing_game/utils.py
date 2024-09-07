#!/usr/bin/env python3

from typing import Dict, Tuple

# Constants for difficulty levels
EASY = 1
MEDIUM = 2
HARD = 3

# Number of chances for each difficulty level
EASY_CHANCES = 10
MEDIUM_CHANCES = 5
HARD_CHANCES = 3

# The guessing range
MIN_RANGE = 1
MAX_RANGE = 100

# Difficulty levels dictionary
DIFFICULTY_LEVELS: Dict[int, Tuple[str, int]] = {
    EASY: ("EASY", EASY_CHANCES),
    MEDIUM: ("MEDIUM", MEDIUM_CHANCES),
    HARD: ("HARD", HARD_CHANCES)
}


def get_difficulty_level() -> int:
    """
    Prompts the player to select a difficulty level.

    Returns:
        str: The number of chances available for the selected difficulty level.
    """
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in DIFFICULTY_LEVELS:
                level_name, chances = DIFFICULTY_LEVELS[choice]
                print(f"\nGreat! You have selected {level_name} difficulty.\n"
                      "Let's start the game!\n")
                return chances
            else:
                print("\nInvalid choice.\n"
                      "Please select [1, 2, or 3]")
        except (ValueError):
            print("Please enter a valid number (1, 2, or 3).")


def get_user_guess() -> int:
    """
    Prompts the player to input their guess for the number.

    Returns:
        int: The guessed number, if it is valid (between MIN_RANGE & MAX_RANGE).
    """
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if MIN_RANGE <= guess <= MAX_RANGE:
                return guess
            else:
                print(f"Please enter a number between {MIN_RANGE} and {MAX_RANGE}\n")
        except ValueError:
            print("Please enter a valid number")


def get_decision() -> str:
    """
    Asks the player if they want to play another round.

    Returns:
        str: 'yes' or 'no' based on the player's decision.
    """
    valid_responses = {"yes", "no"}

    while True:
        decision = input("DO YOU WANT TO PLAY ANOTHER ROUND?\n"
                         "Type YES or NO: ").lower().strip()

        if decision in valid_responses:
            return decision
        else:
            print("Invalid input. Please enter 'yes' or 'no'")
