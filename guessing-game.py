# Function to handle the guessing game
def guess_number():
    # Import random module to generate a random number
    import random

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it.")
    
    attempts = 0  # Counter for attempts
    
    # Loop to give the player multiple attempts
    while True:
        guess = int(input("Enter your guess: "))  # Get the user's guess
        attempts += 1
        
        # Check the guess
        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break  # Exit the loop when the correct number is guessed

# Start the game
guess_number()