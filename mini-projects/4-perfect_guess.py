import random

# Generate random number between 1 and 100
rand_int = random.randint(1, 100)
attempt = 0

while True:
    try:
        num = int(input("Enter your guess (1-100): "))
        attempt += 1

        if num < rand_int:
            print("Guess a little higher!")
        elif num > rand_int:
            print("Guess a little lower!")
        else:
            print(f"Congratulations! You guessed it right in {attempt} attempts.")
            break
    except ValueError:
        print("Please enter a valid number!")

# Save high score to a file
with open("score.txt", "+a") as f:
    f.write(f"....this is perfect guesse game score...\n (number of attempts): {attempt}")
    print("Your information has been saved in score.txt file.")
