import random

def computer_guesses_number():
    print("Think of a number in a given range, and I'll try to guess it!")
    
    low = int(input("Enter the lower number: "))
    high = int(input("Enter the upper number: "))
    
    print(f"Now, think of a number between {low} and {high}. I will try to guess it!")
    input("Press Enter when you are ready...")
    
    attempts = 0
    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        print(f"Is your number {guess}? (Enter 'h' if it's higher, 'l' if it's lower, or 'c' if it's correct)")
        feedback = input().strip().lower()
        
        if feedback == 'c':
            print(f"Hooray! I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
    else:
        print("Something went wrong. Are you sure you gave correct feedback?")

if __name__ == "__main__":
    computer_guesses_number()
