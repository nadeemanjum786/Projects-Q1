import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds into MM:SS
        timer = f"{mins:02}:{secs:02}"  # Format as MM:SS
        print(timer)  # Print each second on a new line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("⏰ Time's up! 🚀")

# Get user input for countdown time
try:
    total_seconds = int(input("Enter countdown time in seconds: "))
    countdown(total_seconds)
except ValueError:
    print("⚠️ Please enter a valid number!")

