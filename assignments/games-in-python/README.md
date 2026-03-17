
# 🎮 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, and user input while creating an interactive game experience.

## 📝 Tasks

### 🛠️  Game Setup

#### Description
Set up the basic structure for your Hangman game. Define a list of possible words and randomly select one for the player to guess.

#### Requirements
Completed program should:

- Contain a predefined list of at least 5 words
- Randomly select one word as the secret word
- Display a welcome message and game instructions


### 🛠️  Gameplay Loop

#### Description
Implement the main game loop where the player guesses letters, and the game tracks progress and remaining attempts.

#### Requirements
Completed program should:

- Show the current progress (e.g., _ _ t _ o _)
- Accept single-letter guesses from the user
- Track and display incorrect guesses remaining
- End the game when the word is guessed or attempts run out
- Display a win or lose message at the end

#### Example
```
Welcome to Hangman!
Word: _ _ _ _ _
Guesses left: 6
Guess a letter: a
Word: _ a _ _ _
Guesses left: 6
Guess a letter: e
Word: _ a _ _ e
Guesses left: 6
...
Congratulations! You guessed the word.
```
