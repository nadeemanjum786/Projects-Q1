import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    
    # Get range from user
    lower = int(input("Enter the lower number of the range: "))
    upper = int(input("Enter the upper number of the range: "))
    
    if lower >= upper:
        print("Invalid range. The upper number must be greater than the lower number.")
        return
    
    # Generate a random number within the range
    secret_number = random.randint(lower, upper)
    attempts = 0
    
    while True:
        try:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))
            attempts += 1
            
            if guess < lower or guess > upper:
                print("Out of range! Try again.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Run the game
guess_the_number()
# In the above code, we have defined a function guess_the_number that allows the user to play a number guessing game.
# The function prompts the user to enter a lower and upper bound for the range of numbers.