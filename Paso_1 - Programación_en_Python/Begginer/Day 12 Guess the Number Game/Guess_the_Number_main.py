import random
from Logo import title

def start_the_game():
    """print the start of the game"""
    print(title)
    print("Welcome to the Number guessing Game!\nGood Luck! ")
    print("I'm thinking of a number between 1 and 100.🎲")

def difficulty_select():
    """asks the user to select the difficulty of the game"""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            attempts = 10
            return attempts
        elif difficulty == 'hard':
            attempts = 5
            return attempts
        else:
            print("Type a valid answer.")

def guessing_the_number_game():
    """Is the game of guessing the number"""
    start_the_game()
    attempts = difficulty_select()
    number = random.randint(1,100)
    while attempts > 0:
        """It will be played until there are no more attempts."""
        print(f"You have {attempts} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please, Type a valid number")
            continue 
        if guess > number:
            print("Too high.\nGuess again.")
        elif guess < number:
            print("Too low.\nGuess again.")
        else:
            print("You Win the Guessing Game.")
            print(f"The number i had thought of was {number}.\nCongratulations!! 🥳")
            return
        attempts -= 1
    print(f"Nooo. You lose. The number was {number}.😭")

play_again = 'y'
while play_again == 'y':
    guessing_the_number_game()
    play_again = input("You want play again? Type 'y' or 'n'. ")

