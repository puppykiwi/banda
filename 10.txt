import random

MIN = 1
MAX = 20
TRIALS = 4

def main():
    print("*** Welcome to the secret number game! *** \nYou have 4 trials to guess the number between (1 - 20) \n")
    secret_number = random.randint(MIN, MAX)
    for i in range(TRIALS):
        user_input = input("Please enter a number: ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if user_input == secret_number:
            print(f"Congratulations! You guessed the secret number! [ {secret_number} ]")
            break
        elif user_input > secret_number:
            print("Your guess is too high.")
        elif user_input < secret_number:
            print("Your guess is too low.")
        else:
            print("Please enter a valid number.")
            continue

main()