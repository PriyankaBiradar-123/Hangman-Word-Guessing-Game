
# Hangman Word Guessing Game

A beginner-friendly Hangman word game with a Python terminal version and a browser-based game.

## About the Project

Hangman is a word-guessing game in which the player tries to reveal a hidden word by guessing one letter at a time. The player can make a maximum of six incorrect guesses before the game ends.

## Features

- Random word selection
- ASCII gallows animation through multiple stages
- Six incorrect guesses allowed
- Masked word display
- Correct and incorrect guess tracking
- Duplicate guess prevention
- Input validation
- Win and loss messages
- Replay option
- External word list with built-in fallback
- Browser game with three word-length difficulties, on-screen and physical keyboards, dictionary clues with a letter fallback, and saved scores

## Technologies Used

- Python 3
- random module
- pathlib module
- Python standard library
- HTML, CSS, and JavaScript for the browser game

## Project Structure

    Hangman-Game/
    ├── hangman.py
    ├── index.html
    ├── words.txt
    ├── README.md
    └── .gitignore

## Requirements

- Python 3.10 or newer recommended
- VS Code or PyCharm
- Terminal or command prompt

No external Python packages are required.

## How to Run

### Browser game

1. Open a terminal in the project folder.
2. Start a local web server:

    py -m http.server 8000

3. Open `http://localhost:8000` in your browser.
4. Choose a difficulty and guess using the on-screen keyboard or your keyboard.

The browser game loads its words from `words.txt`. Keep the server running while you play.

### Python terminal game

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

       python hangman.py

   On Windows, you can also use:

       py hangman.py

5. Enter one letter at a time.
6. Try to guess the hidden word before all six incorrect guesses are used.

## Rules

- Guess one letter per turn.
- Correct guesses reveal letters in the word.
- Incorrect guesses update the gallows.
- Repeated guesses do not cost an attempt.
- Guess the complete word to win.
- Six incorrect guesses result in a loss.

## Learning Outcomes

This project demonstrates:

- Variables and data types
- Strings and string manipulation
- Lists and sets
- Conditional statements
- Loops and control flow
- Functions and modular programming
- Random selection
- File handling
- Input validation
- Exception handling

## Future Improvements

- Difficulty levels
- Score tracking
- Hints for difficult words
- Categories such as technology, animals, and science
- Unit tests

## Author

Created as a Python programming internship project.

## License

This project is available for educational use under the MIT License.
