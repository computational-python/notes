import settings
secret = settings.secret_number

max_guesses = settings.max_number

for _ in range(max_guesses):
    guess = input("Guess a number: ")
    guess = int(guess)
    
    if guess > secret:
        print("Too large")
    elif guess < secret:
        print("Too small")
    else:
        print("You win")
        break
else: # executed in the absence of break
    print(f"You lose: the number was {secret}")


print("Game over")