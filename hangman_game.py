import random

# List of 5 predefined words
words = ["python", "computer", "programming", "developer", "security"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
incorrect_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses:", incorrect_guesses)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        print("You won the game!")
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check for repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game over
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", word)