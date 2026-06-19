
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses string manipulation, loops, conditionals, and user interaction.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a Hangman game that randomly selects a secret word from a list and prepares the game state for the player.

#### Requirements
Completed program should:

- Define a list of possible words for the game.
- Randomly choose one word from the list.
- Initialize the display state using underscores for each letter in the secret word.
- Track the number of incorrect guesses remaining.


### 🛠️ Player Guessing Logic

#### Description
Allow the player to guess letters, update the displayed progress, and prevent repeated guesses.

#### Requirements
Completed program should:

- Accept a letter guess from the player using `input()`.
- Reveal correctly guessed letters in the display state (e.g. `_ A _ _ _`).
- Keep a list of guessed letters and avoid re-processing repeated guesses.
- Decrease remaining attempts when the guess is incorrect.


### 🛠️ Win/Lose Game Flow

#### Description
Handle the main game loop and finish the game with a win or loss message.

#### Requirements
Completed program should:

- Continue prompting the player until the word is fully guessed or attempts run out.
- Show the current word progress after each guess.
- Display a win message when the player guesses the word.
- Display a lose message when the player runs out of attempts.
