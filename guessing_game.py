import random

def main():
    print("Guessing Game")
    print("There's a number between 1 and 50. Can you guess it?")

    secret_number = random.randint(1,50)
    guess = None
    attempts = 0

    while guess != secret_number:
        try:
            guess = int(input("Pick a numeber between 1 and 50: "))
            attempts += 1
            if guess < 1 or guess > 50:
                print("Error, please pick a number between 1 and 50!")
            elif guess < secret_number:
                print("Try again! Your guess is too low.")
            elif guess > secret_number:
                print("Try again! Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 50.")

if __name__ == "__main__":
    main()