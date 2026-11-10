import sys
from settings import secret_number as secret

def game():
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

# define max_guesses from a command-line argument

print(sys.argv)

try:
    max_guesses = int(sys.argv[1])
except IndexError:
    print("Usage: game.py max_guesses")
    exit()

game()