import random


secret_number = random.randint(1, 100)

print("Welcome to the guessing game!")
print("Guess the number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the right number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
'
