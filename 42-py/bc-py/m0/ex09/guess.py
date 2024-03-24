import sys
import random

# generate a random number between 1 and 99
secret = random.randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

tries :int = 0
while True:
    tries += 1
    print("What's your guess between 1 and 99?")
    guess = input(">> ")

    if guess == "exit":
        print("Goodbye!")
        sys.exit()

    elif not guess.isdigit():
        print("That's not a number.")

    elif int(guess) == secret:
        if secret == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if tries == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in", tries, "attempts!")
        sys.exit()

    elif int(guess) > secret:
        print("Too high!")
    else:
        print("Too low!")