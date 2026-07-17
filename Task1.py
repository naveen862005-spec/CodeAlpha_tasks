import random

# List of words
words = ["apple", "tiger", "house", "chair", "water"]

# Fixed word for testing
word = "apple"
# To make it random later, use:
# word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== WELCOME TO HANGMAN =====")

while wrong_guesses < max_wrong:

    # Display the word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the word is guessed
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Wrong Guesses:", wrong_guesses)
        print("Remaining Attempts:", max_wrong - wrong_guesses)

# Game Over
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The correct word was:", word)