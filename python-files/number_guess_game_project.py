# %% [markdown]
# # Number Guessing Game
# ### 18th March 2025
# - This notebook helps us to build a game where the user guesses a randomly generated number.\
# - We use loops and conditionals to provide hints (eg. Too high or too low).\
# - Add a score system to track the number of attempts.

# %%
# Import the random module to generate a random number
import random

# %% [markdown]
# ### Number Guessing Game with Restart Option
# This is a number guessing game where the user has 3 lives to guess a number between 1 and 100.\
# After each wrong guess, the player loses one life. The game ends if the player runs out of lives.\
# The player can choose to restart the game after finishing.

# %%
def number_guessing_game():
    """
    Function to run the number guessing game with a life count and restart option.
    """
    while True:  # Outer loop to allow restarting the game
        # Generate a random number between 1 and 100
        target_number = random.randint(1, 100)
        lives = 3  # Player starts with 3 lives
        attempts = 0
        guessed_correctly = False

        print("\n🎮 Welcome to the Number Guessing Game! 🎮")
        print("I've picked a number between 1 and 100. Can you guess it?")
        print(f"You have {lives} lives. Choose wisely!")

        # Loop until the user guesses the correct number or runs out of lives
        while lives > 0 and not guessed_correctly:
            try:
                # Ask the user for their guess
                guess = int(input("Enter your guess (1-100): "))
                attempts += 1

                # Check if the guess is correct
                if guess < target_number:
                    lives -= 1
                    print(f"Hint: Go higher! ⬆️ | Lives left: {lives}")
                elif guess > target_number:
                    lives -= 1
                    print(f"Hint: Go lower! ⬇️ | Lives left: {lives}")
                else:
                    guessed_correctly = True
                    print(f"🎉 Congratulations! You guessed the number in {attempts} attempts! 🎉")
            except ValueError:
                print("⚠️ Invalid input! Please enter a number between 1 and 100.")

        # If the player runs out of lives
        if lives == 0:
            print(f"😢 Game over! You ran out of lives. The correct number was {target_number}.")

        # Ask the player if they want to play again
        play_again = input("\nDo you want to guess another number? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Goodbye! 👋")
            break  # Exit the outer loop and end the game

# Run the game
number_guessing_game()

# %% [markdown]
# ---
# ## It uses **binary search logic** to provide hints and makes the game more challenging with a limited number of attempts.

# %% [markdown]
# ## Code Explanation
# 
# ### 1. **Random Number Generation**
# - The `random.randint(1, 100)` function generates a random integer between 1 and 100, which is the target number the user needs to guess.
# 
# ### 2. **Life Count**
# - The player starts with 3 lives (`lives = 3`).
# - After each wrong guess, the life count decreases by 1 (`lives -= 1`).
# 
# ### 3. **Game Loop**
# - The game runs in a `while` loop until the user guesses the correct number or runs out of lives.
# - The user is prompted to enter their guess, and the number of attempts is incremented.
# 
# ### 4. **Binary Search Logic**
# - If the guess is **less than** the target number, the game hints "Go higher!" and deducts one life.
# - If the guess is **greater than** the target number, the game hints "Go lower!" and deducts one life.
# - This logic mimics the **binary search algorithm**, where the search space is halved with each guess.
# 
# ### 5. **Input Validation**
# - The `try-except` block ensures the user enters a valid integer. If the input is invalid, the game prompts the user to try again.
# 
# ### 6. **Winning the Game**
# - When the user guesses the correct number, the game congratulates them and displays the number of attempts taken.
# 
# ### 7. **Losing the Game**
# - If the player runs out of lives, the game ends and reveals the correct number.
# 
# ### 8. **Restart Option**
# - After finishing a round, the player is asked if they want to play again.
# - If the player chooses "yes", the game restarts with a new random number.
# - If the player chooses "no", the game ends.

# %% [markdown]
# ---
# ### **Future Enhancements**
# 1. **Difficulty Levels**: Add different difficulty levels (e.g., smaller or larger ranges).
# 2. **Score System**: Implement a scoring system based on the number of attempts and remaining lives.
# 3. **GUI**: Create a graphical user interface (GUI) using libraries like `tkinter` or `PyQt`.
# 4. **Multiplayer Mode**: Allow two players to compete against each other.
# 
# This version of the game is more engaging and challenging, making it a great project to showcase your **algorithmic thinking** and **Python skills**! 🚀
# ---

# %%



