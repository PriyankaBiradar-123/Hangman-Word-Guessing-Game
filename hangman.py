
import random
from pathlib import Path

MAX_ATTEMPTS = 6
WORD_FILE = Path(__file__).parent / "words.txt"

# The stages progress from an empty gallows to the complete figure.
HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
         |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
    =======""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
    =======""",
]

FALLBACK_WORDS = [
    "python", "hangman", "computer", "program",
    "keyboard", "developer", "science", "planet",
    "journey", "library", "rainbow", "diamond",
    "puzzle", "network", "function", "variable",
]


def load_words():
    """Load valid words from words.txt or use built-in words."""
    if WORD_FILE.exists():
        try:
            words = [
                line.strip().lower()
                for line in WORD_FILE.read_text(
                    encoding="utf-8"
                ).splitlines()
                if line.strip().isalpha()
            ]

            if words:
                return words

        except OSError:
            print("Could not read words.txt. Using default words.")

    return FALLBACK_WORDS.copy()


def choose_word(words):
    """Select a random word for the current game."""
    return random.choice(words)


def display_game(secret_word, guessed_letters, wrong_guesses):
    """Display the gallows, masked word, and guessed letters."""
    mistakes = len(wrong_guesses)

    print("\n" + "=" * 38)
    print("         HANGMAN WORD GAME")
    print("=" * 38)

    print(HANGMAN_STAGES[mistakes])

    masked_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print(f"\nWord: {masked_word}")
    print(f"Attempts remaining: {MAX_ATTEMPTS - mistakes}")

    if guessed_letters:
        print("Correct guesses:", " ".join(sorted(guessed_letters)))
    else:
        print("Correct guesses: None")

    if wrong_guesses:
        print("Wrong guesses:", " ".join(sorted(wrong_guesses)))
    else:
        print("Wrong guesses: None")

    print("=" * 38)


def get_guess(guessed_letters, wrong_guesses):
    """Ask for one valid letter and reject repeated guesses."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (A-Z).")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        return guess


def play_game(words):
    """Run one complete round of Hangman."""
    secret_word = choose_word(words)
    guessed_letters = set()
    wrong_guesses = set()

    while True:
        display_game(secret_word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nYOU WIN! Congratulations!")
            print(f"You guessed the word: {secret_word.upper()}")
            break

        if len(wrong_guesses) >= MAX_ATTEMPTS:
            print("\nGAME OVER! Better luck next time.")
            print(f"The secret word was: {secret_word.upper()}")
            display_game(secret_word, guessed_letters, wrong_guesses)
            break

        guess = get_guess(guessed_letters, wrong_guesses)

        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"Correct! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            print(f"Sorry! '{guess}' is not in the word.")


def main():
    """Start the game and offer replay until the user exits."""
    words = load_words()

    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses available.")

    while True:
        play_game(words)

        while True:
            choice = input("\nWould you like to play again? (y/n): ")
            choice = choice.strip().lower()

            if choice in ("y", "yes"):
                break

            if choice in ("n", "no"):
                print("\nThanks for playing Hangman. Goodbye!")
                return

            print("Please enter y or n.")


if __name__ == "__main__":
    main()
