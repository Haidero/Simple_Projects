import random  # Ensure the random module is imported

number = random.randint(1, 10)  # Generate a random number between 1 and 10
guess = None  # Initialize guess to None

while guess != number:
    guess = int(input("Enter your guess number between 1 and 10: "))  # Get input from the user

    if guess < number:
        print("Too Low :(")  # Indented with 4 spaces
    elif guess > number:
        print("Too High :(")  # Indented with 4 spaces
    else:
        print("Congratulations! You guessed it right!")  # Indented with 4 spaces
