---

# Number Guessing Game

Welcome to the Number Guessing Game! This is a simple command-line game where the computer selects a random number, and you have to guess it. You have a limited number of chances to guess the number, and the game will end either when you guess the number correctly or run out of chances.

## Features

- Select a difficulty level to determine the number of chances:
  - **Easy**: 10 chances
  - **Medium**: 5 chances
  - **Hard**: 3 chances
- Receive feedback on whether your guess is too high or too low.
- Track the number of attempts and time taken to guess the number.
- Option to play multiple rounds.

## How to Play

1. **Start the Game**: Run the script to start the game.
2. **Select Difficulty Level**: Choose from Easy, Medium, or Hard to set the number of chances you have.
3. **Enter Your Guess**: Guess the number between 1 and 100.
4. **Receive Feedback**: The game will tell you if the number is higher or lower than your guess.
5. **Win or Lose**: The game ends when you either guess the correct number or run out of chances.
6. **Play Again**: Decide if you want to play another round or exit.

## Sample Output

```plaintext
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 35
Incorrect! The number is less than 35.

Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts.
```

## Additional Features (To Be Added)

- **Hint System**: Implement a hint system that provides clues to the user if they are stuck..
- **Score**: Keep track of the user’s high score (i.e., the fewest number of attempts it took to guess the number under a specific difficulty level).
