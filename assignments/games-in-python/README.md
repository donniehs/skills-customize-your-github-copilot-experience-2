
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a complete Hangman word-guessing game using Python strings, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Initialize the game with a list of possible words and randomly select one word for the player to guess.

#### Requirements
Completed program should:

- Store a predefined list of words
- Randomly select one word as the secret word
- Initialize the player's number of incorrect guesses
- Track the letters the player has already guessed

### 🛠️ Implement the Guessing Loop

#### Description
Create a loop that accepts a letter guess, displays the player's progress, and updates the game state.

#### Requirements
Completed program should:

- Ask the player to enter one letter at a time
- Display correctly guessed letters in `_ _ _` format
- Show the letters already guessed
- Track incorrect guesses and remaining attempts
- End when the word is fully guessed or no attempts remain

### 🛠️ Finish the Game

#### Description
Display a clear result and stop the program when the game ends.

#### Requirements
Completed program should:

- Display a win message when the player guesses the secret word
- Display a lose message and reveal the secret word when attempts are exhausted
- End the program after a win or loss
