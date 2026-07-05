import random


def guess_number():
    correct_number = random.randint(1, 10)
    guess_limit = 3
    guess_count = 0

    while guess_count < guess_limit:
        guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1

        if guess == correct_number:
            print("Congratulations! You guessed the number.")
            return

    print(f"Sorry, you failed to guess the number. It was {correct_number}.")


guess_number()
