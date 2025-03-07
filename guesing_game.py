print("Welcome to the guessing game! You have to guess a number, and we have already chosen one.")

secret_number = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_guess_number = int(input("Guess the number = "))
    guess_count += 1

    if user_guess_number == secret_number:
        print("Congrats, you win! 🏆")
        break
    else:
        print("Wrong guess. Try again!")

if user_guess_number != secret_number:
    print("Unfortunately, you lose. 😔")

print("Made with ❤️ by Kumarjit")
